'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

nota1 = float(input("Informe sua primeira nota:"))
nota2 = float(input("Informe sua segunda nota:"))
nota3 = float(input("Informe sua terceira nota:"))
nota4 = float(input("Informe sua quarta nota:"))
print("Se sua média for maior que 5 você está aprovado")

media = (nota1 + nota2 + nota3 + nota4) / 4
if ( media <= 5):
    print(f"O aluno não está aprovado pois sua média é {media}, e a mesma é menor que 5")
else:
    print(f"você foi aprovado pois sua média é {media}, e a mesma é maior que 5")