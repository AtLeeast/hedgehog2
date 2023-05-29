import re
from .account_data_exceptions import *


class AccountDataValidator:
    @staticmethod
    def validate(email: str, password: str):
        AccountDataValidator.validate_emptiness(email, password)
        AccountDataValidator._validate_password(password)
        AccountDataValidator._validate_email(email)

    @staticmethod
    def validate_emptiness(email: str, password: str):
        if email == "" or password == "":
            raise EmptyUserFormFieldsException

    @staticmethod
    def _validate_password(password: str):
        print(len(password))
        if len(password) < 8:
            raise TooSmallPasswordException
        if len(password) > 50:
            raise TooBigPasswordException
        if not (re.search("[a-z]", password)
                and re.search("[A-Z]", password)
                and re.search("[0-9]", password)):
            raise TooEasyPasswordException

    @staticmethod
    def _validate_email(email: str):
        if len(email) > 50:
            raise TooBigEmailException
        if not AccountDataValidator._is_valid_email(email):
            raise WrongEmailFormatException

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
