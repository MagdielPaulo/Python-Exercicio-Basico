                        #### Testes com a Manipulação de textos ou tratamento de cadeias de caracteres (String) ####

                                              
                                              ##### Primeira Operação por fatiamneto #####



'''frase = 'Curso em Vídeo Python'          #======> Quando eu quero saber qual letra pertence a posição 9 na lista.
print(frase[9])'''


'''frase = 'Curso em Vídeo Python'          #======> Aqui eu quero saber quais letra pertece nas posição 9 até a 13 na fila
print(frase[9:13])'''                       #(Sabendo que a ultima cadeia é excluída).


'''frase = 'Curso em Vídeo Python'          #======> Aqui acontece o seguinte ele inicia na posição 9 até a 21, já que ele
print(frase[9:21:2])'''                     #excluir sempre a ultima cadeia da lista indicada ele vai para na posição 20 só que não é
                                            #a melhor maneira de fatiar com um numero. E 2 quer dizer que só vai valer de 2 em 2 a partir do nove.


'''frase = 'Curso em Vídeo Python'          #======> Já que antes dos : não tem nenhum número indicado, inicialmente ele começa da posição 0,
print(frase[:5])'''                         #encerrando-se na posição 5(Que é cadeia que vai ser excluída)


'''frase = 'Curso em Vídeo Python'          #======> Logo essa já é o contrário da anterior, dessa vez ela inicia na posição indicada que é 15,
print(frase[15:])'''                        #e encerra no final da cadeia (posição 20)


'''frase = 'Curso em Vídeo Python'          #======> Nesse caso é indicado o início da fila só que o fim não, sendo assim encerrando na ultima posição e
print(frase[9::3])'''                       #o 3 quer dizer que só vai valer de 3 em 3 a partir do incio indicado que seria posição 9.

                                               
                                               
                                               
                                         ##### Segunda Operação por Análise(Através de alguns métodos) #####



'''frase = 'Curso em Vídeo Python'         #======> Com esse método len podemos analisar o comprimeto da string.
print (len(frase))'''


'''frase = 'Curso em Vídeo Python'         #======> Com esse método count podemos analisar buscas de quantas vezes tal letra se repete na frase.
print (frase.count('o'))'''                #isso é separadamente das maiusculas e minusculas.


'''frase = 'Curso em Vídeo Python'         #======> Nesse caso parecido o que muda é que estamos especificando a busca de tal posição a outra(junto com fatiamento).
print (frase.count('o',0,13))'''           #iniciando do 0 até 13(lembrando que o 13 não vai ser incluido) as busca por o (o) minusculo.


'''frase = 'Curso em Vídeo Python'         #======> Nesse método ele vai me dizer em qual posição se encontra tal palavra na string. 
print (frase.find('Curso'))'''


'''frase = 'Curso em Vídeo Python'         #======> Se você colocar uma palavra dentro do find que não tem na string ele lhe retorna com -1.
print (frase.find('Magdiel'))'''


'''frase = 'Curso em Vídeo Python'         #======> Aqui já é mais um operador e não uma função, que quer me dizer se na frase existe tal palavra
print ('Curso' in frase)'''                #me retornando com True ou False para sua existencia.


                                                              
                                                              
                                        ##### Terceira Operação por Transformação(Através de alguns Métodos) #####
                            


## Em primeira regra uma lista de string é imutavél ou seja a gente não consegue mexer nela, há não ser através de métodos !!! ##



'''frase = 'Curso em Vídeo Python'              #======> Esse método faz simplesmete trocar palavras na string ou melhor reposicionar.
print(frase.replace('Python','Cachorro'))'''    #isso não de uma forma primária e sim secundária.


'''frase = 'Curso em Vídeo Python'              #======> Simplesmente esse método vai colocando-as letras em maisculas mantendo as que já estão.
print (frase.upper())'''


'''frase = 'Curso em Vídeo Python'              #======> Já essa é iversa da anterior, colocando-as letras em minusculas mantendo as que já estão.
print (frase.lower())'''


'''frase = 'Curso em Vídeo Python'              #======> Esse método vai buscar a letra inicial e coloccar ela em Maisculo mantendo o resto no minusculo.
print (frase.capitalize())'''


'''frase = 'Curso em Vídeo Python'              #======> Ela faz a mesma coisa do Capitalize, só que a partir de espaços da string, palavra por palavra.
print (frase.title())'''


'''frase = '   Curso em Vídeo Python   '        #======> Método para remover espaços inuteis na string isso dos dois lados.
print (frase.strip())'''


'''frase = '   Curso em Vídeo Python   '        #======> Muito dos métodos que mexe com string tem variações r ou l. Que quer dizer Right(Direita) ou Left(Esquerda)
print (frase.rstrip())'''                       #ou seja nesse caso ele só está removendo ao lado direto da string o espaço inutil.


'''frase = '   Curso em Vídeo Python   '        #======> Aqui ocorre o mesmo caso do anterior só que aqui ele remove o espaço inutil 
print (frase.lstrip())'''                       #pra o lado esquerdo da string. 



                                           ##### Quarta Operação por Divisão(Através de alguns métodos) #####


'''frase = 'Curso em Vídeo Python'              #======> O split vai dividir um string em uma lista onde cada elemento vai ser separado por seu splitador
dividido = (frase.split())                      #por padrão e espaço.
print(dividido[0])'''                           #Bonus.



'''frase = 'Curso em Vídeo Python'              #======> Join faz a junção de strings separados em listas ou melhor o contrário da anterior.           
print (frase.split())
print (''.join(frase))'''


                                                            










