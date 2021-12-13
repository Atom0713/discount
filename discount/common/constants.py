from enum import Enum


class HTTPMethodsConst:
    POST = 'POST'
    GET = 'GET'


class UserTypeConst(Enum):
    MERCHANT = 1
    USER = 2


class CustomResponse:
    OK = {'status': 'ok', 'message': 'Request successfully evaluated.'}
    FAILED = {'status': 'failed',  'message': 'Request failed.'}
    FAILED_TO_AUTHENTICATE = {'status': 'failed', 'message': 'Authentication failed.'}
    INVALID_TOKEN = {'status': 'failed', 'message': 'a valid token is missing'}

    @staticmethod
    def ok_with_kwargs(**kwargs):
        response: dict = CustomResponse.OK.copy()
        return {**response, **kwargs}

    @staticmethod
    def failed_with_kwargs(**kwargs):
        response: dict = CustomResponse.FAILED.copy()
        return {**response, **kwargs}


class SQSTopicsConst(Enum):
    SHARE_USER_INFO = 1
