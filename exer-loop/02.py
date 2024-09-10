
faixa_0_15 = 0
faixa_16_30 = 0
faixa_31_45 = 0
faixa_46_60 = 0
faixa_mais_60 = 0
i = 1

while(i < 50):
    idade = int(input("Digite as idades: "))
    
    if idade <= 15:
        faixa_0_15 += 1
    elif idade <= 30:
        faixa_16_30 += 1
    elif idade <= 45:
        faixa_31_45 += 1
    elif idade <= 60:
        faixa_46_60 += 1
    else:
        faixa_mais_60 += 1

    i+=1

total_pessoas = 50

percentual_0_15 = (faixa_0_15 / total_pessoas) * 100
percentual_16_30 = (faixa_16_30 / total_pessoas) * 100
percentual_31_45 = (faixa_31_45 / total_pessoas) * 100
percentual_46_60 = (faixa_46_60 / total_pessoas) * 100
percentual_mais_60 = (faixa_mais_60 / total_pessoas) * 100

print("Percentual de pessoas de 0 a 15 anos: {}%".format(percentual_0_15))
print("Percentual de pessoas de 16 a 30 anos: {}%".format(percentual_16_30))
print("Percentual de pessoas de 31 a 45 anos: {}%".format(percentual_31_45))
print("Percentual de pessoas de 46 a 60 anos: {}%".format(percentual_46_60))
print("Percentual de pessoas com mais de 60 anos: {}%".format(percentual_mais_60))
