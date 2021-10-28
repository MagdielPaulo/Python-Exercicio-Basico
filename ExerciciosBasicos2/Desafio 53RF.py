#### Deasafio, Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[31mBUM\033[31m \033[32mBUM\033[32m \033[33mPOOOW!!\033[33m')
  
