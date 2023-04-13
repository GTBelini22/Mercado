


class Produto:
    def __init__(self):
        self.__produtos: dict = {}
        self.__carrinho: dict = {}
        self.__valor: float = 0.0

    @property
    def produtos(self):
        return self.__produtos

    @property
    def carrinho(self):
        return self.__carrinho

    @property
    def valor(self):
        return self.__valor
    @produtos.setter
    def produtos(self, novo_valor):
        self.__produtos= novo_valor
    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    def cadastro(self):
        try:
            novo_cadasto= input("\nPor favor inserir novo produto: ")
            preco = float(input("Inserir Preço: "))
            if novo_cadasto not in self.__produtos:
                self.__produtos[novo_cadasto] =preco
            else:
                print("Produto já cadastrado!")
        except:
            print("Entrada invalida! Tente novamente")

    def listar(self):
        print("\nProdutos que já foram cadastrados")
        for i in self.__produtos:
            print(f"{i} - {self.__produtos[i]}")

    def comprar(self):
        try:
            nova_compra = input("\nQual produto desejaria comprar? ")
            if nova_compra in self.__produtos:
                if nova_compra in self.__carrinho:# Apenas colocando mais 1
                    self.carrinho[nova_compra]+=1
                    self.valor += self.produtos[nova_compra]
                else:#Adicionar no carrinho
                    self.carrinho[nova_compra]= 1
                    self.valor += self.produtos[nova_compra]
            else:
                print("Produto não econtrado!")
        except:
            print("Entrada invalida! Por favor tente novamente")

    def visualiza_carrinho(self):
        print("\n---Produtos já colocados no carrinho---")
        for i in self.__carrinho:
            print(f"{i} - {self.carrinho[i]}")
        print(f"Valor da compra: {self.valor}")

    def fechar(self):
        print("\nFechando a conta")
        for i in self.__carrinho:
            print(f"{i} - {self.carrinho[i]}")
        print(f"Valor a ser pago: {self.valor}")
        print("\nVolte sempre!!")







