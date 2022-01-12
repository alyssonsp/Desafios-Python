# Desafio 14 - Escreva um programa que converta uma temperatura digitada em °C
# e convertida para °F.

c = float(input('Informe a temperatura em C: '))
f = ((9*c)/5)+32
print('A temperatura em {} °C corresponde a {}°F !' .format(c, f))