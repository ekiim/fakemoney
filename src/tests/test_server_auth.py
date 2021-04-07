from os import environ
from shutil import rmtree
import unittest
from webtest import TestApp
import server.app



class TestBottleAuth(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(server.app.app)
        self.storage_dir = environ["STORAGE_DIR"]
        try:
            rmtree(self.storage_dir)
        except FileNotFoundError:
            pass

        self.valid_user = {
                "email": "test@fakemoney.ekiim.xyz",
                "phone": "+526640001111",
                "password": "password_test",
                "password_confirmation": "password_test",
                "personal_data": {
                    "first_name": "José",
                    "middle_name": "Rómulo",
                    "last_name_1": "Sosa",
                    "last_name_2": "Ortiz",
                    "birthdate": "1948-02-17"
                }
            }


    def tearDown(self):
        try:
            rmtree(self.storage_dir)
        except FileNotFoundError:
            pass

    def test_signup(self):
        response = self.app.post_json("/auth/signup", self.valid_user)
        assert response.json["code"] == 201

    def test_signup_different_passwords(self):
        data = self.valid_user
        data["password_confirmation"] = "something different"
        code = 406
        response = self.app.post_json("/auth/signup", data, status=code)
        assert response.json["code"] == code

    def test_signup_no_middle_name(self):
        data = self.valid_user
        data["personal_data"]["middle_name"] = ""
        code = 201
        response = self.app.post_json("/auth/signup", data, status=code)
        assert response.json["code"] == code

    def test_signup_no_middle_name(self):
        data = self.valid_user
        data["personal_data"]["last_name_2"] = ""
        code = 201
        response = self.app.post_json("/auth/signup", data, status=code)
        assert response.json["code"] == code

    def test_signup_no_first_name(self):
        data = self.valid_user
        data["personal_data"]["first_name"] = ""
        code = 406
        response = self.app.post_json("/auth/signup", data, status=code)
        assert response.json["code"] == code

    def test_signup_again(self):
        self.test_signup()
        data = self.valid_user
        code = 406
        response = self.app.post_json("/auth/signup", data, status=code)
        assert response.json["code"] == code
