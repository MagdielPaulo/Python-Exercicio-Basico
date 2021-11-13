#### Um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

dataAtual = date.today().year
maior = 0
menor = 0
for c in range(1, 5):
    ano = int(input('{})Diga seu ano de nascimento: '.format(c)))
    idade = dataAtual - ano
    if idade >= 18:
        
        maior += 1
    
    else:
        menor += 1

print('Pessoas com maioridade foram apenas {}'.format(maior))
print('já as de menor idade foram apenas {}'.format(menor))    