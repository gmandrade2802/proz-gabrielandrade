"""
Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o comando print(). 
O primeiro array deve conter os produtos de uma loja da sua escolha (loja de comida, materiais de construção, música, etc). 
O segundo array deve conter os anos de nascimento de familiares e amigos seus. 
Lembre-se de usar nomes descritivos para nomear cada variável, e 
de usar o tipo de dado apropriado para cada lista (strings, booleanos, números inteiros, floats).
"""

loja_de_construcao = ["Cimento","Tijolo","Areia","Vergalhão","Enxada"]
ano_nascimento_irmaos = [1986,1987,1992,1994,1998]

print("Materiais disponíveis:")
for material in loja_de_construcao:
  print(loja_de_construcao.index(material)+1," - ", material)

print("Ano de nascimento entre irmãos:")
for ano in ano_nascimento_irmaos:
  print(ano_nascimento_irmaos.index(ano)+1," - ", ano)
