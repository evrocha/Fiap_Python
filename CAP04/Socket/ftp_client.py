from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usr=input("usuario: ")
senha=input("senha: ")

ftp.login(usr, senha)

print(f"diretorio atua de trabalho {ftp.pwd()}")

ftp.cwd('pub') # a lterando o dir

print("dir corrente: ", ftp.pwd())

print(ftp.retrlines('LIST'))   # lista os arquivos do dir
ftp .quit()