# Desafio 57 - Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter o valor correto.

sexo = str(input('Infome o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MFmf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print('Sexo {} registado com sucesso. '.format(sexo))

