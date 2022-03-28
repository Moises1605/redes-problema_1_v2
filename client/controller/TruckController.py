class TruckController:
    def __init__(self):
        pass

    def make_request(self,route,message,api):
        self.api = api
        if route == "/get-proxima-lixeira":
            return self.get_trash_can_current(message)
        else:
            return
    
    def set_list_trash_can(self):
        return
    
    def get_trash_can_current(self,message):
        return
    