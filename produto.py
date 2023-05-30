from random import randint


class Produto:
    def __init__(self , codigo , nome , preco , estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


        def get_codigo(self):
               return self.codigo

        def get_name(self):
               return self.name

     
        def get_nome(self):
               return self.estoque

        @preco.setter
        def get_preco(self, valor):
               if not isinstance(valor,float):
                    raise TypeError("valor invalido !")
                    return 
               self.preco = valor
          
        def set_nome(self , valor):
               self.nome = valor
          
     
        @classmethod
        def set_preco(cls , valor ):
                cls.ano = valor

        @staticmethod
        def gerar_codigo():
          cod = randint(100 , 999)
          return cod




produtos = []
produtos.append(Produto.gerar_codigo(),"Mouse", 20.0 , 10)
produtos.append(Produto.gerar_codigo(),"Teclado",60.0 , 15)
for produtos in produtos:
     print(p1.get_ano(), p1.get_nome(), p1.get_preco())
     print(p2.get_ano(), p2.get_nome(), p2.get_preco())