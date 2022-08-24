from socket import *
server = "127.0.0.1"#localhost
porta = 43210

msg = bytes(input("Digit algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((server, porta))
obj_socket.send(msg)
resp = obj_socket.recv(1024)
print("Recebemos: ", resp)
obj_socket.close()