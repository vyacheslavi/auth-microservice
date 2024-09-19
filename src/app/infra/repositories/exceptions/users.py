from .base import BaseException  # noqa


class UserAlreadyExist(BaseException):
    email: str

    @property
    def message(self):
        return f"User with email {self.email} already exists"
