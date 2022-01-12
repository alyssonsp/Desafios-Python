# Desafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar.

real = float(input('Qual valor que você tem na carteira? R$'))
dolar = real / 5.68
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))