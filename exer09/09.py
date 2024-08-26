#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
fahren = float(input("Qual a temperatura enm Fahrenheit: "))
calc = 5 * ((fahren - 32) / 9)
print("A temperatura em Fahrenheit {}, equivale a {} em graus Celsius.".format(fahren, calc))