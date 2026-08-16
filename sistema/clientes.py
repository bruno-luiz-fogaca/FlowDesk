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
