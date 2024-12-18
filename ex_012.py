print("nesse programa calcularemos o seu reajuste salarial ! ")
salar_ini= int(input("Digite o valor do seu salario inicial : "))
ajuste_salar= int(input("Digite o o valor de reajuste ex: 10, 20, 40: "))
var_salar_pctg = (salar_ini/100) * ajuste_salar
var_salar_atualiz = var_salar_pctg +salar_ini
print("O valor do reajuste e de {}".format (var_salar_atualiz))