'''
Created on 20.04.2017

@author: pro
'''
import gen.networking.service_pb2 as service
import gen.networking.responses_pb2 as response
import gen.networking.service_pb2_grpc as service_pb2_grpc
import gen.networking.data_pb2 as data
import concurrent.futures as futures
import grpc
import time


from database.db_interface import register_db ,add_message,get_user_by_id
from database.model import create_database, create_session, test
#DEFINES
_ONE_DAY_IN_SECONDS = 60*60 * 24


class MessengerServicer(service_pb2_grpc.MessengerAPIServiceServicer):
    def __init__(self,engine):
        self.session = create_session(engine)
    def register(self, request, context):
        print "Register called!"
        unique_id = register_db(self.session, request.name, request.publickey)
        res = response.Response()
        res.error = data.ErrorType.Value("SUCCESS")
        res.registerResponse.uniqueID = unique_id
        return res
    def sendMessage(self, request, context):

        add_message(self.session, request.message)
        res = response.Response()
        res.error = data.ErrorType.Value('SUCCESS') 
        
        return res

    def findUserByName(self, request, context):
        #user = get_user_by_id(self.session, id)
        pass
    def getUserInfo(self, request, context):
        user = get_user_by_id(self.session,request.uniqueID)
        resp =  response.Response()
        resp.error = data.SUCCESS
        resp.getUserInfoResponse.user.uniqueID = user.user_id
        resp.getUserInfoResponse.user.name = user.name
        resp.getUserInfoResponse.user.publicKey = user.public_key
        return resp
    def getMessages(self, request, context):
        request.uniqueID
        request.timestamp
        request.signature
        user = get_user_by_id(self.session, request.uniqueID)
        resp = response.Response()
        resp.error = data.SUCCESS
        for msg in user.messages:
            proto_msg = resp.getMessagesResponse.messages.add()
            proto_msg.origin = msg.origin
            proto_msg.destination = msg.destination
            proto_msg.key = msg.key
            proto_msg.iv = msg.iv
            proto_msg.message = msg.content
            proto_msg.type = msg.type
            proto_msg.timestamp = msg.timestamp
            proto_msg.publickey = msg.publickey
            proto_msg.signature = msg.signature
        return resp
def serve():
    engine = create_database("main.db")
    #test(s)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MessengerAPIServiceServicer_to_server(MessengerServicer(engine), server)
    server.add_insecure_port('0.0.0.0:8890')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)




if __name__ == '__main__':
    print "Starting Server"
    serve()
    print "Stop server?"
    
    
