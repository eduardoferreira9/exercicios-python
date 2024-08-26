numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = float(input("Digite um número real: "))
#O produto do dobro do primeiro com metade do segundo .
calc1 = numero1 * 2 
calc2 = numero2 / 2
calc3 = calc1 * calc2

#A soma do triplo do primeiro com o terceiro.
calc4 =  numero1 + numero3
calc5 = calc4 * 3
calc6 = calc1 + calc5

#O terceiro elevado ao cubo.
calc7 = numero3**3

print("O produto do dobro do primeiro com metade do segundo é {}, a soma do triplo do primeiro com o terceiro número é {} e o terceiro número elevado ao cubo é {}".format(calc3, calc6, calc7))