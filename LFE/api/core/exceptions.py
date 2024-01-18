from typing import Any
from rest_framework.exceptions import APIException

from api.data.constant import USER_ERR_3


class IDNotFound(APIException):
    def __init__(self, id: Any):
        self.status_code = 404
        self.detail = USER_ERR_3.format(id=id)
        self.code = 'no_found'
        super().__init__(detail=self.detail, code=self.code)
