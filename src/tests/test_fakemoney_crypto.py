import unittest
from fakemoney.utils import verify_password, hash_password

class TestFakeMoneyPassword(unittest.TestCase):
    def test_same_password(self):
        password = "hello_world"
        hashed = hash_password(password)
        assert verify_password(hashed, password)

    def test_different_password(self):
        password = "hello_world"
        hashed = hash_password(password)
        assert not verify_password(hashed, "not_the_same")
