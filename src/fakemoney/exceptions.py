class FakeMoneyException(Exception):
    message = "Fakemoney Error: Generic"

class PasswordsDoNotMatch(FakeMoneyException):
    message = "Passwords do not match"

class PhoneNumberCountryError(FakeMoneyException):
    message = "Country code not supported"

class PhoneNumberFormat(FakeMoneyException):
    message = "Phone number not formated properly"

class EmailFormat(FakeMoneyException):
    message = "Not a valid email"

class DateFormatError(FakeMoneyException):
    message = "Date not in ISO format."

class UserAlreadyExists(FakeMoneyException):
    message = "User already exists"

class UserNotFound(FakeMoneyException):
    message = "User Not Found"

class AuthNoUserProvided(FakeMoneyException):
    message = "No User Email or Phone Provided"

class BadInputStructure(FakeMoneyException):
    message = "Bad Input Structure"
