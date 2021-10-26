#### Desafio, desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até
# 200 km e R$ 0,45 para viagens mais longas.

'''dis = float(input('Qual foi a distância de sua viagem ?'))         
print('Você está prestes a começar uma viagem de {}km')
if dis <=200:
    preço = dis * 0.50                                                  #====> Condição normal de if e Else
else:
    preço = dis * 0.45
print('E o preço de sua passgem será de R${:.2f}'.format(preço))'''

dis = float(input('Qual foi a distância de sua viagem ?'))
print('Você está prestes a começar uma viagem de {}km'.format(dis))                 #====> Condição simplificada.
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print('E o preço de sua passgem será de R${:.2f}'.format(preço))