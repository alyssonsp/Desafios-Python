# Desafio 44 - Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro 10% de desconto
# - À vista no cartão 5% de desconto
# - Em até 2x no cartão: Preço normal
# - Em 3x ou mais no cartão: 20% de juros

print("=============== LOJAS ALYSSON ===============")
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista no dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcelas = int(input('Qual o total das parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcelas, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, total))





