#Escreva um algoritmo que calcule e imprima o somatório dos números pares existentes entre 100 e 500.
i = 100
soma = 0
while(i <= 500):
    soma += i
    i += 2
print(soma)