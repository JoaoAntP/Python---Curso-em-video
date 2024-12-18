import random
a1 = str(input("Nome do Aluno(a)"))
a2 = str(input("Nome do Aluno(a)"))
a3 = str(input("Nome do Aluno(a)"))
a4 = str(input("Nome do Aluno(a)"))
lista_alu = [a1,a2,a3,a4]
aluno_selec = random.choice(lista_alu)
print("O Aluno selecionado foi {} ".format(aluno_selec))
