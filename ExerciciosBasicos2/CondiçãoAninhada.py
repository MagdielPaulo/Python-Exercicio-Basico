''' Estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python. '''

nome = str(input('Qual o seu nome ?')).strip()
if nome == 'Magdiel':
    print('Nossa que nome Bonito')

elif nome in 'Ana':
    print('Belo nome feminino')

elif nome == 'Pedro' or 'Maria' or 'João':
    print('Seu nome é bem comum no Brasil !')

else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!!'.format(nome))
