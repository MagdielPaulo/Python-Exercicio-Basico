#### Desafio, escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint                                           #### Para sortear os números e fazer como se o computador fosse pensar
from time import sleep                                               #===> Uma biblioteca diferente time ou melhor tempo para controlar o tempo

computador = randint(0,5)                                            #====> randint para sortear os num de 0 a 5.

print('-=--=--'*10)                                                  # Nada mais do que um toque de beleza no programa
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('-=--=--'*10)

jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)                                                            #====> Sleep método para fazer o comando anterior dormir um pouco antes de exe.

if jogador == computador:                                           # E as condições !!!
    print('OH NÃO ! Como você advinhou que eu escolhi o número {} ? PARABÉNS !!!'.format(computador))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador,jogador))
