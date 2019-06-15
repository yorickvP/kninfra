from __future__ import absolute_import

import logging
import threading
import sdnotify

from django.conf import settings

from kn.utils.hans import moderation, sync



_ONE_DAY_IN_SECONDS = 60 * 60 * 24

from kn.rpc.util_pb2 import Success
from kn.rpc.rpc_pb2_grpc import HansServicer, add_HansServicer_to_server
from kn.rpc.rpc_pb2 import MailChanges
from google.protobuf.empty_pb2 import Empty
from kn.rpc import mail_pb2
            
class Hans(rpc_pb2_grpc.HansServicer):
    def maillist(self, request: MailChanges, context) -> Success:
        sync.apply_changes(request)
        return Success()
    
    def get_membership(self, request: Empty, context) -> mail_pb2.Membership:
        return mail_pb2.Membership(membership=sync.get_membership())
    
    def get_moderated_lists(self, request: Empty, context) -> mail_pb2.ModeratedLists:
        return mail_pb2.ModeratedLists(lists=moderation.get_lists())
    
    def set_moderation(self, request: mail_pb2.Moderation, context) -> Success:
        moderation.activate(request.name, request.moderated)
        return Success()
    
    def get_moderator_cookie(self, request: mail_pb2.List, context) -> mail_pb2.ModeratorCookie:
        return mail_pb2.ModeratorCookie(cookie=moderation.get_cookie(request.name))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    rpc_pb2_grpc.add_HansServicer_to_server(Hans(), server)
    server.add_insecure_port(settings.HANS_SOCKET)
    server.start()
    sdnotify.SystemdNotifier().notify("READY=1")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
# vim: et:sta:bs=2:sw=4:
