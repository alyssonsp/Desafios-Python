# Desafio 12 - Faça um algoritimo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

preco = float(input('Qual o preço do produto? R$'))
desconto = preco - (preco * 5) /100
print('O preço que custava R${:.2f}, na promoção com desconto de 5%, irá custar R${:.2f} ' .format(preco, desconto))