from datetime import date
from random import randint
from produto import Produto

class NotaFiscal:

    def __init__(self) :
        self.numero = randint(1000 , 9999)
        self.data = date.today()
        self.total = 0.00
        self.produtos = []
    

    def  inserir_produtos(self , produto):
        self.produtos.append(produto)

    
    def mostrar_produtos(self):
        print("===================")
        print("COD ITEM      PREÇO")
        print("-------------------")
        for produto in self.produtos:
            print(f"{produto.codigo}", end=" ")
            print(f"{produto.nome}", end=" ")
            print(" " * (10 - len(produto.nome)), end="")
            print(f"{produto.preco:5.1f}")
        print("-------------------")
        self.calcular_total()
        print(f"TOTAL: R$ {self.total}")
        print("===================")

    def calcular_total(self):
        total = 0.00
        for produto in self.produtos:
            self.total += produto.preco
        self.total = total


if __name__ == "_main_":
    nf = NotaFiscal()
    print(nf.numero, nf.data, nf.total, nf.produtos)
    nf.inserir_produtos(Produto(Produto.gerar_codigo(), "mouse", 30.00))
    nf.inserir_produtos(Produto(Produto.gerar_codigo(), "teclado", 100.00))
    nf.inserir_produtos(Produto(Produto.gerar_codigo(), "ssd", 200.00))
    print(nf.numero, nf.data, nf.total)
    nf.mostrar_produtos()