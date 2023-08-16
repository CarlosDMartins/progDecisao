'''
7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
'''

num = float(input("Informe um número:"))
num2 = float(input("Informe outro número:"))

if (num < num2):
    print(f"{num} é menor que {num2}")
if (num2 < num):
    print(f"{num2} é menor que {num}")
if (num == num2):
    print(f"{num} e {num2} são iguais")