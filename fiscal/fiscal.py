from datetime import date
from random import randint
from produto import produto

class NotaFiscal:

    def __init__(self) :
        self.numero = randint(1000 , 9999)
        self.data = date.today()
        self.total = 0.00
        self.produtos = []
    

    def  inserir_produtos(self , produto):
        self.produtos.append(produto)

    
    def mostra_produtos(self):
        print(" ==========================  ")
        print("COD ITEM      PREÇO")
        for  produto in self.produtos:
            print(f"Codigo..: {produto.codigo}" , end= " ")
            print(f"Nome..: {produto.nome}" , end= " ")
            print(" " (* 10 - len(*produto.nome)))
            print(f"{produto.preco:5.1f}")

        print(" ==========================  ")
    

    def calculcular_total(self):
       total = 0.00
       for produto in self.produtos:
          total += produto.preco
          self.total = total


nf = NotaFiscal()
print(nf.numero , nf.data , nf.total , nf.produtos)
nf.inserir_produtos(produto(produto.ferar_codigo(), "mouse" , 30.00))



    
       