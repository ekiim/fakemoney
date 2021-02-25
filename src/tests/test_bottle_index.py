import unittest
from webtest import TestApp
import server.app


class TestBottleIndex(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(server.app.app)

    def test_index(self):
        response = self.app.get("/")
        assert response.status_code == 200
