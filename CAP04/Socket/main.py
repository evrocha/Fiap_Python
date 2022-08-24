import socket
resp = 's'

while resp=="s":
    url = input("digite uma url:")
    ip =socket.gethostbyname(url)
    print("O ip refernte a url informada é: ", ip)
    resp = input(("quer continuar? <s>"))