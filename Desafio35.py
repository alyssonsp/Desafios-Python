# Desafio 35 - Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar um triângulo.

print('#########################')
print('Analisador de triângulos')
print('#########################')
s1 = float(input('Primeiro seguimento: '))
s2 = float(input('Segundo seguimento: '))
s3 = float(input('Terceiro seguimento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos acima formam um triângulo.')
else:
    print('Os seguimentos acima NÃO formam um triângulo.')
