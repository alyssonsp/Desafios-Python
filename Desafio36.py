# Desafio 36 - Escreva um programa para aprovar o emprestimo bancário para a
# compra de um apartamento. Pergunte o valor do apartamento, o salário do comprador
# e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o emprestimo será negado.

apartamento = float(input('Qual o valor do apartamento? '))
salário = float(input('Qual o salário mensal do comprador? '))
anos = int(input('Em quantos anos vai pagar o apartamento? '))
prestação = apartamento / (anos * 12)
mínimo = salário * 30 /100
print('Para comprar o apartamento de R${:.2f} a prestação será de R${:.2f} '.format(apartamento, prestação))
if prestação <= mínimo:
    print('O empréstimo pode ser CONCEDIDO!')
else:
    print('O empréstimo foi NEGADO!')


