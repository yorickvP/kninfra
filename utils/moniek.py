#!/usr/bin/env python
# vim: et:sta:bs=2:sw=4:
import _import  # noqa: F401
from django.conf import settings

import protobufs.messages.moniek_pb2_grpc as moniek_pb2_grpc
from kn.utils.moniek.service import Moniek
from microservice import Microservice

class MoniekD(Microservice):
    def __init__(self):
        super().__init__()
        moniek_pb2_grpc.add_MoniekServicer_to_server(Moniek(), self.server)
        self.start(settings.MONIEK_SOCKET)

if __name__ == '__main__':
    MoniekD()
