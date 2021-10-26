#### Desafio, faça um programa que leia três números e mostre qual é o maior e qual é o menor. ####


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número '))

# O valor Menor !!

if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c

print('O valor menor é: {}'.format(menor))

# O valor maior

if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O valor maior é: {}'.format(maior))
