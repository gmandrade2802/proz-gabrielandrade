"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""
#função que imprime um menu simples em tela
def menu():
    print("===========================")
    print("=== Calculadora  Básica ===")
    print("===========================")
    print("=== 1. Soma             ===")
    print("=== 2. Subtração        ===")
    print("=== 3. Multiplicação    ===")
    print("=== 4. Divisão          ===")
    print("=== 5. Sair             ===")
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
        #Não permite divisão por zero
        if (num2 > 0):
            return num1 / num2
        else:
            return 0
    else:
        return 0
#primeira impressão do menu
menu()
operacao = int(input("Digite a operação: "))
while (operacao in [1,2,3,4]):
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print("O Resultado é: ", calculadora(num1,num2,operacao))
    #exibe o menu para uma nova operação ou saída do programa
    menu()
    operacao = int(input("Digite a operação: "))
