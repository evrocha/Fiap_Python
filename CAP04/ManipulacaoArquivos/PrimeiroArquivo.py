    # escrevendo no arquivo
# with open("primeiro_arquivo.html", "a") as arquivo:
#     arquivo.write("<h1> BBBBBBBBBBBB </h1>")

    # lendo o arquivo tod0
# with open("primeiro_arquivo.html", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)
folha = ""
with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        folha += linha
        print(linha)
    if "xiiiiiiiiiiiiiiiiii" in folha:
        print('-----------BU-------------')
    # else:
    #     print("Roda dnv")