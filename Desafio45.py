# Desafio 45 - Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('O jogo empatou !')
    elif jogador == 1:
        print('Parabéns, você GANHOU !')
    elif jogador == 2:
        print('Você PERDEU, o computador venceu ! ')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('Você PERDEU, o computador venceu ! ')
    elif jogador == 1:
        print('O jogo empatou !')
    elif jogador == 2:
        print('Parabéns, você GANHOU !')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Parabéns, você GANHOU !')
    elif jogador == 1:
        print('Você PERDEU, o computador venceu ! ')
    elif jogador == 2:
        print('O jogo empatou !')
    else:
        print('JOGADA INVÁLIDA!')
