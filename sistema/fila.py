def chamar_proximo_cliente(lista):
    if len(lista) == 0:
        print("Não Há Cliente na Fila")
        return

    cliente = lista.pop(0)
    print("Chamando o Próximo Cliente")
    print(f"Cliente {cliente["nome"]} Chamado")
    
