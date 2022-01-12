# Desafio 04 - Faça um programa  que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possivel sobre ele.

n = input('Digite algo ')
print('O tipo primitivo desse valor é: ', type(n))
print('O que digitou é uma letra ?', n.isalpha())
print('O que digitou é um número ?', n.isnumeric())
print('O que digitou é alfanúmerico?', n.isalnum())
print('O que digitou é uma letra maiúscula ?', n.isupper())
print('O que digitou é uma letra minúsculal ?', n.islower())

