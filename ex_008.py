print("Nesse program iremos fazer a conversão de valores de cm pra metro e de metro para centimentros: ")
valor_cm= float(input("Digite o Valor de valor em centimetros :"))
valor_m= float(input("Digite o valor em metros: "))
print("Vou te retornar o valor de duas formas se voce digitou em cm vou te dar em metro e caso tenha dando em metro em centimetros: ")
valor_CmpM =  valor_cm / 100
valor_MpCm =  valor_m * 100
valor_1MM = valor_cm / 100
valor_2MM = valor_m/1000
print(" se voce me me deu o valor em cm para converter para M esse e o resultado e {}M ,Caso valor tenha sido em M para cm esse e o Valor {}cm ".format(valor_CmpM,valor_MpCm))
print("Aqui vai um Bonus seu valor e Milimetros e {} Cm para MM, e de {} de M para MM".format(valor_1MM,valor_2MM))
