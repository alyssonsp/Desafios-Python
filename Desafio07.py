# Desafio 07 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A media entre {} e {} é de {}.' .format(n1, n2, m))
