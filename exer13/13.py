#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

selecionar = (input("Você é homem ou mulher? "))
if selecionar == "homem":
    altura = float(input("Digite aqui sua altura em cm: "))
    altura_cm = altura / 100
    calc = (72.7*altura_cm) - 58
    print("O seu peso ideal é {}".format(calc))
elif selecionar == "mulher":
    altura = float(input("Digite aqui sua altura em cm: "))
    altura_cm = altura / 100
    calc = (62.1*altura_cm) - 44.7
    print("O seu peso ideal é {}".format(calc))
else:
    print("Selecione apenas umas das duas opções!")