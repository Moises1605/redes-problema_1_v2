class ManagerInterfaceController:
    def __init__(self):
        pass

    def make_request(self,route,message,api):
        self.api = api
        if route == "/bloquear-lixeira":
            return self.block_trash_can(message)
        elif route == "/mudar-ordem-lixeira":
            return self.set_collection_order_trash_can(message)
        elif route == "/get-proxima-lixeira":
            return self.get_next_trash_can(message)
        else:
            return
    
    def block_trash_can(self,message):
        return
    
    def set_collection_order_trash_can(self,message):
        return
    
    def get_next_trash_can(self,message):
        return