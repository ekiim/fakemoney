from copy import deepcopy
import datetime as dt
from marshmallow import Schema, fields, validates, validates_schema, ValidationError, pre_load
import phonenumbers

from fakemoney.utils import StringToBase64
import fakemoney.exceptions as exceptions


class CRUDSchema(Schema):
    created_at = fields.DateTime()
    modified_at = fields.DateTime()

class Phone:
    def __init__(self, phone):
        if isinstance(phone, phonenumbers.PhoneNumber):
            self.phone = phone
        else:
            self.phone = phonenumbers.parse(phone, None)

    def __str__(self):
        return phonenumbers.format_number(self.phone, phonenumbers.PhoneNumberFormat.E164)

    def __repr__(self):
        return self.__str__()


    def is_valid(self):
        return phonenumbers.is_valid_number(self.phone)

    def encode(self, *args, **kwargs):
        return str(self).encode(*args, **kwargs)

class PhoneField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return str(value)

    def _deserialize(self, value, attr, data, **kwargs):
        phone = None
        try:
            phone = Phone(value)
            valid = phone.is_valid()
            if not valid:
                raise Exception()
        except Exception as error:
            raise ValidationError("Phone Number Error")
        return phone

class PersonalData(Schema):
    birthdate = fields.Date("%Y-%m-%d")
    first_name = fields.Str(required=True)
    middle_name = fields.Str()
    last_name_1 = fields.Str(required=True)
    last_name_2 = fields.Str()

    @validates_schema
    def validates_schema(self, data, **kwargs):
        if (
            len(data["first_name"]) == 0
            or
            len(data["last_name_1"]) == 0
        ):
            raise ValidationError("Not a valid name")

class User(CRUDSchema):
    email = fields.Email()
    phone = PhoneField()

class UserFull(User):
    password = fields.Str(required=True)
    personal_data = fields.Nested(PersonalData, required=True)

class UserSignUp(UserFull):
    password_confirmation = fields.Str(required=True)

    @validates_schema
    def password_validation(self, data, **kwargs):
        if data["password"] != data["password_confirmation"]:
            raise exceptions.PasswordsDoNotMatch()

class UserLogIn(User):
    password = fields.Str()

    @validates_schema
    def validate_schema(self, data, **kwargs):
        if not data.get("email") and not data.get("phone"):
            raise exceptions.AuthNoUserProvided()

