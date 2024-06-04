import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova conta
    [l]\tListar contas
    [u]\tNovo usuário
    [sa]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print("\n--- Depósito realizado com sucesso! ---")
    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        if saldo >= valor:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n---- Saque realizado com sucesso! ----")
        else:
            print("\n*** Operação falhou! Você não tem saldo suficiente. ***")
    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n------- EXTRATO ================")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n*** Já existe usuário com esse CPF! ***")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n*** Usuário não encontrado, fluxo de criação de conta encerrado! ***")


def listar_contas(contas):
    for conta in contas:
        print(f"\n------------------------------------------------------")
        print(f"Agência: {conta['agencia']} - C/C: {conta['numero_conta']} - Titular: {conta['usuario']['nome']}")
        print(f"------------------------------------------------------")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "n":
            conta = criar_conta(AGENCIA, len(contas) + 1, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "sa":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()