'''
Crie um programa que pergunte a idade do usuário
e em seguida informe se este usuário é menor de idade ou maior de idade.
'''

idade = int(input("Informe sua idade:"))

#lógica do op ternário: var = (se for falso, se for verdadeiro)[teste condicional]
resposta = ("Você é menor de idade", "você é maior de idade")[idade>=18]

print(resposta)

