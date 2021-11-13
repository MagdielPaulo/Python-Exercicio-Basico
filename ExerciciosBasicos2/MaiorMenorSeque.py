#### Um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 5):
    kg = float(input('Peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
       
        if kg < menor:
            menor = kg

print('Pesoa com maior peso foi {}kg!'.format(maior))
print('Pessoa com menor peso foi {}kg!'.format(menor))