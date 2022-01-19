# Desafio 29 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

