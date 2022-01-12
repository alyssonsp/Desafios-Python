# Desafio 16 - Crie um programa que leia um número real qualquer pelo teclado e
# mostre na tela a sua porção inteira.

import math
quebrado = float(input("Digite um numero quebrado: "))
inteiro = math.floor(quebrado)
print("O numero digitado foi {}, mas sua posição inteira é {} " .format(quebrado, inteiro))
