# Desafio 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso   - 25 até 29: Sobrepeso
# Entre 18.5 e 24: Peso Ideal      - 30 até 39: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Informe o peso: (Kg) '))
altura = float(input('Informe a altura: (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

