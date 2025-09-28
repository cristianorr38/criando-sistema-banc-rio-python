# Início do código

## Função de depósito
def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor do depósito deve ser positivo!")
    return saldo, extrato

## Função de saque
def sacar(valor, saldo, extrato, LIMITE_SAQUES, numero_saques, /):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > 500:
        print("Operação falhou! O valor do saque excede o limite de R$ 500.00 por saque!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques diários atingido (Limite de 3 saques diários)!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor do saque deve ser positivo!")
    return saldo, extrato, numero_saques

## Função de exibir extrato
def exibir_extrato(saldo, extrato, /):
    print("\n=== EXTRATO ===\n")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual: R$ {saldo:.2f}.\n")
    print("===============")

## Função principal
def transacoes_bancarias():
    saldo = 0.0
    extrato = []
    LIMITE_SAQUES = 3
    numero_saques = 0

    while True:
        print("\n=== MENU ===\n")
        print("d - Depositar")
        print("s - Sacar")
        print("e - Visualizar Extrato")
        print("t - Terminar\n")
        opcao = input("Escolha uma opção de transação bancária: ")

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(valor, saldo, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, LIMITE_SAQUES, numero_saques)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "t":
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break
        else:
            print("Operação inválida! Por favor, selecione uma opção válida!")

## Chamda da da função principal
transacoes_bancarias()
    
# Fim do código
