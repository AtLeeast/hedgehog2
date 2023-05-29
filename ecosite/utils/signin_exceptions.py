from rest_framework.exceptions import APIException


class UserWithThisEmailDoesNotExistException(APIException):
    status_code = 400
    default_detail = "Пользователя с заданной почтой не существует"
    default_code = "user_with_this_email_does_not_exist"


class NotCorrectPasswordGivenException(APIException):
    status_code = 400
    default_detail = "Пароль который был введен не соотвествует действительному. Попробуйте еще раз"
    default_code = "password_is_not_correct"


class NotCorrectEmailGivenException(APIException):
    status_code = 400
    default_detail = "Пользователя с заданной почтой не существует"
    default_code = "email_is_not_correct"
