#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado1 = int(input("Digite o 1 lado do quadrado em metros: "))
lado2 = int(input("Digite o 2 lado do quadrado em metros: "))
calc = (lado1 ** lado2) * 2
print("O dobro da área do quadrado é {} m²".format(calc))