# Classe responsável por representar a entidade lixeira
from model.Client import client


class ManagerInterface(client): 

    def __intit__(self,capacity,released,latitude,longitude,identifier,port,host):
        super().__init__(host, port)
        self.list_trash_can =  ""
        self.identifier = identifier
        self.collection_order_trash_can = ""