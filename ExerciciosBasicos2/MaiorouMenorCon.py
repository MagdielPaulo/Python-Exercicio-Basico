#### Desafio, Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: ####
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais


num1 = int(input('Digite o primiero número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    
    print('\033[1;31mO primeiro valor é MAIOR\033[m')

elif num1 < num2:
    
    print('\033[1;32mO segundo valor é MAIOR\033[m')

elif num1 == num2:
    
    print('\033[1;33mNão existe valor maior, os dois são iguais.\033[m')

print('\033[1;34mComparação finalizada com sucesso !\033[m')
