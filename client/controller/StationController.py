class StationController:
    def __init__(self):
        pass

    def make_request(self,route,message,api):
        self.api = api
        if route == "/get-capacidade":
            return self.get_current_capacity(message)
        elif route == "/get-capaciade-total":
            return self.get_capacity_total(message)
        elif route == "/colocar-lixo":
            return self.put_trash(message)
        elif route == "/esvaziar-estacao":
            return self.empty_station(message)
        else:
            return
    
    def get_current_capacity(self,message):
        return
    
    def get_capacity_total(self,message):
        return
    
    def put_trash(self,message):
        return
    
    def empty_station(self,message):
        return