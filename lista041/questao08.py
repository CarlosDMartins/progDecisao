'''
8) Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num = int(input("Informe um número:"))

if ( num < 1 ):
    print(f"{num} está abaixo de 1")
elif ( num <= 1 ):
    print(f"{num} está entre 1 e 10")
else:
    print(f"{num} está acima de 10")