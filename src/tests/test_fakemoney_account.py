import uuid
import time
import unittest
import fakemoney.account
import fakemoney.defaults

class TestFakeMoneyTypesPictures(unittest.TestCase):
    def test_create_default(self):
        account_data = fakemoney.account.create()
        assert isinstance(account_data, dict)
        assert account_data["owner"] is None
        assert account_data["picture"]["url"] == fakemoney.defaults.picture
        assert isinstance(account_data["users"], list)
        assert isinstance(account_data["blocked"], bool)

    def test_create_with_owner_valid(self):
        owner = "info@ekiim.xyz"
        account_data = fakemoney.account.create(
            owner=owner
        )
        assert isinstance(account_data, dict)
        assert account_data["owner"] == owner
        assert account_data["picture"]["url"] == fakemoney.defaults.picture
        assert isinstance(account_data["users"], list)
        assert isinstance(account_data["blocked"], bool)
        assert fakemoney.account.validate(account_data)

    def test_create_with_owner_time_valid(self):
        owner = "info@ekiim.xyz"
        timestamp = time.time()
        account_data = fakemoney.account.create(
            owner=owner,
            timestamp=timestamp
        )
        assert isinstance(account_data, dict)
        assert account_data["owner"] == owner
        assert account_data["picture"]["url"] == fakemoney.defaults.picture
        assert isinstance(account_data["users"], list)
        assert isinstance(account_data["blocked"], bool)
        assert fakemoney.account.validate(account_data)

    def test_validate_valid_minimal(self):
        account = {
            "created_time": 10.0,
            "uuid": uuid.uuid4(),
            "owner": "info@ekiim.xyz",
            "picture": {
                "filename":"example.png",
                "url": "https://test/example.png"
            },
            "users": [],
            "blocked": True
        }
        assert fakemoney.account.validate(account)

    def test_validate_invalid_default(self):
        account = fakemoney.account.create()
        assert fakemoney.account.validate(account) == False

    def test_validate_invalid(self):
        account = {
            "created_time": 10.0,
            "uuid": uuid.uuid4(),
            "owner": " ",
            "picture": {
                "filename":"example.png",
                "url": "https://test/example.png"
            },
            "users": [],
            "blocked": True
        }
        assert fakemoney.account.validate(account) == False
