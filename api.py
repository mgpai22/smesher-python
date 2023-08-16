import grpc
from types_proto import activation_pb2_grpc as atx_pb2_grpc
import binascii
from google.protobuf.empty_pb2 import Empty


class ActivationClient(object):
    def __init__(self, ip_address_with_port):
        self.channel = grpc.insecure_channel(ip_address_with_port)
        self.stub = atx_pb2_grpc.ActivationServiceStub(self.channel)

    def get_highest(self):
        request = Empty()
        response = self.stub.Highest(request)
        return response

    def get_highest_atx_id(self):
        atx_id = self.get_highest().atx.id.id
        return binascii.hexlify(atx_id).decode()