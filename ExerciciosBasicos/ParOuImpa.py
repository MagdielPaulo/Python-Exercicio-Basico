#### Desafio, crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar ####

num = int(input('Digite um número: '))
if (num%2) == 0:
    
    print('Seu número {} é PAR !'.format(num))

else:
    
    print('Seu número {} é ÍMPAR !'.format(num))