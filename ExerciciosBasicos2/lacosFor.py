#### Os laços e vamos fazer primeiro o “for” ####


############################## EXEMPLO ############################## 

'''for c in range(0,6):
    print('Oi')                             
print('FIM')'''

############################## EXEMPLO ############################## 

'''n = int(input('Digite um número: '))
for c in range(0, n+1):                     
    print(c)
print('FIM')'''

############################## EXEMPLO ############################## 

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

############################## EXEMPLOS ############################## 

'''for c in range(0,3):
    n = int(input('Digite um valor: '))
print('FIM')'''

############################## EXEMPLOS ############################## 

s = 0
for c in range(0,4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os valores é: {}'.format(s))
print('FIM')