#### Dasafio, crie um programa que leia um número Real qualquer pelo teclado e mostre
#### na tela a sua porção inteira.  Ex: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.

''' #### Primiera forma ####

import math
num = float(input('Digite um número: '))
i = math.trunc(num)
print('O número {} tem a sua porção inteira {}'.format(num,i))'''

''' #### Segunda forma ####

from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a sua porção inteira {}'.format(num, trunc(num)))'''


''' #### Terceira forma e sem importação ####

num = float(input('Digite um número: '))
print('O número {} tem a sua porção inteira {}'.format(num, int(num)))'''



