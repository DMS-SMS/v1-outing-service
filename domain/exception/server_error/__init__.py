from typing import Optional

from domain.exception.grpc_exception import gRPCException


class ServerErrorException(gRPCException):
    def __init__(self):
        self.status = 500
        self.code = -1000
        self.msg = "Server Error"