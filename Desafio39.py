# Desafio 39 - Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}. '.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE! ')
elif idade < 18:
    ano = 18 - idade
    futuro = ano + atual
    print('Ainda falta {} anos para se alistar.'.format(ano))
    print('Você deve se alistar no ano de {}'.format(futuro))
elif idade > 18:
    ano = idade - 18
    passado =atual - ano
    print('Você deveria ter se alistado há {} anos. '.format(ano))
    print('Seu alistamento foi em {}.'.format(passado))





