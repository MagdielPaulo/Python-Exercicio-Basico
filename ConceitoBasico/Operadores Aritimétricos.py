###### Operadores Aritiméticos ######

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
p = n1**n2
di = n1//n2
rd = n1%n2
print('A soma {} a subtração {} a multiplicação {} e a divisão {:.3f}'.format(a,s,m,d))
print('A potência {} a divisão inteira {} e o resto da divisão {}'.format(p,di,rd))
