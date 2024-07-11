import textwrap
def menu():  
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar contas
    [6] Novo Usuário
    [7] Sair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo = saldo + valor
            extrato += f"Deposito: RS {valor:.2f}\n"
            print(f"Você acabou de depositar R$ {valor:.2f}\n")
    else:
        print("Você digitou um valor inválido!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo,/,*,extrato):
    print( "\n----EXTRATO----")
    print("Não foi realizada movimentações!"if not extrato else extrato)
    print(f"\n Saldo:\t\t R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Digite O CPF (somente números): ")
    usuario = filtar_usuario(cpf,usuarios)

    if usuario:
        print("\n Já existe cadastro com esse CPF!")
        return
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digitr o endereço (logradouro, n - bairro- cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento,"cpf":cpf, "endereco":endereco})
    print("Usuário cadastrado com sucesso!")

def filtar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input ("Digite o CPF do usuário: ")
    usuario = filtar_usuario(cpf,usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}

    print("\n Usuário não encontrado!")
    

def listar_contas(contas):
    for conta in contas:
        linha = f""" \
            Agência:\t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['none']}
            """
        print("="*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES=3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    numero_saques= 0
    extrato =""
    usuarios= []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == "1":
            print("Depositar")
            valor = float (input("Qual valor deseja depoistar?" ))
            saldo , extrato = depositar(saldo, valor,extrato)

        elif opcao == "2":
            print("Sacar")
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            print("\n-------------EXTRATO--------------")
            print("Não foram realizadas monimentações" if not extrato else extrato)
            print(f"Saldo da conta R${saldo:.2f}\n")
            print("\n----------------------------------")
        
        elif opcao == "4":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao== "6":
            criar_usuario(usuarios)

        elif opcao =="7":
            break

        else:
            print("Operação inválida, por avor selecione novamente a opção desejada")



main()

