soma = 0

while True:
    num = int(input("Digite os números inteiros positivos: "))
    if num % 2 == 0:
         soma += num
    elif num < 0:
         break
print(soma)

