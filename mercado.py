"""
Descrição:
Devemos desenvolver uma aplicação onde ao ser inicializada apresente ao usuárioummenuonde seja
possível cadastrar, listar e comprar produtos, além de visualizar carrinho de compraousairdaaplicação.
Ao adicionar um produto no carrinho de compras, deve-se verificar se já existeummesmoproduto no carrinho,
bastando alterar a quantidade. Ao finalizar a compra deve ser
apresentado ao usuário o total de acordo comos produtosequantidades inseridas no carrinho de compra.

Funções a adicionar:
    Verificar mesmo sendo maiusculo ou minusculo com o upper()
    Adicionar valores aos produtos


"""
from Classes.produto import Produto

def main():
    saida = 0
    prod = Produto()
    print("\nBem vindo ao sistema do mercado!---\n")
    while saida !=6:
        print("\nSelecione uma das opções: ")
        try:
            escolha = int(input("1-Cadastrar produtos\n2-Listar produtos\n3-Comprar produtos\n4-Visualizar carrinho\n5-Fechar pedido\n6-Sair do sistema"))


            if escolha == 1:  # cadastrar produtos
                prod.cadastro()
            elif escolha == 2:  # Listar produtos
                prod.listar()
            elif escolha == 3:  # comprar produtos
                prod.comprar()
            elif escolha == 4:  # visualizar carrinho
                prod.visualiza_carrinho()
            elif escolha == 5:  # fechar pedido
                prod.fechar()
                saida = 6
            elif escolha == 6:  # sair
                saida = 6
                print("Obrigado por nos escolher volte sempre!")
        except:
            print("Errou a entrada!! Tente novamente")




if __name__ == "__main__":
    main()
