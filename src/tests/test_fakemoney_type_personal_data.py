import unittest
import fakemoney.personal_data
from datetime import date


class TestFakeMoneyTypesPersonalData(unittest.TestCase):
    def test_create_default(self):
        personal_data = fakemoney.personal_data.create()
        assert isinstance(personal_data, dict)
        assert len(personal_data) == 5
        assert all((value is None for value in personal_data.values()))


    def test_create_with_valid_data(self):
        first = "Miguel"
        middle = "Alejandro"
        lastname_1 = "Salgado"
        lastname_2 = "Zapien"
        birthdate = date(1994,12,23)

        personal_data = fakemoney.personal_data.create(
            first=first,
            middle=middle,
            lastname_1=lastname_1,
            lastname_2=lastname_2,
            birthdate=birthdate
        )
        assert personal_data['first'] == first
        assert personal_data['middle'] == middle
        assert personal_data['lastname_1'] == lastname_1
        assert personal_data['lastname_2'] == lastname_2
        assert personal_data['birthdate'] == birthdate

    def test_validate_none_instead_of_empty(self):
        first = "Miguel"
        middle = None
        lastname_1 = "Salgado"
        lastname_2 = None
        birthdate = date(1994,12,23)
        personal_data = fakemoney.personal_data.create(
            first=first,
            middle=middle,
            lastname_1=lastname_1,
            lastname_2=lastname_2,
            birthdate=birthdate
        )
        valid = fakemoney.personal_data.validate(personal_data)
        assert valid == False

    def test_validate_valid_with_empty(self):
        first = "Miguel"
        middle = ""
        lastname_1 = "Salgado"
        lastname_2 = ""
        birthdate = date(1994,12,23)
        personal_data = fakemoney.personal_data.create(
            first=first,
            middle=middle,
            lastname_1=lastname_1,
            lastname_2=lastname_2,
            birthdate=birthdate
        )
        valid = fakemoney.personal_data.validate(personal_data)
        assert valid == True

    def test_validate_invalid_firstname(self):
        first = ""
        middle = ""
        lastname_1 = "Salgado"
        lastname_2 = ""
        birthdate = date(1994,12,23)
        personal_data = fakemoney.personal_data.create(
            first=first,
            middle=middle,
            lastname_1=lastname_1,
            lastname_2=lastname_2,
            birthdate=birthdate
        )
        valid = fakemoney.personal_data.validate(personal_data)
        assert valid == False


    def test_validate_invalid_lastname(self):
        first = "Miguel"
        middle = ""
        lastname_1 = " "
        lastname_2 = ""
        birthdate = date(1994,12,23)
        personal_data = fakemoney.personal_data.create(
            first=first,
            middle=middle,
            lastname_1=lastname_1,
            lastname_2=lastname_2,
            birthdate=birthdate
        )
        valid = fakemoney.personal_data.validate(personal_data)
        assert valid == False

    def test_validate_invalid_birthdate(self):
        first = "Miguel"
        middle = ""
        lastname_1 = "Salgado"
        lastname_2 = ""
        birthdate = ""
        personal_data = fakemoney.personal_data.create(
            first=first,
            middle=middle,
            lastname_1=lastname_1,
            lastname_2=lastname_2,
            birthdate=birthdate
        )
        valid = fakemoney.personal_data.validate(personal_data)
        assert valid == False
