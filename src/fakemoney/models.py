import datetime as dt
from time import time
from marshmallow import ValidationError
import filestorage.storage as storage
from fakemoney.utils import StringToBase64
import fakemoney.schemas as schemas
import fakemoney.exceptions as exceptions
from fakemoney.utils import hash_password, verify_password, jwt_sign

class User:
    collection = "users"
    def __init__(self, data):
        self.data = data
        self._file = None
        self.exists = False
        try:
            self.get_record()
            self.exists = True
        except exceptions.UserNotFound:
            pass

    @property
    def filename(self):
        if self._file is not None:
            returnable = self._file
        else:
            b64_email, b64_phone = "", ""
            data = self.data
            if "email" in data:
                b64_email = StringToBase64(data["email"])
            if "phone" in data:
                b64_phone = StringToBase64(data["phone"])
            returnable = f"{b64_email}_{b64_phone}"
        return returnable

    def find(self):
        files = storage.query_collection(
            self.collection,
            lambda f: self.filename in f
        )
        return files

    def get_record(self):
        try:
            record_found = self.find()
            record_name = record_found[0]
            self._file = record_name
        except IndexError:
            raise exceptions.UserNotFound()
        record_data = storage.retrieve_record(
            self.collection,
            record_name
        )
        schema = schemas.UserFull()
        data = schema.load(record_data)
        self.data = data

    def save(self):
        now = dt.datetime.today()
        self.data["modified_at"] = now

    def create(self):
        now = dt.datetime.today()
        now_iso = now.isoformat()
        self.data["created_at"] = now
        self.data["modified_at"] = now
        self.data["password"] = hash_password(self.data["password"])
        schema = schemas.UserFull()
        data_str = schema.dumps(self.data)
        filename = storage.store_new_record(
            self.collection,
            self.filename,
            data_str,
            timestamp=now_iso
        )
        self._file = str(filename)
        return self._file

    def verify_password(self, password):
        return verify_password(self.data["password"], password)

    def generate_token(self):
        return jwt_sign({
            "sub": self.filename,
            "iat": time()
        })

    @classmethod
    def signup(cls, data):
        try:
            schema = schemas.UserSignUp()
            data = schema.load(data)
        except ValidationError as e:
            error = e.normalized_messages()
            if "email" in error:
                raise exceptions.EmailFormat()
            elif "phone" in error:
                raise exceptions.PhoneNumberFormat()
            else:
                raise exceptions.BadInputStructure()
        obj = User(data)
        if len(obj.find()) > 0:
            raise exceptions.UserAlreadyExists()
        file = obj.create()
        return obj

    @classmethod
    def login(cls, data):
        try:
            schema = schemas.UserLogIn()
            data = schema.load(data)
            password = data["password"]
            user = User(data)
        except ValidationError as e:
            error = e.normalized_messages()
            if "email" in error:
                raise exceptions.EmailFormat()
            if "phone" in error:
                raise exceptions.PhoneNumberFormat()
            else:
                raise exceptions.BadInputStructure()
        return user.exists and user.verify_password(password) and user
