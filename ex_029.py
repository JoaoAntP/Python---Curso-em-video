vel_carro= int(input('Qual a velocidade do carro :'))
vel_max = 80
multa = (vel_carro - 80) * 7
if  vel_carro > multa:
    print("Seu carro esta dentro da velocidade pode passar")
else:
    print("Multado, Voce ultrapassou a velocidade e sua Multa e {}".format(multa))