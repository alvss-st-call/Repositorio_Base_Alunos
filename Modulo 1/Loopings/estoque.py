print("--------------------------------")
print("!Sistema de Estoque de Produtos!")
print("--------------------------------")

produto = []

def cadastrar(produto):
    novo_produto = input("Digite o novo produto: ")
    produto.append(novo_produto)
    print(f"Produto{novo_produto} Adicionado com sucesso!")

def listar(produto):
    for i, produtos in enumerate(produto, start=1):
        print(f"{i}. {produtos}")
try:
    while True:
        print("----------------------")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produto")
        print("3 - Excluir produto")
        print("0 - sair")
        print("----------------------")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            cadastrar(produto)
        elif opcao == "2":
            listar(produto)
        elif opcao == "3":
            excluir_produto = input("Digite o nome do produto: ")
            produto.remove(excluir_produto)
            print(f"{excluir_produto} Excluido com sucesso")
        elif opcao == "0":
            break
except:
    print("Codigo invalido, TENTE novamente")
    
    
