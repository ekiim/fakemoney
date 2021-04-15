from os import environ
from shutil import rmtree
from copy import deepcopy
import unittest
from fakemoney.models import User
from fakemoney.exceptions import *


class TestFakeMoneyAuthBase(unittest.TestCase):
    def setUp(self):
        self.valid_personal_data = {
                "first_name": "José",
                "middle_name": "Rómulo",
                "last_name_1": "Sosa",
                "last_name_2": "Ortiz",
                "birthdate": "1948-02-17"
            }
        self.valid_user = {
            "email": "test@fakemoney.ekiim.xyz",
            "phone": "+526641231234",
            "password": "password_test",
            "personal_data": self.valid_personal_data
        }
        self.storage_dir = environ["STORAGE_DIR"]
        try:
            rmtree(self.storage_dir)
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            rmtree(self.storage_dir)
        except FileNotFoundError:
            pass

class TestFakeMoneyUserRegistration(TestFakeMoneyAuthBase):
    def test_00_signup(self):
        data = deepcopy(self.valid_user)
        data["password_confirmation"] = "password_test"
        user = User.signup(data)
        assert isinstance(user, User)
        filename = user.filename
        filename_parts = filename.split("_")
        assert len(filename) > 0
        assert len(filename_parts) == 3
        assert user.find()

    def test_01_login_email(self):
        self.test_00_signup()
        data = dict(
            email=self.valid_user["email"],
            password=self.valid_user["password"]
        )
        user = User.login(data)
        assert user
        assert isinstance(user, User)

    def test_02_login_phone(self):
        self.test_00_signup()
        data = dict(
            phone=self.valid_user["phone"],
            password=self.valid_user["password"]
        )
        user = User.login(data)
        assert user
        assert isinstance(user, User)

    def test_03_login_email_non_existing_user_email(self):
        self.test_00_signup()
        data = dict(
            email="test@test.com",
            password=self.valid_user["password"]
        )
        user = User.login(data)
        assert not user

    def test_03_login_email_non_existing_user_phone(self):
        self.test_00_signup()
        data = dict(
            phone="+526649991111",
            password=self.valid_user["password"]
        )
        user = User.login(data)
        assert not user

    def test_03_login_email_bad_password(self):
        self.test_00_signup()
        data = dict(
            email="test@test.com",
            password="not_real_password"
        )
        user = User.login(data)
        assert not user



class TestFakeMoneyUsers(TestFakeMoneyAuthBase):
    def test_signup(self):
        data = deepcopy(self.valid_user)
        data["password_confirmation"] = "password_test"
        user = User.signup(data)
        assert isinstance(user, User)
        filename = user.filename
        assert len(filename) > 0
        assert len(user.find()) == 1

    def test_signup_password_does_not_match(self):
        data = deepcopy(self.valid_user)
        data["password_confirmation"] = "123"
        with self.assertRaises(PasswordsDoNotMatch):
            user = User.signup(data)

    def test_signup_bad_phone(self):
        data = deepcopy(self.valid_user)
        data["password_confirmation"] = "password_test"
        data["phone"] = "123"
        with self.assertRaises(PhoneNumberFormat):
            user = User.signup(data)

    def test_signup_bad_email(self):
        data = deepcopy(self.valid_user)
        data["password_confirmation"] = "password_test"
        data["email"] = "something(at)else.com"
        with self.assertRaises(EmailFormat):
            user = User.signup(data)

    def test_signup_extra_fields(self):
        data = deepcopy(self.valid_user)
        data["extra"]= {"field": "value"}
        with self.assertRaises(BadInputStructure):
            user = User.signup(data)

    def test_signup_missing_personal_data(self):
        data = deepcopy(self.valid_user)
        del data["personal_data"]
        with self.assertRaises(BadInputStructure):
            user = User.signup(data)
