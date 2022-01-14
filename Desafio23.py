# Desafio 23 - Faça um programa que leia um numero de 0 a 9999 e mostre na tela
# cada um dos digitos separados.

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} '.format(num))
print('Sua Unidade é: {} '.format(u))
print('Sua Dezena é: {} '.format(d))
print('Sua Centena é: {} '.format(c))
print('Seu Milhar é: {} '.format(m))
