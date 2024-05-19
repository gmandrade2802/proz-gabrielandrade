"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
"""
def verifica_idade(ano):
    if (ano >= 1922 and ano <= 2021):
        return 2022 - ano
    else:
        raise Exception("O ano de nascimento deve ser entre 1922 e 2021.")
nome_completo = input("Digite seu nome completo: ")
while (True):
    try:
        ano = int(input("Digite seu ano de nascimento: "))
        idade = verifica_idade(ano)
        print("Seu nome é ",nome_completo," e completará ",idade," anos em 2022")
        break
    except Exception as e:
        print("Digite um ano válido.")
        print("Detalhe do erro: ",e)
        
        
