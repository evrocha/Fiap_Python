from socket import *
server = "127.0.0.1"#localhost
porta = 43210
#                   tipo de identificaao que o servir tera / oq peermite trabalhar ocm o tcp protocol
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server, porta))
obj_socket.listen(2) # qtd max de clints

print("aguardando cliente")

while True:
    con,cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print(f"recebemos {msg_recebida}")
        msg_enviada = b'Ola cliente'
        con.send(msg_enviada)
        break
    con.close()