import unittest
import fakemoney.picture
import fakemoney.defaults


class TestFakeMoneyTypesPictures(unittest.TestCase):
    def test_create_default(self):
        picture_data = fakemoney.picture.create()
        assert picture_data['url'] == fakemoney.defaults.picture
        assert picture_data['filename'] == 'avatar2.png'

    def test_create_with_valid_data(self):
        url = 'https://test/image.png'
        filename = "test.png"
        picture_data = fakemoney.picture.create(url=url, filename=filename)
        assert picture_data['url'] == url
        assert picture_data['filename'] == filename

    def test_create_with_valid_url_only(self):
        url = 'https://test/image.png'
        picture_data = fakemoney.picture.create(url=url)
        assert picture_data['url'] == url
        assert picture_data['filename'] == 'image.png'

    def test_create_with_valid_filename_only(self):
        filename = 'image.png'
        picture_data = fakemoney.picture.create(filename=filename)
        assert picture_data['url'] is fakemoney.defaults.picture
        assert picture_data['filename'] == 'image.png'


    def test_validate_valid(self):
        url = 'https://test/image.png'
        filename = "test.png"
        picture_data = fakemoney.picture.create(url=url, filename=filename)
        assert fakemoney.picture.validate(picture_data) == True

    def test_validate_invalid_url_schema(self):
        url = 'ftp://test/image.png'
        filename = "test.png"
        picture_data = fakemoney.picture.create(url=url, filename=filename)
        assert fakemoney.picture.validate(picture_data) == False

    def test_validate_invalid_url_type(self):
        url = 1
        filename = "test.png"
        picture_data = fakemoney.picture.create(url=url, filename=filename)
        assert fakemoney.picture.validate(picture_data) == False

    def test_validate_invalid_filename_type(self):
        url = 'http://test/image.png'
        filename = 1
        picture_data = fakemoney.picture.create(url=url, filename=filename)
        assert fakemoney.picture.validate(picture_data) == False
