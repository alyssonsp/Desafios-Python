# Desafio 31 - Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagem até 200km e R$0,45
# para viagens mais longes.

km = int(input('Qual a distância da viagem em km? '))
print('Você está prestes a fazer uma viagem de {}km'.format(km))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('E o preço da sua passagem é de R${:.2f}'.format(preco))

