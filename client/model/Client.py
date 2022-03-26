from util.Connection_client import Connection_client

class client:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.connection = ""

    def connect(self):
        self.connection = Connection_client(self.host,self.port)