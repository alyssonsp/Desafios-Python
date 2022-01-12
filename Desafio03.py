# Desafio 03 - Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input('Primeiro número '))
num2 = int(input('Segundo número '))
soma = num1 + num2
# print('A soma entre o', num1, 'e', num2, 'corresponde ao valor', soma)
print('A soma entre {} e {} corresponde ao valor {}' .format(num1, num2, soma))