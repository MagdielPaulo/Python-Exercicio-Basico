#### Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o ultimo nome separadamente.

#Ex:Ana Maria de Souza
#Primeiro = Ana
# Ultimo = Souza

n = str(input('Diga o seu nome completo: ')).title().strip()
nome = n.split()
print ('O primeiro nome é: {}'.format(nome[0]))
print ('O seu Ultimo nome é: {}'.format(nome[len(nome)-1]))        ### usando a função len de nome eu vou saber quantas posição tem nome
                                                                   ### então eu posso fazer ele me mostre o nome na posição, len de nome -1 porque
                                                                   ### porque ele conta o 0.