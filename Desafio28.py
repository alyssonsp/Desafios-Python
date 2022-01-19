# Desafio 28 - Escreva um programa que faça o computador "Pensar" em um
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu.

from random import randint
computador = randint(0, 5) # Faz o computador sortear um numero de 0 a 5.
print("#######################################################")
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print("#######################################################")
jogador = int(input('Em que numero eu pensei ? '))
if jogador == computador:
    print('PARABÉNS! Você adivinhou, o numero que eu pensei foi o {}.'.format(computador))
else:
    print('ERROOOOOU! Você não conseguiu adivinhar, o número que pensei foi o {}.'.format(computador))





