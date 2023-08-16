'''
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste
'''

sig = input("Coloque uma sigla de um estado da região sudeste:")

if sig == 'RJ' or sig == 'SP' or sig == 'ES' or sig == 'MG':
    print("Este estado pertence a região sudeste")
else:
    print("Este estado não pertence a região sudeste")