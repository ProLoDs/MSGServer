'''
Created on 29.03.2017

@author: pro
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testImports(self):
        pass
    def testMessageCreate(self):
        from gen.networking import requests_pb2 as Requests
        from gen.networking.requests import messages_pb2 as Messages
        print Requests.RequestType.items()
        testmsg =  Messages.test()
        testrequest = Requests.Request
        testrequest.request_type = Requests.TEST
        testrequest.message = testmsg.SerializeToString()
        #pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()