from os import environ
from datetime import date
from time import time
from urllib.parse import urlparse
import re
import uuid

builtins = [str, int, float, bool]

from fakemoney.types import builtins

def nested_dict_get(agregated, current):
    return agregated.get(current, None)

def single_value_validate(value, _type):
    valid_check = True
    if value is None:
        valid_check = False
    elif _type in builtins:
        valid_check &= value == _type(value)
    else:
        valid_check &= _type.validate(value)
    return valid_check

def isValidConstructor(fields={}):
    def isValid(data={}):
        valid_check = bool(len(fields))
        for (key, _type) in fields.items():
            try:
                value = data[key]
                valid_check &= single_value_validate(value, _type)
                del data[key]
            except KeyError:
                valid_check = False
                break
        return (len(data.keys()) == 0) and valid_check
    return isValid


class email:
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    @staticmethod
    def validate(_email):
        returnable = False
        if re.search(email.regex, _email):
            returnable = True
        return returnable

class phone:
    """
    Validacion para numeros telefonicos
    Por lo pronto nos interesan numeros telefonicos
    con prefijo
        +1
        +52
    """
    country_codes = ["1", "52"]
    @staticmethod
    def validate(number):
        v_line = len(number[-7:]) == 7
        v_area = len(number[-10:-7]) == 3
        v_cc = number[1:-10] in phone.country_codes
        returnable = (number[0] == "+" and v_line and v_area and v_cc)
        return returnable


class md5:
    regex = r"([a-fA-F\d]{32})"
    @staticmethod
    def validate(_md5=""):
        returnable = False
        if re.search(md5.regex, _md5):
            returnable = True
        return returnable


class url:
    @staticmethod
    def validate(_url):
        returnable = False
        try:
            parsed = urlparse(_url)
            if len(parsed.scheme) in [4,5] and parsed.scheme in 'https':
                returnable = True
        except:
            pass
        return returnable

class birthdate:
    @staticmethod
    def validate(_date):
        return isinstance(_date, date)

class str_nonempty(str):
    @staticmethod
    def validate(_str):
        returnable = False
        try:
            returnable = len(_str.replace(" ","")) and str(_str) == _str
        except:
            pass
        return returnable

class UUID:
    @staticmethod
    def validate(_uuid):
        returnable = False
        try:
            _uuid_regen = uuid.UUID(str(_uuid))
            returnable = _uuid == _uuid_regen
        except:
            pass
        return returnable

    @staticmethod
    def create(_path, timestamp=None, _collection=None):
        if timestamp is None:
            timestamp = time()
        if _collection is None:
            collection = "generic"
        namespace = uuid.NAMESPACE_URL
        _url = "/".join([
            environ["DEPLOY_DOMAIN"],
            str(timestamp),
            str(_path)
        ])
        return uuid.uuid3(namespace, _url)

def list_of(_type):
    class list_of_type:
        @staticmethod
        def validate(_list):
            valid_check = True
            for elem in _list:
                valid_check &= single_value_validate(elem, _type)
            return valid_check
    return list_of_type
