import fakemoney.utils as utils
import fakemoney.types as types


fields = {
    "first": types.str_nonempty,
    "middle": str,
    "lastname_1": types.str_nonempty,
    "lastname_2": str,
    "birthdate": types.birthdate
}


validate = utils.isValidConstructor(fields)


def create(
    first=None,
    middle=None,
    lastname_1=None,
    lastname_2=None,
    birthdate=None
):
    return {
        "first": first,
        "middle": middle,
        "lastname_1": lastname_1,
        "lastname_2": lastname_2,
        "birthdate": birthdate
    }
