from socket import *

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    conex, cliente = obj_socket.accept()
    print("Conectado com : ", cliente)
    while True:
        msg_rescebida = str(conex.recv(1024))
        print("Recebemos: ", msg_rescebida)
        msg_enviada = b"Ola cliente"
        conex.send(msg_enviada)
        break
    conex.close()
