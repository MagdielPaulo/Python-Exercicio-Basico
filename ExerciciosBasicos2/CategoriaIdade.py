#### A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year
nasc  = int(input('Ano de nasciemento: '))
idade = atual - nasc

print('\033[1;31mQuem nasceu em {} tem {} anos.\033[m'.format(nasc, idade))

if idade <= 9:
    
    print('\033[1;32mCLASSIFICÇÃO : MIRIM\033[m')

elif idade <= 14:

    print('\033[1;33mCLASSIFICAÇÃO : INFANTIL\033[m')

elif idade <= 19:

    print('\033[1;34mCLASSIFICAÇÃO : JÚNIOR\033[m')

elif idade <= 25:

    print('\033[1;35mCLASSIFICAÇÃO : SÊNIOR\033[m')

elif idade > 25:

    print('\033[1;36mCLASSIFICAÇÃO : MASTER\033[m')



