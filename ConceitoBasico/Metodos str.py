########### "Is" métodos de diferentes testes de tipos (str) ###########

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?',a.isspace())
print('Só tem letras maiúsculas?',a.isupper())
print('Só tem números?',a.isnumeric())
print('Tem letras e números?',a.isalnum())
print('Só tem letras minúsculas?',a.islower())