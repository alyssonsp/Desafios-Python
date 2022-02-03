# Desafio 42 - Refaça o Desafio35 dos triângulos, acrecentando o recurso de
# mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais.
# - Isósceles: Dois lados iguais.
# - Escaleno: Todos os lados diferentes.

print('#########################')
print('Analisador de triângulos')
print('#########################')
s1 = float(input('Primeiro seguimento: '))
s2 = float(input('Segundo seguimento: '))
s3 = float(input('Terceiro seguimento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos acima formam um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os seguimentos acima NÃO formam um triângulo.')
