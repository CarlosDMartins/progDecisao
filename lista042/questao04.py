'''
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Infrome um número:"))

if (num == 1):
    print("Este dia é domingo")
if (num == 2):
    print("Este dia é segunda-feira")
if (num == 3):
    print("Este dia é terça-feira")
if (num == 4):
    print("Este dia é quarta-feira")
if (num == 5):
    print("Este dia é quinta-feira")
if (num == 6):
    print("Este dia é sexta-feira")
if (num == 7):
    print("Este dia é sábado")
if (num > 7):
    print("Número escolhido é inválido")