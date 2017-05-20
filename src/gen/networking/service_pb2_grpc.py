# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import networking.requests.messages_pb2 as networking_dot_requests_dot_messages__pb2
import networking.responses_pb2 as networking_dot_responses__pb2
import service_pb2 as service__pb2


class MessengerAPIServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.register = channel.unary_unary(
        '/networking.service.MessengerAPIService/register',
        request_serializer=networking_dot_requests_dot_messages__pb2.RegisterRequest.SerializeToString,
        response_deserializer=networking_dot_responses__pb2.Response.FromString,
        )
    self.sendMessage = channel.unary_unary(
        '/networking.service.MessengerAPIService/sendMessage',
        request_serializer=networking_dot_requests_dot_messages__pb2.SendMessageRequest.SerializeToString,
        response_deserializer=networking_dot_responses__pb2.Response.FromString,
        )
    self.getMessages = channel.unary_unary(
        '/networking.service.MessengerAPIService/getMessages',
        request_serializer=networking_dot_requests_dot_messages__pb2.GetMessagesRequest.SerializeToString,
        response_deserializer=networking_dot_responses__pb2.Response.FromString,
        )
    self.getUserInfo = channel.unary_unary(
        '/networking.service.MessengerAPIService/getUserInfo',
        request_serializer=networking_dot_requests_dot_messages__pb2.GetUserInfoRequest.SerializeToString,
        response_deserializer=networking_dot_responses__pb2.Response.FromString,
        )
    self.findUserByName = channel.unary_unary(
        '/networking.service.MessengerAPIService/findUserByName',
        request_serializer=networking_dot_requests_dot_messages__pb2.FindUserByNameRequest.SerializeToString,
        response_deserializer=networking_dot_responses__pb2.Response.FromString,
        )
    self.ping = channel.unary_unary(
        '/networking.service.MessengerAPIService/ping',
        request_serializer=service__pb2.pingMessage.SerializeToString,
        response_deserializer=service__pb2.pongMessage.FromString,
        )


class MessengerAPIServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sendMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUserInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findUserByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessengerAPIServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'register': grpc.unary_unary_rpc_method_handler(
          servicer.register,
          request_deserializer=networking_dot_requests_dot_messages__pb2.RegisterRequest.FromString,
          response_serializer=networking_dot_responses__pb2.Response.SerializeToString,
      ),
      'sendMessage': grpc.unary_unary_rpc_method_handler(
          servicer.sendMessage,
          request_deserializer=networking_dot_requests_dot_messages__pb2.SendMessageRequest.FromString,
          response_serializer=networking_dot_responses__pb2.Response.SerializeToString,
      ),
      'getMessages': grpc.unary_unary_rpc_method_handler(
          servicer.getMessages,
          request_deserializer=networking_dot_requests_dot_messages__pb2.GetMessagesRequest.FromString,
          response_serializer=networking_dot_responses__pb2.Response.SerializeToString,
      ),
      'getUserInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getUserInfo,
          request_deserializer=networking_dot_requests_dot_messages__pb2.GetUserInfoRequest.FromString,
          response_serializer=networking_dot_responses__pb2.Response.SerializeToString,
      ),
      'findUserByName': grpc.unary_unary_rpc_method_handler(
          servicer.findUserByName,
          request_deserializer=networking_dot_requests_dot_messages__pb2.FindUserByNameRequest.FromString,
          response_serializer=networking_dot_responses__pb2.Response.SerializeToString,
      ),
      'ping': grpc.unary_unary_rpc_method_handler(
          servicer.ping,
          request_deserializer=service__pb2.pingMessage.FromString,
          response_serializer=service__pb2.pongMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'networking.service.MessengerAPIService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))