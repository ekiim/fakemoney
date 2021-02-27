import unittest
import fakemoney.utils
from fakemoney.types import email


class TestFakeMoneyUtils(unittest.TestCase):
    def test_nested_dict_get_aggreaged_tautology(self):
        class aggegated:
            get = lambda j, i: True
        value = fakemoney.utils.nested_dict_get(aggegated, None)

    def test_nested_dict_get_aggreaged_dict_valid(self):
        test_value = "test value"
        test_dict = dict(value=test_value)
        value = fakemoney.utils.nested_dict_get(test_dict, "value")
        assert value == test_value

    def test_nested_dict_get_aggreaged_dict_invalid(self):
        test_value = "test value"
        test_dict = dict(value=test_value)
        value = fakemoney.utils.nested_dict_get(test_dict, "invalid")
        assert value is None

    def test_is_valid_constructor_call(self):
        is_valid_func = fakemoney.utils.isValidConstructor({})
        assert callable(is_valid_func)

    def test_is_valid_constructor_call_empty_empty(self):
        is_valid_func = fakemoney.utils.isValidConstructor({})
        assert is_valid_func({}) == False

    def test_is_valid_constructor_call_fields_builtin_data_empty(self):
        fields = { "name": str }
        is_valid_func = fakemoney.utils.isValidConstructor(fields)
        data = {}
        assert is_valid_func(data) == False

    def test_is_valid_constructor_call_fields_builtin_data_overloaded(self):
        fields = { "name": str }
        is_valid_func = fakemoney.utils.isValidConstructor(fields)
        data = {"name": "Alejandro", "last": "Salgado"}
        assert is_valid_func(data) == False

    def test_is_valid_constructor_call_fields_builtin_data_valid_one(self):
        fields = { "name": str }
        is_valid_func = fakemoney.utils.isValidConstructor(fields)
        data = {"name": "Alejandro"}
        assert is_valid_func(data) == True

    def test_is_valid_constructor_call_fields_builtin_data_valid_int(self):
        fields = { "name": str, "age": int}
        is_valid_func = fakemoney.utils.isValidConstructor(fields)
        data = {"name": "Alejandro", "age": 26}
        assert is_valid_func(data) == True

    def test_is_valid_constructor_call_fields_builtin_data_valid_int_float(self):
        fields = { "name": str, "age": int, "score": float}
        is_valid_func = fakemoney.utils.isValidConstructor(fields)
        data = {"name": "Alejandro", "age": 26, "score": 9.75}
        assert is_valid_func(data) == True

    def test_is_valid_constructor_call_fields_custom_data_valid(self):
        fields = { "name": str, "age": int, "score": float, "email": email}
        is_valid_func = fakemoney.utils.isValidConstructor(fields)
        data = {"name": "Alejandro", "age": 26, "score": 9.75, "email": "test@ekiim.xyz"}
        assert is_valid_func(data) == True
