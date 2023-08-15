'''
10) Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

num = int(input("Informe um número:"))
num2 = int(input("Informe outro número:"))

if (num2 % num):
    print(f"{num2} é divisível pelo primeiro número")
else:
    print("Ele não é divisível")