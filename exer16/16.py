#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
metros2 = int(input("Quantos metros quadrados será pintado: "))
calc = metros2 / 3
qtd_latas = calc / 18
valor = qtd_latas * 80
print("Você deverá comprar {} no valor de {}".format(qtd_latas, valor))
