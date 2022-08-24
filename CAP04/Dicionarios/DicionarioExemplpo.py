def perguntar():
    return str(input("O que deseja fazer?\n" +
                 "<1> - Inserir usuário\n" +
                 "<2> - Pesquisar usuário\n" +
                 "<3> - Excluir usuário\n" +
                 "<4> - Listar usuário: ").upper())

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))


def inserir(dicionario):
    dicionario[input("Digite o login: ".upper())] = [input("Nome: ").upper(),
                                                     input("Última data de acesso: "),
                                                     input("Estaçãoa acessada: ").upper()]
    salvar(dicionario)
