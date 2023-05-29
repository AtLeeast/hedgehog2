from rest_framework.exceptions import APIException


class InvalidPasswordException(APIException):
    status_code = 400


class TooSmallPasswordException(InvalidPasswordException):
    default_detail = "Слишком маленький пароль (мин. длина 8 символов). Такие пароли проще взломать!"
    default_code = "too_small_password"


class TooBigPasswordException(InvalidPasswordException):
    default_detail = "Слишком длинный пароль (макс. длина 50 символов)."
    default_code = "too_big_password"


class TooEasyPasswordException(InvalidPasswordException):
    default_detail = "Неправильный формат введеного пароля. Используйте строчные и заглавные буквы английского алфавита и цифры!"
    default_code = "too_easy_password"


class InvalidEmailException(APIException):
    status_code = 400


class TooBigEmailException(InvalidEmailException):
    default_detail = "Слишком длинный адрес электронной почты (макс. длина 50 символов)."
    default_code = "too_big_email"


class WrongEmailFormatException(InvalidEmailException):
    default_detail = "Неправильный формат введеной электронной почты."
    default_code = "wrong_email_format"


class EmptyUserFormFieldsException(APIException):
    status_code = 400
    default_detail = "Введены пустые данные"
    default_code = "empty_user_form_fields"
