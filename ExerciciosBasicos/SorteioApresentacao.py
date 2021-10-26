##### O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#### faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


''' ##### Primeiro método de importação básico sem especificar o método #####

import random

al1 = (input('Primiero Aluno: '))
al2 = (input('Segundo Aluno: '))
al3 = (input('Terceiro Aluno: '))
al4 = (input('Quarto Aluno: '))

lista = [al1,al2,al3,al4]

random.shuffle(lista)

print('A ordem dos quatros alunos a ao apagar o quadro será: {}'.format(lista)) '''

#### Segundo método de importação com especificamento do método ####

from random import shuffle

tri1 = (input('Primeiro tripulante: '))
tri2 = (input('Segundo tripulante: '))
tri3 = (input('Terceiro tripulante: '))
tri4 = (input('Quarto tripulante: '))

lista = [tri1,tri2,tri3,tri4]

shuffle(lista)
print('A ordem dos tripulantes a subur abordo do caminhao vai ser: {}'.format(lista))