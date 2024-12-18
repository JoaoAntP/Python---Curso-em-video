from select import select

p = str(input("Diga Algo :")).upper()
print("A letra A aparece {} vezes".format(p.count('A')))
print("A letra A aparece pela primeira vez {} vezes".format(p.find('A')+1))
print("A letra A aparece pela ultima vez {} vezes".format(p.rfind('A')+1))
# pega o resultado de result_list indentificar a posição dentro da lista onde aparece pela primeira vez e jpgar o resulta olha dentro da ista dnv e jogar a ultima posição