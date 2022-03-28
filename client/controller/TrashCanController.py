class TrashCanController:
    def __init__(self,api):
        self.client = ""
        self.api = ""

    def make_request(self,route,message,api):
        self.api = api
        if route == "/colocar-lixo":
            return self.put_trash_trash_can(message)
        elif route == "/get-dados-lixeira":
            return self.get_data_trash_can(message)
        elif route == "/bloquear-lixeira":
            return self.set_status_trash_can(message)
        else:
            return
    
    def put_trash_trash_can(self,message):
        return
    
    def set_status_trash_can(self,message):
        return
    
    def get_data_trash_can(self,message):
        return
    
    def get_trash_can(self,message):
        return
    
    def empty_trash_can(self,message):
        return