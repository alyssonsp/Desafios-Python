# Desafio 40 - Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a media atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2)/2
print('Tirando {} e {}, a média do aluno é {}.'.format(n1, n2, média))
if média < 5:
    print('A média do aluno foi {}, aluno REPROVADO!'.format(média))
elif média >= 5 and média < 7:
    print('A média do aluno foi {}, aluno em RECUPERAÇÃO!'.format(média))
elif média >= 7:
    print('A média do aluno foi {}, aluno APROVADO! '.format(média))


