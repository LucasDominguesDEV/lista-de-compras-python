import os

lista_compras = []

while True:
    os.system('cls')

    opcao = input(
        "Selecione uma opção:\n"
        "1- inserir item\n"
        "2- apagar item\n"
        "3- listar itens\n"
        "4- sair\n"
        "Opção: "
    )

    if opcao == "1":
        os.system('cls')
        print("--- LISTA DE COMPRAS ---")
        for indice, valor in enumerate(lista_compras):
            print(f"{indice} - {valor}")

        item = input("\nDigite o produto que deseja inserir: ")
        lista_compras.append(item)
        print("\nProduto adicionado com sucesso.")
        input("\nPressione ENTER para continuar...")

    elif opcao == "2":
        os.system('cls')
        if not lista_compras:
            print("A lista está vazia. Nada para apagar.")
            input("\nPressione ENTER para continuar...")
            continue

        print("--- LISTA DE COMPRAS ---")
        for indice, valor in enumerate(lista_compras):
            print(f"{indice} - {valor}")

        try:
            indice_apagar = int(input("\nDigite o índice do produto que deseja apagar: "))
            lista_compras.pop(indice_apagar)
            print("\nProduto removido com sucesso.")
        except ValueError:
            print("\nErro: digite apenas números.")
        except IndexError:
            print("\nErro: índice não existe na lista.")

        input("\nPressione ENTER para continuar...")

    elif opcao == "3":
        os.system('cls')
        print("--- LISTA DE COMPRAS ---")
        if not lista_compras:
            print("A lista está vazia.")
        else:
            for indice, valor in enumerate(lista_compras):
                print(f"{indice} - {valor}")

        input("\nPressione ENTER para continuar...")

    elif opcao == "4":
        os.system('cls')
        print("Programa encerrado.")
        break

    else:
        print("\nOpção inválida.")
        input("\nPressione ENTER para continuar...")
