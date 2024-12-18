from os.path import split

valor = int(input("Digite seu nome pfv :"))
u =      valor  // 1 % 10
d =     valor    // 10 % 10
c =  valor       // 100 % 10
m =    valor     // 1000 % 10
format(valor)
print("O valor de Unidad e {}".format(u))
print("O valor de Dezena e {}".format(d))
print("O valor de centen e {}".format(c))
print("O valor de Milhar e {}".format(m))


