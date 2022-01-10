preco = float(input('Qual o preço do produto? R$'))
desconto = preco - (preco * 5) /100
print('O preço que custava R${:.2f}, na promoção com desconto de 5%, irá custar R${:.2f} ' .format(preco, desconto))