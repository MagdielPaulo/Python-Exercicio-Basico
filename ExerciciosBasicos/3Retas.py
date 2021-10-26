####  Desafio, desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

from time import sleep

print('-=-=-'*10)
print('Analisador de Triângulos !')
print('-=-=-'*10)

a = float(input('Diga o primeiro segmento: '))
b = float(input('Diga o segundo segmento: '))
c = float(input('Diga o terceiro segmento: '))
print('PROCESSANDO...')
sleep(2)

if a+b>c and b+c>a and a+c>b :
    print('Sim pode formar um triângulo !!!')
else:
    print('Infelizmente não pode formar um triângulo !')