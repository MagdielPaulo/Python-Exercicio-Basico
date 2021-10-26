#### Desafio faça um programa que leia um ano qualquer e mostrese ele é bissexto ####

from datetime import date

ano = int(input('Em qual ano que você está ? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year                               #====> Método de uma biblioteca chamada "datetime" que serve pra mostar o ano atual entre outras coisa.
if (ano%4) == 0 and (ano%100) !=0 or (ano%400) == 0:      #====> Tem que ser divisivel por 4 "e" também não pode ser diferente de 0 "ou" o ano
    print('Sim seu ano de {} é bissexto'.format(ano))     # ser divisivel por 400. %=divisivel(resto) !=(diferente)
else: 
    print('Não é bissexto o ano de {}'.format(ano))