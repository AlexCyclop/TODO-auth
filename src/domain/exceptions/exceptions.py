class DomainException(Exception):
    pass


class UserAlreadyExistsError(DomainException):
    pass


class UserNotFoundError(DomainException):
    pass
