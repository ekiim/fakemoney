import unittest
from fakemoney.schemas import Phone, PhoneField
from marshmallow import Schema, ValidationError

class PhoneSchema(Schema):
    phone = PhoneField()

class TestFakeMoneySchemasPhone(unittest.TestCase):

    def test_phone_class(self):
        phone = "+526641231234"
        phone_obj = Phone(phone)
        assert phone == str(phone_obj)

