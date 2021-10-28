#### Um programa para aprovar o empréstimo bancário para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo 
# será negado.

casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

mínimo = salário * 30 / 100                                                      #===> Isso aqui é os 30% do salário do comprador. Sendo o mínimo da parcela que ele tem.
prestação = casa / (anos * 12)                                                   #===> É o preço da casa dividido por quantos meses ele vai pagar que é a quantidade de anos vezes os meses.
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos), end='')    #===> end= é para que o print de baixo continue na mesma linha da frase de cima.
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
