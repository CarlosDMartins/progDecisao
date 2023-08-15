'''
9) Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = float(input("Informe um número:"))

if (num > 0):
    print("Este número é positivo")
elif (num == 0):
    print("Este número é nulo")
else:
    print("Este número é negativo")