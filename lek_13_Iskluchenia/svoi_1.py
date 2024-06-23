class UserException(Exception):
    pass


# А теперь добавим исключения для ошибок имени и возраста пользователя. Пока это будут исключения на минималках.

class UserAgeError(UserException):
    pass


class UserNameError(UserException):
    pass
