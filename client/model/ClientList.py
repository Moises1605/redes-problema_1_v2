class ClientList():

    def __init__(self,list_clients):
        self.list_clients = "";
    

    def get_client(self,client_type,client_id):
        client_result = ""
        for client in self.list_clients:
            if client.client_type == client_type and client.id == client_id:
                client_result = client
                break
        
        return client_result
    
    def get_all_client(self):
        return self.list_clients