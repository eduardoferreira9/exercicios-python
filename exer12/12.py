#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Digite aqui sua altura em cm: "))
altura_cm = altura / 100
calc = (72.7*altura_cm) - 58
print("O seu peso ideal é {}".format(calc))