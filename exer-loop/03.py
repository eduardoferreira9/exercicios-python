i = int(input("Digite o primeiro número: "))
h = int(input("Digite o segundo número: "))
soma = 0 

if i < h:
    menor = i
    maior = h 
else: 
    maior = h
    menor = i

while(i <= h):
    soma += i
    i += 1
print(soma)