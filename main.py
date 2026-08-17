from sistema import clientes
lista = []
def menu():
    while True:
        print("----------------------")
        print("BEM VINDO AO FLOW DESK")
        print("----------------------")
        print(" ")
        print("[1] Cadastrar Cliente")
        print("[2] Excluir Cliente")
        print("[3] Chamar Próximo Cliente")
        print("[4] Ver Lista de Cliente")
        print("[5] Sair")

        escolha = int(input("Opção: "))

        if escolha == 1:
            clientes.cadastrar_clientes(lista)

        if escolha == 2:
            clientes.excluir_clientes(lista)