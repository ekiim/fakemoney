import re
from urllib.parse import urlparse

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
        parsed = urlparse(_url)
        if len(parsed.scheme) in [4,5] and parsed.scheme in 'https':
            returnable = True
        return returnable
