from functools import reduce
from fakemoney.types import builtins

def nested_dict_get(agregated, current):
    return agregated.get(current, None)


def isValidConstructor(fields={}):
    def isValid(data={}):
        valid_check = bool(len(fields))
        for (key, _type) in fields.items():
            try:
                value = data[key]
                if value is None:
                    valid_check = False
                    break
                elif _type in builtins:
                    valid_check &= value == _type(value)
                else:
                    valid_check &= _type.validate(value)
                del data[key]
            except KeyError:
                valid_check = False
                break
        return (len(data.keys()) == 0) and valid_check
    return isValid
