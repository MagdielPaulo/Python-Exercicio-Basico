#### Desafio, escreva um programa que leia a velocidade de um carro.
# se ele ultrapassa 80km/h, mostre uma mensagem dizendo que ele foi multado.
# a multa vai custar R$7,00 por cada km acima do limite.


velocidade = float(input('Qual é a velocidade atual do carro: '))
if velocidade >80:
    print('O seu carro foi multado por ter ultrapassado os 80km/h !')
    multa = (velocidade - 80) * 7.00
    print('A multa que você vai pagar é de: R$ {:.2f}'.format(multa))
else:
    print('Tenha um Bom dia! Dirija com segurança!')

