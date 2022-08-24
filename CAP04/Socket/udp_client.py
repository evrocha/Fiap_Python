from  socket import *
server = "127.0.0.1"#localhost
porta = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, porta))

saida = ""

while saida!="X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(), (server, porta))
    dados, origem = obj_socket.recvfrom(65535)
    print(("resposta do servidor "), dados.decode())
    saida = input("<X> p sair").upper()
obj_socket.close()