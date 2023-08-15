'''
1) Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num = float(input("Informe um número:"))

if ( num >= 20 ):
    div = num / 2
    print(f"A metade deste número é {div}")
else:
    print(f"{num} é menor que 20")