# Melhore o DESAFIO 61, perguntando para o úsuario se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-----------//----------')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo = termo + razão
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados. '.format(total))
