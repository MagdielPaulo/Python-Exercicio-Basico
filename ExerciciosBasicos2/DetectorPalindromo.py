### Um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palvras = frase.split()
junto = ''.join(palvras)
inver = junto[::-1]                                               #### <---  APENAS COM O TRATAMENTO DE UMA STRING

'''for c in range(len(junto) - 1, -1, -1):                        #### <---  USANDO LAÇO FOR
    inver += junto[c]'''

print('O inversor de {} é {}'.format(junto, inver))             
if inver == junto:
    print('Temos um palíndromo!')
else:
    print('NÂO é um palíndromo!')

