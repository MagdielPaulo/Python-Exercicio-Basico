#### Faça um programa que leia o comprimeto do cateto oposto e do cateto adjacente de um triângulo retângulo,
#### calcule a mostra o comprimento da hipotenusa.

''' ##### Primeira forma #####

import math
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca,)
print('O comprimento da hipotenusa é: {:.2f}'.format(hi))'''

''' ##### Segunda forma #####

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hi))'''