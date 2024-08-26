#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Digite o raio do circulo. Ex 9: "))
pi = float (3.14)
calc  = pi * (raio**2)

print("O valor do raio é de {}".format(calc))