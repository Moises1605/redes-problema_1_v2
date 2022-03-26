from util.Connection_server import Connection_server
from util.Connection_client import Connection_client
from server.Api import Api

if __name__ == "__main__":
    # Inicia o servidor e começa a "escutar" os clientes
    api = Api("10.0.0.130",12345)
    connection = api.connect()
    connection.connect()
    connection.receive()

    # connection = Connection_client()
    # connection.connect()
    # connection.receive()