n=str(input("Qual seu nome ? :"))
nome = n.split()
print("Seu primeiro nome e {}".format(nome[0]))
print("Seu ultimo nome e {}".format(nome[len(nome)-1]))