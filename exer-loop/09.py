import random
numero = random.randint(1, 100)

while True:
    num = int(input("Digite o número que você acha que o computador escolheu: "))
    if num == numero:
        print("Você acertou!")
        break
    else: 
        print("Você errou, mas ainda pode tentar.")