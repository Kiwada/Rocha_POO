from random import randint
from conta import Conta

def pesquisar_conta(contas, numero):
    for i, conta in enumerate(contas):
        if conta.get_numero() == numero:
            return contas[i]


def menu():
    op = -1
    while True:
        print("\n########## MENU PRINCIPAL ##########")
        print("1. Criar Conta      2. Mostrar Saldo")
        print("3. Depósitar        4. Sacar Valor")
        print("5. Transferência    6. Extrato")
        print("7. Relatório")
        print("0. Sair")
        print("------------------------------------")
        try:
            op = int(input("Digite sua opção -> "))
        except:
            op = -1
        if 0 <= op <= 7:
            return op
        else:
            print("Opção inválida!")
            print("------------------------------------")
            continue


def principal():
    contas = []
    while True:
        op = menu()
        if op == 0:
            break
        elif op == 1:
            print("====================================")
            print("######## CRIANDO UMA CONTA #########")
            print("====================================")
            numero = randint(1000, 9999)
            titular = input("Nome do cliente: ").upper()
            try:
                valor = float(input("Saldo inicial: "))
            except:
                print("Valor inválido!")
                print("Criando conta com saldo: R$ 0.00")
                valor = 0.00
            contas.append(Conta(numero, valor, titular))
            print(f"Conta {numero} criada com sucesso!")
            print("====================================")
        elif op == 2:
            num = int(input("Número da conta: "))
            conta = pesquisar_conta(contas, num)
            if conta:
                print("====================================")
                print("########## SALDO EM CONTA ##########")
                print("====================================")
                conta.mostrar_saldo()   # Implementar
            else:
                print("Conta inexistente")
            print("====================================")
        elif op == 3:
            print("====================================")
            print("######## DEPÓSITO EM CONTA #########")
            print("====================================")
            try:
                num = int(input("Número da conta: "))
                valor = float(input("Valor a depositar: "))
            except:
                print("Valor inválido!")
            else:
                conta = pesquisar_conta(contas, num)
                if conta:
                    conta.depositar(valor) # Implementar
                else:
                    print("Conta inexistente")
            print("====================================")
        elif op == 4:
            print("====================================")
            print("########## SAQUE EM CONTA ##########")
            print("====================================")
            try:
                num = int(input("Número da conta: "))
                valor = float(input("Valor a sacar: "))
            except:
                print("Valor inválido!")
            else:
                conta = pesquisar_conta(contas, num)
                if conta:
                    if conta.sacar(valor): #Implementar
                        print("Saque realizado com sucesso!")
                    else:
                        print("Saque não realizado")
                        print("Saldo insuficiente!")
                else:
                    print("Conta inexistente")
                print("====================================")
        elif op == 5:
            try:
                num1 = int(input("Número da conta de origem: "))
                num2 = int(input("Número da conta de destino: "))
                valor = float(input("Valor a transferir: "))
            except:
                print("Valor inválido!")
            else:
                print("====================================")
                print("#### TRANSFERÊNCIA ENTRE CONTAS ####")
                print("====================================")
                conta1 = pesquisar_conta(contas, num1)
                conta2 = pesquisar_conta(contas, num2)
                if conta1 and conta2:
                    if conta1.transferir(conta2, valor):
                        print("Transferência realizada com sucesso!")
                    else:
                        print("Transferência não realizada")
                        print("Saldo insuficiente!")
                else:
                    print("Conta de origem/destino inexistente")
                print("====================================")
        elif op == 6:
            num = int(input("Número da conta: "))
            conta = pesquisar_conta(contas, num)
            print("====================================")
            print("######### EXTRATO DE CONTA #########")
            print("====================================")
            if conta:
                conta.extrato()
            else:
                print("Conta inexistente")
            print("====================================")
        elif op == 7:
            print("====================================")
            print("####### RELATÓRIO DE CONTAS ########")
            print("====================================")
            for conta in contas:
                conta.mostrar_saldo()
            print("==================================")
        else:
            print("\n######### OPÇÃO INVÁLIDA #########\n")


if __name__ == "__main__":
    principal()