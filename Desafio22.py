# Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {} '.format(nome.upper()))
print('Seu nome em minúsculas é {} '.format(nome.lower()))
print('Seu nome tem ao todo {} de letras' .format(len(nome)-nome.count(' ')))
primeiro_nome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))
