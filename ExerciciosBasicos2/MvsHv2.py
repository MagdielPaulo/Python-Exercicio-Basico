#### o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print('Sou sua maquina... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi ? ')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Hummm, Oxe mais um pouco!')
        if jogador > computador:
            print('Hmmm... Rapaz um pouco menos!')
print('Acertou com {} palpites. Boa meu consagrado!!'.format(palpites))
