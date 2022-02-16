# Desafio 49 - Refaça o Desafio 09, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver a tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))

