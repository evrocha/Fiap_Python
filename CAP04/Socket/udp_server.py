from  socket import *
server = "127.0.0.1"#localhost
porta = 43210
# dgram = broadcast
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, porta))
print("Server is ready")

while True:
    dados, origem = obj_socket.recvfrom(6535)
    print("Origem............:", origem)
    print("Dados recebidos...:", dados.decode()) # decodifica byte->str
    resp = input("Digite a resposta")
    obj_socket.sendto(resp.encode(), origem)
obj_socket.close()