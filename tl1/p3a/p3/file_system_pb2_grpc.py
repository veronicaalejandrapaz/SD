# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import file_system_pb2 as file__system__pb2


class FSStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFiles = channel.unary_unary(
                '/FS/ListFiles',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.PathFiles.FromString,
                )
        self.OpenFiles = channel.unary_unary(
                '/FS/OpenFiles',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.Booleano.FromString,
                )
        self.CloseFiles = channel.unary_unary(
                '/FS/CloseFiles',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.Booleano.FromString,
                )
        self.ReadFiles = channel.unary_unary(
                '/FS/ReadFiles',
                request_serializer=file__system__pb2.Path.SerializeToString,
                response_deserializer=file__system__pb2.Path.FromString,
                )


class FSServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FSServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.PathFiles.SerializeToString,
            ),
            'OpenFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenFiles,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.Booleano.SerializeToString,
            ),
            'CloseFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseFiles,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.Booleano.SerializeToString,
            ),
            'ReadFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFiles,
                    request_deserializer=file__system__pb2.Path.FromString,
                    response_serializer=file__system__pb2.Path.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FS', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FS(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/ListFiles',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.PathFiles.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/OpenFiles',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.Booleano.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/CloseFiles',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.Booleano.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FS/ReadFiles',
            file__system__pb2.Path.SerializeToString,
            file__system__pb2.Path.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)