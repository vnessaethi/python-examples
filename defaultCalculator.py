print("\n******************* Python Calculator *******************")

# Variavel que armazena a escolha da operação
print("\nOperações disponíveis:\n")
print("\n1 - Soma")
print("\n2 - Subtração")
print("\n3 - Multiplicação")
print("\n4 - Divisão\n")

opcao = input("\nEscolha uma operação (1/2/3/4): ")

# Função de soma
def soma():
    primeiro = int(input("\nDigite o primeiro valor: "))
    segundo = int(input("\nDigite o segundo valor: "))
    soma = primeiro + segundo
    print("\nA soma entre {0} e {1} é: ".format(primeiro,segundo), soma)
    return;

def subtracao():
    primeiro = int(input("\nDigite o primeiro valor: "))
    segundo = int(input("\nDigite o segundo valor: "))
    subtracao = primeiro - segundo
    print("\nA subtração entre {0} e {1} é: ".format(primeiro,segundo), subtracao)
    return;

def multiplicacao():
    primeiro = int(input("\nDigite o primeiro valor: "))
    segundo = int(input("\nDigite o segundo valor: "))
    multiplicacao = primeiro * segundo
    print("\nA multiplicação entre {0} e {1} é: ".format(primeiro,segundo), multiplicacao)
    return;

def divisao():
    primeiro = int(input("\nDigite o primeiro valor: "))
    segundo = int(input("\nDigite o segundo valor: "))
    divisao = primeiro / segundo
    print("\nA divisão entre {0} e {1} é: ".format(primeiro,segundo), divisao)
    return;

# Operação para validar a opção escolhida no input
if opcao == '1':
    soma()
elif opcao == '2':
    subtracao()
elif opcao == '3':
    multiplicacao()
elif opcao == '4':
    divisao()
else:
    print("\nOpção inválida para as operações exibidas. Tente novamente!")
