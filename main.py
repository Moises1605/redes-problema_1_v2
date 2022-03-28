from util.Connection_server import Connection_server
# from util.Connection_client import Connection_client
from server.Api import Api
import select, socket, sys 
from  queue import *

if __name__ == "__main__":
    # Inicia o servidor e começa a "escutar" os clientes
    api = Api("10.0.0.130",12345)
    connect_server = api.connect()
    server = connect_server.connect()
    inputs = [server]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs)
        for s in readable:
            connection, client_address = s.accept()
            # data =""
            print("Ouvindo endereço: ")
            print(client_address)
            data = connection.recv(1024)
            if data:
                # result = api.decode_message(data,api)
                # Decodifica a mensagens para saber o que deve ser feito
                connection.sendall(data)
                # message_queues[s].put(data)
                # if s not in outputs:
                #     outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]

    # connection = Connection_client()
    # connection.connect()
    # connection.receive()



#Estrutura da mensagem
#Header
#tipo de cliente (1-lixeira,2-Caminhão,3-estacao,4-Administrador)
#tipo de formatacao de texto (utf-8)
#rota para realizar requisicao
#tipo de requisicao
#host
#port
#Parte de dados
#(dados se tiver)