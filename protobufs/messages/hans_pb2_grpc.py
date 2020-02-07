# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protobufs.messages import hans_pb2 as protobufs_dot_messages_dot_hans__pb2


class HansStub(object):
  """Hans talks directly to Mailman.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMembership = channel.unary_unary(
        '/Hans/GetMembership',
        request_serializer=protobufs_dot_messages_dot_hans__pb2.GetMembershipReq.SerializeToString,
        response_deserializer=protobufs_dot_messages_dot_hans__pb2.GetMembershipResp.FromString,
        )
    self.ApplyChanges = channel.unary_unary(
        '/Hans/ApplyChanges',
        request_serializer=protobufs_dot_messages_dot_hans__pb2.ApplyChangesReq.SerializeToString,
        response_deserializer=protobufs_dot_messages_dot_hans__pb2.ApplyChangesResp.FromString,
        )


class HansServicer(object):
  """Hans talks directly to Mailman.
  """

  def GetMembership(self, request, context):
    """Get all lists with all memberships.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplyChanges(self, request, context):
    """Apply changes: create new lists for the 'create' property, and add/remove
    members of a list with the add/remove properties.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HansServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMembership': grpc.unary_unary_rpc_method_handler(
          servicer.GetMembership,
          request_deserializer=protobufs_dot_messages_dot_hans__pb2.GetMembershipReq.FromString,
          response_serializer=protobufs_dot_messages_dot_hans__pb2.GetMembershipResp.SerializeToString,
      ),
      'ApplyChanges': grpc.unary_unary_rpc_method_handler(
          servicer.ApplyChanges,
          request_deserializer=protobufs_dot_messages_dot_hans__pb2.ApplyChangesReq.FromString,
          response_serializer=protobufs_dot_messages_dot_hans__pb2.ApplyChangesResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Hans', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))