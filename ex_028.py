from random import random,randint,randrange

print("Pense em um numero entre 0 e 5:")
num_usuario = int(input("Digite seu numero escolhido"))
num_hard = randint(0, 5)
print("Processando ...")
if num_usuario==num_hard:
    print("Boa voce adivinhou o valor")
else:
    print('Tente outra vez o numero e {}'.format(num_hard))