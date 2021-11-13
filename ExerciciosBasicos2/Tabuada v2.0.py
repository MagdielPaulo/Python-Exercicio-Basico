### tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Dogite um numero para ver sua tabuada: '))
for c in range (1,11):
    print('{} x {} = {}'.format(num, c, num*c))