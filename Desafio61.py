# Desafio 61 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão
# de uma PA, mostrando os 10 primeiros termos de progressão usando a
# estrutura while.

print('Gerador de PA')
print('-----------//----------')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo = termo + razão
    cont = cont + 1
print('FIM')
