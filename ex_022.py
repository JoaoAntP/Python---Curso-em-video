#from itertools import count
#rom posixpath import split

#nome = str(input("Digite seu nome pfv :")).strip()
#print(nome.upper())
#print(nome.lower())
#print("Seu nome tem {} numero de letras".format(len(nome)-(nome.count(' ')))) #
#print("Seu primeiro nome tem {} nmr de letras".format(nome.find(' ')))#

nome = str(input("Digite seu nome :")).strip()
print('seu nome em Maiusculo e {}'.format(nome.upper()))
print('seu nome em Maiusculo e {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome)-(nome.count(' '))))
print('Seu Primeiro nome e {}'.format(nome.find(' ')))