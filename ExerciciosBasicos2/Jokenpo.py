#### Um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint

print('''\033[31mSuas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA\033[31m''')

jogador = int(input('\033[32mQual é a sua jogada?\033[32m'))
print('\033[33mJO\033[33m')
sleep(2)
print('\033[34mKEN\033[34m')
sleep(2)
print('\033[35mPO!!!\033[35m')
sleep(2)

print('\033[36m-=\033[36m' * 11)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('O computador jogou: {}'.format(itens[computador]))
print('O jogador jogou: {}'.format(itens[jogador]))

print('-=' * 11)

if computador == 0: ##==> PEDRA
    
    if jogador   == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: ##==> PAPEL
    
    if jogador   == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: ##==> TESOURA
    
    if jogador   == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')