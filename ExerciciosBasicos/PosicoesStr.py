#### Faça um programa que leia uma frase pelo teclado e mostre
#=> Quantas vezes aparece a letra "A".
#=> Em que posição ela aparece a primeira vez.
#=> Em que posição ela aparece a útima vez.

frase = str(input('Digite um frase: ')).strip().upper()
print ('A letra "A" apareceu {} vezez !'.format(frase.count('A')))
print ('A primeira vez que ela aparece é na posição: {}'.format(frase.find('A')+1))        ## O +1 nesse caso ta servindo para o entendimento no geral
print ('A ultima vez que ela aparece é na posição: {}'.format(frase.rfind('A')+1))         ## das pessoas e não ficar aquela posição 0 que poucos entenderia.
                                                                                            
                                                                                           ## No ultimo caso se inicia a busca pela direita assim sabendo o ultimo
                                                                                           ## com o método rfind(pela direita da string iniciando de 1)