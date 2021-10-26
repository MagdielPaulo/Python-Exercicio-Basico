##### Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento #####

salário = float(input('Qual o salário do funcionario ? R$ '))
novo    = salário + (salário * 15 / 100)
print('O salário de R${:.2f}, ficou com aumento o novo salário fica partir de R${:.2f}.'.format(salário,novo))
