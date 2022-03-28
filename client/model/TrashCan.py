# Classe responsável por representar a entidade lixeira
from model.Client import client


class TrashCan(client): 

    def __intit__(self,capacity,released,latitude,longitude,identifier,port,host):
        super().__init__(host, port)
        self.capacity =  capacity
        self.released = released
        self.latitude = latitude
        self.latitude = longitude
        self.identifier = identifier
        self.capacity_total = 100

    # Método responsável por colocar lixo na lixeira
    def put_trash(self,value=3):
        capacity_temp = self.capacity + value

        if(capacity_temp <= self.capacity_total):
            self.capacity += value
            return bool("true")
        
        return bool("false")
    
    # Método responsável por mudar o status da lixeira (Liberada/bloqueada)
    def set_status(self,status):
        self.released = status
        
    
