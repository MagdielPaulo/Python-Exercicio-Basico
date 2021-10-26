## Exemplo 1

'''print('\033[1;36;45mOlá, Mundo\33[m')'''          #===> Caso eu queira apenas nas palavras especificas só colocar novamente a barra \33[m'

## Exemplo 2

'''a = 4
b = 5
print('Os valores são \033[1;32m{}\033[m e \033[1;31m{}\033[m'.format(a,b))'''

## Exemplo 3

'''nome = 'Magdiel'
print('Muito prazer {}{}{}, seja bem vind0 !'.format('\033[1;36;32m',nome,'\033[m'))'''    #====> No format pra ficar mais organizado.

## Exemplo 4

'''nome = 'Magdiel'                                   
cores = {'limpa':'\033[m',
        'azul' :'\033[34m',
        'amarelo':'\033[33m',
        'pretobranco':'\033[7;30m'}
print('Muito prazer {}{}{}, seja bem vind0 !'.format(cores['azul'], nome, cores['limpa']))'''






