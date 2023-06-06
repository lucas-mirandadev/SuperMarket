print('Seja bem-vindo ao Supermercado!')
print('Esta é a nossa lista de produtos, sinta-se à vontade para escolher!')
produtos = [
    {"codigo": 1, "produto": "Arroz", "preco": 5.99},
    {"codigo": 2, "produto": "Feijão", "preco": 3.49},
    {"codigo": 3, "produto": "Macarrão", "preco": 2.99},
    {"codigo": 4, "produto": "Leite", "preco": 3.29},
    {"codigo": 5, "produto": "Café", "preco": 7.99},
    {"codigo": 6, "produto": "Açúcar", "preco": 2.79},
    {"codigo": 7, "produto": "Sal", "preco": 1.49},
    {"codigo": 8, "produto": "Pão", "preco": 4.99},
    {"codigo": 9, "produto": "Manteiga", "preco": 5.49},
    {"codigo": 10, "produto": "Biscoito", "preco": 2.19}
]

# Exibir cabeçalho da tabela
def exibir_tabela_produtos():
    print("Código | Produto   | Preço")
    print("---------------------------")
    for produto in produtos:
        print(f"{produto['codigo']:6} | {produto['produto']:<9} | R${produto['preco']:5.2f}")

carrinho = {}

while True:
    print("Selecione uma opção:")
    print("1. Adicionar produto ao carrinho")
    print("2. Remover produto do carrinho")
    print("3. Visualizar carrinho")
    print("4. Finalizar compra")
    print("5. Sair")

    opcao = input("Opção selecionada: ")

    if opcao == '1':
        exibir_tabela_produtos()
        produto_selecionado = int(input("Selecione um produto: "))
        produto_encontrado = False
        for produto in produtos:
            if produto["codigo"] == produto_selecionado:
                quantidade = int(input("Quantidade: "))
                produto_nome = produto["produto"]
                carrinho[produto_nome] = carrinho.get(produto_nome, 0) + quantidade
                print("Produto adicionado ao carrinho.")
                produto_encontrado = True
                break

        if not produto_encontrado:
            print("Produto não encontrado.")

    elif opcao == '2':
        if len(carrinho) > 0:
            print("Produtos no carrinho:")
            for produto, quantidade in carrinho.items():
                print(f"{produto}: {quantidade}")

            produto_remover = input("Selecione um produto para remover: ")
            if produto_remover in carrinho:
                del carrinho[produto_remover]
                print("Produto removido do carrinho.")
            else:
                print("Produto não encontrado no carrinho.")
        else:
            print("O carrinho está vazio.")

    elif opcao == '3':
        if len(carrinho) > 0:
            print("Produtos no carrinho:")
            for produto, quantidade in carrinho.items():
                print(f"{produto}: {quantidade}")
        else:
            print("O carrinho está vazio.")

    elif opcao == '4':
        if len(carrinho) > 0:
            total = 0.0
            print("Produtos no carrinho:")
            for produto, quantidade in carrinho.items():
                for p in produtos:
                    if p["produto"] == produto:
                        preco = p["preco"]
                        break
                valor_total_produto = quantidade * preco
                total += valor_total_produto
                print(f"{produto}: {quantidade} x R${preco:.2f} = R${valor_total_produto:.2f}")

            print(f"Total da compra: R${total:.2f}")
            print("Compra finalizada. Obrigado!")
            break
        else:
            print("O carrinho está vazio.")

    elif opcao == '5':
        print("Até mais! Volte sempre!")
        break

    else:
        print("Opção inválida. Tente novamente.")
