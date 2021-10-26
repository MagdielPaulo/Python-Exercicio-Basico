## Exemplo 1

'''print('\033[1;36;45mOlá, Mundo\33[m')'''          #===> Caso eu queira apenas nas placras só colocar npvamente a barra \33[m'

## Exemplo 2

'''a = 4
b = 5
print('Os valores são \033[1;32m{}\033[m e \033[1;31m{}\033[m'.format(a,b))'''

## Exemplo 3

'''nome = 'Magdiel'
print('Muito prazer {}{}{}, seja bem vind0 !'.format('\033[1;36;32m',nome,'\033[m'))'''    #====> NO format pra ficar mais organizado.

## Exemplo 4

'''nome = 'Magdiel'                                   #====> Essa coleção que é um dicionário que é um tema mais pra frente 
cores = {'limpa':'\033[m',
        'azul' :'\033[34m',
        'amarelo':'\033[33m',
        'pretobranco':'\033[7;30m'}
print('Muito prazer {}{}{}, seja bem vind0 !'.format(cores['azul'], nome, cores['limpa']))'''






