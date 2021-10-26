#### Como utilizar módulos em Python utilizando os comandos import e from/import no Python ####
#### Como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas ####


''' #### Primeira forma básica de importação com todas as funcionalidades da biblioteca ####

import math
num = int(input('Digite um número: '))
r = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num,r))'''



''' #### Segunda forma básica de importação com apenas umas das funcionalidades da biblioteca ####

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num,raiz))'''



''' #### Testando com outras bibliotecas #### 

import random
num = random.randint(1, 10)
print(num)'''


'''#### Testando importação extras separadmente ####


import emoji
print(emoji.emojize('Olá, Mundo :monkey:',use_aliases=(True)))'''
