'''
7) Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Informe um número:"))

som = num + num

if ( som >= 0 ):
    print(f"{num} é positivo")
else:
    print(f"{num} é negativo")