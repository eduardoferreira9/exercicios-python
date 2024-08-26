#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celcius = float(input("Qual a temperatura enm Celsius: "))
calc = (celsius * 9/5) + 32
print("A temperatura em Celcius {}, equivale a {} em graus Fahrenheint.".format(celcius, calc))