menu = """

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
    print(f"\nSeu saldo atual é de R$ {saldo:.2f}")
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("Informe aqui o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Operação realizada com sucesso!")

            else:
                print("Operação falhou! \nFaça o deposito com um valor positivo.")

        case "s":
            print(f"Voce tem direito a {LIMITE_SAQUES - numero_saques} saques")
            
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
                continue

            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1            
                print(f"Operação realizada com sucesso!")

            else:
                print("Operação falhou! O valor informado é inválido.")

        case "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        case "q":
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
