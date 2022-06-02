# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import corgi_pb2 as corgi__pb2


class RpcCorgiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayWoof = channel.unary_unary(
                '/packageOfCorgis.RpcCorgi/SayWoof',
                request_serializer=corgi__pb2.CorgiRequest.SerializeToString,
                response_deserializer=corgi__pb2.WoofReply.FromString,
                )


class RpcCorgiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayWoof(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcCorgiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayWoof': grpc.unary_unary_rpc_method_handler(
                    servicer.SayWoof,
                    request_deserializer=corgi__pb2.CorgiRequest.FromString,
                    response_serializer=corgi__pb2.WoofReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'packageOfCorgis.RpcCorgi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RpcCorgi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayWoof(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/packageOfCorgis.RpcCorgi/SayWoof',
            corgi__pb2.CorgiRequest.SerializeToString,
            corgi__pb2.WoofReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
