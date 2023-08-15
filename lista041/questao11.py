'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

num = int(input("Informe um número com três algarismos: "))

if (num >= 100 and num <= 999):
    centenas = num // 100
    print(f"O algarismo das centenas de {num} é {centenas}")
else:
    print(f"O valor informado não tem três algarismos")