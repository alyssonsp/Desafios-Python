# Desafio 08 - Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

n1 = int(input('Escreva um valor em metro: '))
c = n1*100
m = n1*1000
print('Você digitou {} m' .format(n1))
print('Que é o mesmo de {} centimetros.' .format(c))
print('Que é o mesmo de {} milimetros.' .format(m))