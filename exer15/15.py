#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#Salário bruto
salario = float(input("Quanto você ganha por hora: "))
horas = float(input("E quantas horas por semana você trabalha: "))
calc_mes = salario * (horas * 30) 

#Valor pago ao INSS
calc_inss = (calc_mes / 100) * 8

#Valor pago ao sindicato
calc_sindi = (calc_mes / 100) * 5

#Salário líquido
calc_liq = calc_mes - calc_inss - calc_sindi
print("O seu salário bruto é de {} com o desconto do INSS é de {}, e com o desconto do Sindicato é {}. No final seu salário é {}".format(calc_mes, calc_inss, calc_sindi, calc_liq))