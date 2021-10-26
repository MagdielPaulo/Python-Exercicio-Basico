#### Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separado.
#Ex: Digite um número: 1834
#=> unidade:4
#=> dezena:3
#=> centena:8
#=> milhar:1

'''num = int(input('Digite um número entre 0 a 9999: '))
n = str(num)
print ('A unidade do seu número é: {}'.format(n[3]))              ## Esse método não deu certo pelo fato que nós não 
print ('A dezena do seu número é: {}'.format(n[2]))               ## ultilizou os 4 digitos no string. 
print ('A centena do seu número é: {}'.format(n[1]))              ## USANDO SÓ UMA CONVERSÃO PRA STRING, QUE DEU ERRADO !!!
print ('O milhar do seu número é: {}'.format(n[0]))'''


num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10                                                 ## Se eu pego um número faço a divisão inteira (//) dele por um,
d = num // 10 % 10                                                ## pegando o módulo de 10 isso é, pegar esse número dividir por 10 pegando o resto
c = num // 100 % 10                                               ## da divisão sendo o resto a minha unidade !! Usando os 4 digitos corretamente da str.
m = num // 1000 % 10                                              ## RESOLVENDO MATEMATICAMENTE !!!
print ('A unidade do seu número é: {}'.format(u))
print ('A dezena do seu número é: {}'.format(d))              
print ('A centena do seu número é: {}'.format(c))
print ('O milhar do seu número é: {}'.format(m))                                                              