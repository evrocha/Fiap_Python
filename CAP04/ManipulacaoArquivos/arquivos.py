base_dados = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        base_dados.append(registro.split(","))
print(base_dados)