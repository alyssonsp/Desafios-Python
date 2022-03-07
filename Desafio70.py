# Desafio 70 - Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = maiormil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço R$'))
    cont = cont + 1
    total = total + preço
    if preço > 1000:
        maiormil = maiormil + 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer contunuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA!')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maiormil} produtos que custam mais que 1000 reais.')
print(f'O produto mais barato foi o {produto} e custa R${menor}.')

