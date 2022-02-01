# Desafio 38 - Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# O primeiro número é maior.
# O segundo número é maior.
# Não existe valor maior, os dois números são iguais.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a > b:
    print('O primeiro numero é maior.')
elif b > a:
    print('O segundo número é maior.')
else:
    print('Não existe valor maior, os dois números são iguais.')



