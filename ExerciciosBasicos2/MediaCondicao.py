#### Um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO


nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2

if  7 > média >= 5:
    
    print('\033[1;31mSua nota foi {:.1f} e é entre 5.0 e 6.9 portando você está em recuperação\033[m'.format(média))       #==> "entre e" 

elif média < 5.0:

    print('\033[1;32mSua nota foi {:.1f} e é abaixo 5.0 portanto está REPROVADO\033[m'.format(média))

elif média >= 7.0:
    
    print('\033[1;33mSua nota foi {:.1f} portando você foi APROVADO !!!\033[m'.format(média))
