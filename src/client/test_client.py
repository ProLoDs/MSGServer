'''
Created on 21.04.2017

@author: pro
'''

import grpc
import gen.networking.service_pb2_grpc as service

def connect():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service.MessengerAPIServiceStub(channel)
    req = request.Request()
    req.register_request.name = "test1"
    req.register_request.publickey = b"asd"
    request.RegisterRequest
    #req.register_request.add() 
    req.request_type = request.RequestType.Value("Register")

    response = stub.register(req)
    print response.error
    print response.register_response.uniqueID

if __name__ == '__main__':
    connect()