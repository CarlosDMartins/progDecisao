'''
10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
Média Situação

Abaixo de 3,0 Reprovado
Entre 3,0 e 6,9 Prova Final
A partir de 7,0 Aprovado
'''

nome = (input("Informe seu nome:"))
nota1 = int(input("Informe sua nota:"))
nota2 = int(input("Informe sua outra nota:"))

media = (nota1 + nota2) / 2

if (media < 3):
    print("Você está reprovado")
elif (media <= 6.9):
    print("Você está de prova final")
else:
    print("Você foi aprovado, Parabéns")



