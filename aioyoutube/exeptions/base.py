class YoutubeApiError(Exception):
    """Base class for youtube api exceptions"""

    def __init__(self, mess: str, code: int = None, json: dict = None):
        self._mess = mess
        self._code = code
        self._json = json

    def __repr__(self):
        return f'{self.__class__.__name__} code={self.code} mess={self.mess}'

    def __str__(self):
        return f'code={self.code} mess={self.mess}'

    @property
    def mess(self) -> str:
        return self._mess

    @property
    def code(self) -> int:
        return self._code

    @property
    def json(self) -> dict:
        return self._json
