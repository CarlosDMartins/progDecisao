'''
13) Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = float(input("Informe um a:"))
b = float(input("Informe um b:"))
c = float(input("Informe um c:"))

# 1- a te que ser menor que b
if ( a > b ):
    aux = a
    a = b
    c = aux

# garantido até aqui que entre a e b, o menor está em a

# 2- a tem que ser menor que c

if ( a > c ):
    aux = a
    a = c
    c = aux

 # garantido até aqui que a é o menor dos 3
 # agora é necessário garantir que b seja menor que c

if (b > c):
    aux = b
    b = c
    c = aux

    # garantido até agora que entre b e c, o b é o menor, ou seja, o c é o maior de todos
print(f"Ordem crescente:{a}, {b}, {c}")


