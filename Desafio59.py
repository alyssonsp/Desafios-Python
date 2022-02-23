# Desafio 59 - Crie um programa que leia dois valores e mostre um
# menu como abaixo: Seu programa deve realizar a operação solicitada em cada caso.
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] somar 
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {}+{} = {}.'.format(num1, num2, soma))
    elif opção == 2:
        multiplicação = num1 * num2
        print('A multiplicação entre {}X{} = {}.'.format(num1, num2, multiplicação))
    elif opção == 3:
        if num1 > num2:
            maior = num1
            print('Entre o {} e {} o {} é o número maior.'.format(num1, num2, maior))
        elif num1 < num2:
            maior = num2
            print('Entre o {} e {} o {} é o número maior.'.format(num1, num2, maior))
        else:
            print('Os dois números são iguais!')
    elif opção == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    print('====================||=====================')
print('Fim do programa !')
