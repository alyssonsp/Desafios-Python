# Desafio 24 - Crie um programa que leia o nome de uma cidade e
# diga se ela começa ou não com o nome "Santo".

cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')