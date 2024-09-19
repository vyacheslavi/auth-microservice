class BaseException(Exception):  # noqa
    @property
    def message(self):
        return "A base exceptions raised"
