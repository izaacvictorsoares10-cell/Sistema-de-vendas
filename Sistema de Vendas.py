estoque = {
    1: {"nome": "𝙲𝚑𝚊𝚟𝚎 𝚂𝚒𝚖𝚙𝚕𝚎𝚜", "quantidade": 5, "valor": 950},
    2: {"nome": "𝙵𝚛𝚊𝚐𝚖𝚎𝚗𝚝𝚘 𝚍𝚎 𝙼𝚊𝚜𝚌𝚊𝚛𝚊", "quantidade": 5, "valor": 15000},
    3: {"nome": "𝙵𝚛𝚊𝚐𝚖𝚎𝚗𝚝𝚘 𝚍𝚎 𝚅𝚊𝚜𝚘", "quantidade": 2, "valor": 1450},
    4: {"nome": "𝙼𝚎𝚜𝚝𝚛𝚎 𝚍𝚊 𝙲𝚘𝚛𝚛𝚒𝚍𝚊", "quantidade": 1, "valor": 1000},
    5: {"nome": "𝙲𝚑𝚊𝚟𝚎 𝙴𝚕𝚎𝚐𝚊𝚗𝚝𝚎", "quantidade": 2, "valor": 5000},
    6: {"nome": "𝙾𝚟𝚘 𝚁𝚊𝚗𝚌𝚘𝚜𝚘", "quantidade": 10, "valor": 100}
}
carrinho = {}
def mostrar_menu():
    print("\n𝙿𝙰𝚃𝙰𝙼𝙰𝚂𝚃𝙸𝙰 - Loja do Sly")
    print("[1] Visualizar Estoque")
    print("[2] Adicionar Item ao Carrinho")
    print("[3] Visualizar Carrinho")
    print("[4] Finalizar Compra")
    print("[0] Sair")
def mostrar_estoque():
    print("\nID | ITEM | PREÇO | ESTOQUE")
    for id_produto, item in estoque.items():
        print(f"{id_produto} | {item['nome']} | R${item['valor']:.2f} | {item['quantidade']}")
def adicionar_carrinho():
    id_produto = input("ID do item: ")
    quantidade = input("Quantidade: ")
    if id_produto == "" or quantidade == "":
        print("Entrada inválida!")
        return
    id_produto = int(id_produto)
    quantidade = int(quantidade)
    if id_produto not in estoque:
        print("Item inexistente!")
    elif quantidade <= 0:
        print("Quantidade inválida!")
    elif quantidade > estoque[id_produto]["quantidade"]:
        print("Estoque insuficiente!")
    else:
        if id_produto in carrinho:
            carrinho[id_produto]["quantidade"] += quantidade
        else:
            carrinho[id_produto] = {
                "nome": estoque[id_produto]["nome"],
                "valor": estoque[id_produto]["valor"],
                "quantidade": quantidade
            }
        estoque[id_produto]["quantidade"] -= quantidade
        print("Item adicionado ao carrinho!")
def mostrar_carrinho():
    if carrinho == {}:
        print("Carrinho vazio!")
        return
    subtotal = 0
    print("\n--- CARRINHO ---")
    for item in carrinho.values():
        total = item["valor"] * item["quantidade"]
        subtotal += total
        print(f"{item['nome']} x{item['quantidade']} - R${total:.2f}")
    print(f"\nSubtotal: R${subtotal:.2f}")
def finalizar_compra():
    if carrinho == {}:
        print("Carrinho vazio!")
        return
    subtotal = 0
    for item in carrinho.values():
        subtotal += item["valor"] * item["quantidade"]
    cupom = input("Cupom (ENTER para ignorar): ").upper()
    desconto = 0
    match cupom:
        case "DEV10":
            desconto = subtotal * 0.10
        case "DEV20" if subtotal > 500:
            desconto = subtotal * 0.20
        case _:
            desconto = 0
    total = subtotal - desconto
    print(f"\nSubtotal: R${subtotal:.2f}")
    print(f"Desconto: R${desconto:.2f}")
    print(f"Total: R${total:.2f}")
    confirmar = input("Confirmar compra? (S/N): ")
    if confirmar == "S":
        carrinho.clear()
        print("Compra finalizada!")
    else:
        for id_item in carrinho:
            estoque[id_item]["quantidade"] += carrinho[id_item]["quantidade"]
        carrinho.clear()
        print("Compra cancelada!")
while True:
    mostrar_menu()
    escolha = input("Escolha: ")
    match escolha:
        case "1":
            mostrar_estoque()
        case "2":
            adicionar_carrinho()
        case "3":
            mostrar_carrinho()
        case "4":
            finalizar_compra()
        case "0":
            print("Até mais, aventureiro!")
            break
        case _:
            print("Opção inválida!")