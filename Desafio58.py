# Desafio 58 - Melhore o jogo do DESAFIO 28 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10) # Faz o computador sortear um numero de 0 a 5.
print("#######################################################")
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print("#######################################################")
jogador = int(input('Em que numero eu pensei ? '))
tentativas = 0
acertou = False
while not acertou:
    if computador > jogador:
        print('Mais... Tente mais uma vez.')
        tentativas = tentativas + 1
        jogador = int(input('Em que numero eu pensei ? '))
    if computador < jogador:
        print('Menos... Tente mais uma vez.')
        tentativas = tentativas + 1
        jogador = int(input('Em que numero eu pensei ? '))
    if jogador == computador:
        acertou = True
        tentativas = tentativas + 1
        print('Você acertou com {} tentativas, Parabéns.'.format(tentativas))


