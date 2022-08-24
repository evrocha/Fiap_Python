import platform
import getpass
from datetime import datetime

# print("Nome maquina:........", platform.node())
# print("Arquitetura:.........", platform.architecture())
# print("Sistema Operacional:.", platform.system())
# print("Versão do SO:........", platform.release())
# print("Processador:........", platform.processor())
# print("Versao do python:........", platform.python_version())
#
# print(datetime.now())

usuario = (getpass.getuser())
senha = (getpass.getpass("Digite sua senha:..."))
i = 3
if usuario == "emanu" and senha == "1608":
    print("Acesso permitido")
else:
    while i <= 3 and i>0:
        print(f"voce ainda tem {i} chances")
        print("tente novamente: ")
        senha = (getpass.getpass("Digite sua senha:..."))
        i = i - 1
        print("Acesso negado")


