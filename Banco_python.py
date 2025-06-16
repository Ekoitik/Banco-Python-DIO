menu = """
    [d] Depositar
    [s] Sacar
    [e] Estrato
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
        print("Deposito".center(41,"="))
        while True:

            deposito_input = float(input(f"\nInforme o valor a ser depositado: \n"))

            if(deposito_input > 0):
                saldo += deposito_input
                deposito_info = f"Foram depositados R$ {deposito_input}\n"
                extrato += deposito_info
                print(deposito_info)
                print("".center(41,"="))
                break

            elif(deposito_input == 0):
                print("Valor digitado foi 0, logo a operação de depósito foi cancelada")
                break

            else:
                print("Valor inválido para deposito, caso queira desistir do deposito digite 0\n")

    elif opcao == "s":
        print("Saque".center(41, "="))
        while True:

            if(numero_saques < LIMITE_SAQUES):
                saque_input = float(input(f"\nInforme o valor a ser sacado,\no máximo possível por saque é de R$ {limite}:\n"))

                if(saque_input > 0):

                    if(saldo >= saque_input and limite >= saque_input):
                        saldo -= saque_input
                        saque_info = f"Foram sacados R$ {saque_input}\n"
                        extrato += saque_info
                        numero_saques += 1
                        print(saque_info + f"Você fez {numero_saques} de {LIMITE_SAQUES} saques diários\n")
                        print("".center(41,"="))
                        break

                    elif(saldo < saque_input):
                        print(f"Saldo da conta insuficiente para o valor do saque, você possui R$ {saldo} na conta")

                    elif(limite < saque_input):
                        print(f"O valor do saque é maior que o limite, o limite é de R$ {limite}")

                    print("Caso queira desistir do saque, digite 0\n")

                elif(saque_input == 0):
                    print("O valor digitado foi 0, sua operação de saque foi cancelada\n")
                    print("".center(41,"="))
                    break

                else:
                    print("Valor de saque inválido, por favor colocar um valor válido\nCaso queira desistir do saque, digite 0")

            else:
                print("\nVocê atingiu seu limite diário de saques\n")
                print("".center(41,"="))
                break

    elif opcao == "e":
        print("Extrato".center(41, "="))
        extrato_print = "\nNão foram realizadas movimentações" if(extrato == "")  else f"\n{extrato}"
        print(extrato_print)
        print(f"Você possui R${saldo} na conta\n")
        print("".center(41,"="))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")