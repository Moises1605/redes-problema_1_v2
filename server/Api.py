from util.Connection_server import Connection_server
from client.controller.ClientController import ClientController
from client.controller.StationController import StationController
from client.controller.TrashCanController import TrashCanController
from client.controller.TruckController import TruckController
from client.controller.ManagerInterfaceController import ManagerInterfaceController

import json
class Api:
    def __init__(self,host,port):
        self.port = port
        self.host = host
        self.connection = ""
    
    # Método responsável por iniciar a conexão do servidor
    def connect(self):
        self.connection = Connection_server(self.host,self.port)
        return self.connection 

    # Método responsável por decodificar a mensagem recebida pela api
    def decode_message(self,data,api):

        message = json.loads(data)
        client_type = message['header']['tipo_cliente']
        route = message["header"]["rota"]
        result = ""
        client_controller = ""

        if client_type == "1":
            client_controller = TrashCanController()
            result = client_controller.make_request(route,message,api)
            return
        elif client_type == "2":
            client_controller = TruckController()
            return
        elif client_type == "3":
            client_controller = StationController()
            return
        elif client_type == "4":
            client_controller = ManagerInterfaceController()
            return

        return  
    
    # Método responsável por redirecionar a solicitação para o método responsável.
    def request_controller(self):
        return

    def get_client(self,client_type,client_id):
        
        return

    ########################  ENDPOINTS DA API #########################

    #Caminhao


    #Estação
    def put_trash_station(self,trash):
        return

    def get_status_station(self):
        return

    def leave_trash_staion(self):
        return
    #admistrador


