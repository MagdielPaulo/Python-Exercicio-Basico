#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente
#desse ângulo.

import math

a = float(input('Diga um ângulo: °'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O valor do SENO de {} é: {:.2f}'.format(a,s))
print('O valor do COSSENO de {} é: {:.2f}'.format(a,c))
print('O valor da TANGENTE de {} é: {:.2f}'.format(a,t))