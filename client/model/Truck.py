# Classe responsável por representar a entidade lixeira
from model.Client import client


class Truck(client): 

    def __intit__(self,identifier,port,host):
        super().__init__(host, port)
        self.current_trash_can =  ""
        self.trash_can_list = ""
        self.identifier = identifier
        self.capacity_total = 100
        self.current_capacity = ""
    

