# Desafio 33 - Faça um programa que leia três números e mostre qual é
# o maior e qual é o menor.

print('Digite três valores diferentes...')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi o {}.'.format(menor))
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi o {}.'.format(maior))
