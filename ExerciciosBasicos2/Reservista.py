#### Um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nasc = int(input('\033[1;7;37mAno de nasciemnto: \033[m'))
idade = atual - nasc

print('\033[1;31mQuem nasceu em {} tem {} anos em {}\033[m'.format(nasc, idade, atual))

if idade == 18:
    
    print('\033[1;32mVocê tem que se alistar IMEDIATAMENTE\033[m')

elif idade < 18:
    
    saldo = 18 - idade
    print('\033[1;33mVocê ainda não tem 18 anos. Ainda faltam {} anos para o alistamneto\033[m'.format(saldo))
    ano = atual + saldo
    print('\033[1;34mSeu alistamento será em {}\033[m'.format(ano))

elif idade > 18:
    
    saldo = idade - 18
    print ('\033[1;35mVocê já deveria ter se alistado há {} anos.\033[m'.format(saldo))
    ano = atual - saldo
    print ('\033[1;36mO seu alistamento foi em {}\033[m'.format(ano))









