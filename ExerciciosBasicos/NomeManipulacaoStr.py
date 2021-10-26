#### Desafio, Crie um programa que leia o nome completo de uma pessoa e mosrtre:
#=> O nome com todas as letras maiúsculas.
#=> O nome com todas as letras minúsculas.
#=> Quantas letras ao todo (sem considerar espaços).
#=> Quantas letras tem o primiero nome.

nome = (input('Digite o seu nome completo:')).strip()                               #=====> pode adicionar o método "strip()" depois de ler o nome 
print ('O nome com todas as letras Maiúsculas é: {}'.format(nome.upper()))        #para corta o espaço dos lado esquerdo e direito
print ('O nome com todas as letras minúsculas é: {}'.format(nome.lower()))
print ('A quantidade de letras ao todo é: {}'.format(len(nome) - nome.count(' '))) #======> Esse menos com o "-nome.count(' ')" é para retirar os espeços do meio.
separa = (nome.split())                                                                                #=======> Criando uma variavel pra ultilizar o metodo split para separar os nome 
print ('O seu primeiro nome é {} com o total de letras de: {}'.format(separa[0], len(separa[0])))      #pra pegar o primeiro nome na fila sendo o 0.