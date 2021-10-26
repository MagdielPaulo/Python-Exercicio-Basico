#### Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#### Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

''' #### Primeira forma de importação ####

import random

Aluno1 = (input('Primeiro nome: '))
Aluno2 = (input('Segundo nome: '))
Aluno3 = (input('Terceiro nome: '))                  
Aluno4 = (input('Quarto nome: '))

lista = [Aluno1, Aluno2, Aluno3, Aluno4]

escolhido = random.choice(lista)
print('O escolhido entre os alunos foi o(a): {} '.format(escolhido)) '''

   
   
        #### Segunda forma de importação ####

from random import choice

c1 = (input('Primeiro carro: '))
c2 = (input('Segundo carro: '))
c3 = (input('Terceiro carro: '))
c4 = (input('Quarto carro: '))

lista = [c1,c2,c3,c4]

premiado = choice(lista)

print('O carro premiado foi o: {}'.format(premiado)) 

    