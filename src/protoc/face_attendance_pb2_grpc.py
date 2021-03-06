# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protoc import face_attendance_pb2 as face__attendance__pb2


class DetectFaceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DoDetectFace = channel.unary_unary(
        '/face_attendance.DetectFace/DoDetectFace',
        request_serializer=face__attendance__pb2.DetectFaceRequest.SerializeToString,
        response_deserializer=face__attendance__pb2.DetectFaceResponse.FromString,
        )


class DetectFaceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DoDetectFace(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DetectFaceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DoDetectFace': grpc.unary_unary_rpc_method_handler(
          servicer.DoDetectFace,
          request_deserializer=face__attendance__pb2.DetectFaceRequest.FromString,
          response_serializer=face__attendance__pb2.DetectFaceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'face_attendance.DetectFace', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
