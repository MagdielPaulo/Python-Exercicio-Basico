#### Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

print('\033[31m{:=^40}'.format('\033[31mLOJA MAGDIEL\033[31m'))
preço = float(input('Preço das compras: R$'))
print('''\033[32mFORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão\033[32m''')
opção = int(input('\033[33mQual a sua opção? \033[33m'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('\033[34mSua compra será parcelada em 2x de R${:.2f} SEM JUROS\033[34m'.format(parcela))
elif opção == 4:
    total = preço + (preço*20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(totparc,parcela))
else:
    total = 0
    print('\033[36mOPÇÃO INVÁLIDA DE PAGAMENTO\033[36m')
    
print('\033[35mSua compra de R${:.2f} vai custar R${:.2f} no final.\033[35m'.format(preço, total))