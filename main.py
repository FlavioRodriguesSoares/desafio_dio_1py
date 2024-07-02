menu = """BANCO FRS

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

O que deseja fazer: """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saques = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        deposito = float(input("Valor do deposito R$"))

        if deposito < 0:
            print("Deposito inválido")

        else:
            saldo += deposito
            extrato += f"depósito: +R${deposito: .2f}\n"
            print(f"Depósito de R${deposito:.2f} realizado com sucesso")


    elif opcao == "s":

        saque = int(input("Qual o valor do saque : "))

        if saque < 0:
            print("Operação invalida! tente novamente")

        elif saque > limite:
            print(f'Limite máximo de saque é de R${limite} tente novamente!')

        elif saque > saldo:
            print("Saldo insuficiente")

        elif numero_saque >= limite_saques:
            print("você só pode efetuar 3 saque por dia, tente novamente amanhã.")


        else:
            saldo -= saque
            extrato += f"Saque: -R$ {saque:.2f}\n"
            numero_saque += 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso")


    elif opcao == "e":
        print("\n====== EXTRATO ======")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)

        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("======================")

    elif opcao == "q":
        break

    else:
        print("Operaçõa inválida, por favor selecione novamente a operação desejada.")
