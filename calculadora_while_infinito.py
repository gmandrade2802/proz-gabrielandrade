"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""
# função que imprime um menu simples em tela
def menu():
    print("===========================")
    print("=== Calculadora  Básica ===")
    print("===========================")
    print("=== 1. Soma             ===")
    print("=== 2. Subtração        ===")
    print("=== 3. Multiplicação    ===")
    print("=== 4. Divisão          ===")
    print("=== 0. Sair             ===")
    print("===========================")
    return
#função para calcular as 4 operações disponíveis
def calculadora(num1, num2, operacao):
    if (operacao == 1):
        return num1 + num2
    elif (operacao == 2):
        return num1 - num2
    elif (operacao == 3):
        return num1 * num2
    elif (operacao == 4):
        if (num2 > 0):
            return num1 / num2
        else:
            return 0
    else:
        return 0
# while infinito. Obs.: Saída somente após o comando break
while (True):
    menu()
    operacao = int(input("Digite a operação: "))
    if (operacao in [0,1,2,3,4]):
        if (operacao == 0):
            print("Saindo...")
            break
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print("O Resultado é: ", calculadora(num1,num2,operacao))
    else:
        print("Essa opção não existe")
