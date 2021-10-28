# EQUILÁTERO: todos os lados iguais.
# ISÓSCELES: dois lados iguais, um diferente.
# ESCALENO: todos os lados diferentes.

a = float(input('Diga o primeiro segmento: '))
b = float(input('Diga o segundo segmento: '))
c = float(input('Diga o terceiro segmento: '))

if a+b>c and b+c>a and a+c>b :
    print('Sim os segmentos acima pode FORMAR UM triângulo ! ',   end='')
    if a == b == c:                                                           ### Outra forma de se construir uma condição aninhada.
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO !')
    else:
        print('ISÓSCELES!!')
else:
    print('Infelizmente não pode formar um triângulo !')