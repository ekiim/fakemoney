from shutil import rmtree
from os import makedirs
import json
import unittest
import server.modules.storage as storage


class TestFileCollectionsStorage(unittest.TestCase):
    def setUp(self):
        self.storage_void = "/tmp/fakemoney_test_storage_void"
        self.storage_empty = "/tmp/fakemoney_test_storage_empty"
        self.storage_filled = "/tmp/fakemoney_test_storage_filled"
        self.collection_name = "test_collection"
        self.initial_record_name = '0.0-test.json'
        makedirs(self.storage_empty, exist_ok=True)
        makedirs(self.storage_filled, exist_ok=True)
        makedirs("/".join([
            self.storage_filled,
            self.collection_name
        ]), exist_ok=True)
        filename = "/".join([
            self.storage_filled, self.collection_name, self.initial_record_name
        ])
        self.initial_record_data = dict(data="test")
        json_data = json.dumps(self.initial_record_data)
        with open(filename, 'w') as file:
            file.write(json_data)

    def tearDown(self):
        rmtree(self.storage_void, ignore_errors=True)
        rmtree(self.storage_empty, ignore_errors=True)
        rmtree(self.storage_filled, ignore_errors=True)

    def test_query_to_unexisting_storage(self):
        query_result = storage.query_collection(
            self.collection_name, storage_dir=self.storage_void
        )
        assert query_result == []

    def test_query_to_empty_storage(self):
        query_result = storage.query_collection(
            self.collection_name, storage_dir=self.storage_empty
        )
        assert query_result == []

    def test_query_to_filled_storage(self):
        query_result = storage.query_collection(
            self.collection_name, storage_dir=self.storage_filled
        )
        assert len(query_result) == 1
        assert query_result[0] == self.initial_record_name

    def test_query_to_filled_storage_by_filer_func(self):
        filter_func = lambda d: self.initial_record_name == d
        query_result = storage.query_collection(
            self.collection_name,
            filter_func=filter_func,
            storage_dir=self.storage_filled
        )
        assert len(query_result) == 1
        assert query_result[0] == self.initial_record_name

    def test_retrieve_record(self):
        retrieve_data = storage.retrieve_record(
            self.collection_name,
            self.initial_record_name,
            self.storage_filled
        )
        retrieve_keys_count = len(retrieve_data.keys())
        wanted_keys_count = len(self.initial_record_data.keys())
        assert retrieve_keys_count == wanted_keys_count
        for (key, value) in self.initial_record_data.items():
            assert key in retrieve_data.keys()
            assert value == retrieve_data[key]

    def test_retrieve_record_fail(self):
        self.assertRaises(
            Exception,
            storage.retrieve_record,
            self.collection_name,
            "Invalid_name",
            self.storage_filled
        )
