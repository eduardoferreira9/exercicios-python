#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input("Qual seu salário por hora? "))
horas = int(input("Quantas horas por semana você trabalha? "))
calc = ganho_hora * (horas * 30)
print("Seu salário por mês é de {}".format(calc))
