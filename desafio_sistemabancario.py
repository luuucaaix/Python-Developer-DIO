menu = """

   #INSIRA UMA DAS OPÇÕES ABAIXO#
    
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira o valor que deseja depositar: "))
        if deposito > 0:
            saldo = saldo + deposito
            extrato += f"Depósito: R$: {deposito:.2f}\n"
        else:
            print("Insira um valor valido.")

    elif opcao == "s":
        saque = float(input("Insira o valor que deseja sacar: "))
        if saldo - saque > 0:
            if saque <= 500 and numero_saques < LIMITE_SAQUES:
                saldo = saldo - saque
                numero_saques += 1
                extrato += f"Saque: R$: {saque:.2f}\n"
                print(f"Você ainda pode realizar {LIMITE_SAQUES-numero_saques} saque(s) hoje.")

            elif saque > 500:
                print("Saque máximo R$500.00, favor inserir um valor entre 0 e 500.")

            elif numero_saques == LIMITE_SAQUES:
                print("Você já realizou o número máximo de saques permitido.")
        else:
            print("Saldo insuficiente.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, favor inserir uma das opções do menu.")
