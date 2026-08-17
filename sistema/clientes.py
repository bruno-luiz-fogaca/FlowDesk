def cadastrar_clientes(lista):
    print("Opção 1 Escolhida (Cadastrar Clientes)")
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))

    cliente = {
        "nome": nome,
        "idade": idade
    }

    lista.append(cliente)
    print("Cliente Cadastrado com Sucesso")

def excluir_clientes(lista):
    print("Opção 2 Escolhida (Excluir Clientes)")
    nome = str(input("Digite o nome do cliente que deseja excluir: "))

    for cliente in lista:
        if cliente["nome"].lower() == nome.lower():
            lista.remove(cliente)
            print("Excluído com Sucesso")
            return
        
    print("Cliente Não Encontrado")
    