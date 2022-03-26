from util.Connection_server import Connection_server

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
    def decode_message(self):
        return  
    
    # Método responsável por redirecionar a solicitação para o método responsável.
    def request_controller(self):
        return


    ########################  ENDPOINTS DA API #########################

    #Lixeira
    def put_trash_trash_can(self):
        return
    
    def set_status_trash_can(self):
        return
    
    def get_data_trash_can(self):
        return 

    #Caminhao


    #Estação
    def put_trash_station(self,trash):
        return

    def get_status_station(self):
        return

    def leave_trash_staion(self):
        return
    #admistrador


