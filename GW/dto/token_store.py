from datetime import datetime, timedelta

from conf import settings

class AuthTokenMissing(Exception):
    pass


class AuthTokenExpired(Exception):
    pass


class AuthTokenCorrupted(Exception):
    pass

class TokenStorage:
    def __init__(self):
        self.token = None
        self.expired = datetime.utcnow() +  timedelta(
            minutes=settings.ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES) 


token_storage = TokenStorage()

