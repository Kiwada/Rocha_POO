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
       

        @property
        def preco(self):
              return self.nome
        
        @preco.setter
        def preco(self):
              return self.preco
        
        @preco.setter
        def preco(self , valor):
              if not isinstance(valor , float):
                    raise TypeError("valor invalido !")
              self._preco = valor
        
        @classmethod
        def get_ano(cls):
              return cls.ano
        
        @classmethod
        def set_ano(cls,valor):
              cls.ano = valor

        
        @staticmethod
        def gerar_codigo():
              cod = randint(100,999)
              return cod
        

produtos = []
produtos.append(Produto.gerar_codigo(),"Mouse", 20.0 , 10)
produtos.append(Produto.gerar_codigo(),"Teclado",60.0 , 15)
for produtos in produtos:
   print(f"Codigo")
