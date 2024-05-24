from rest_framework import status
from rest_framework.exceptions import APIException


class HandleExceptionResponse(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A custom error occurred.'

    def __init__(self, detail=None, status_code=None, code=None):
        if status_code is not None:
            self.status_code = status_code
        super(HandleExceptionResponse, self).__init__(detail, code)
