from random import randint

class Produto:
    def __init__(self , codigo , nome , preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self._estoque = 20


        @property
        def codigo (self):
            return self.codigo
        
        @property
        def preco(self):
            return self.preco
        
        @property
        def estoque(self):
            return self.__estoque
        
        @codigo.setter
        def codigo (self , valor ):
            if isinstance(valor , int):
                self._codigo = valor

        @nome.setter
        def nome(self , valor):
            if isinstance (valor , str):
                self._nome = valor

        @preco.setter
        def nome(self , valor):
            if isinstance (valor , str):
                self._preco = valor

        @estoque.setter
        def estoque(self , valor):
            if isinstance (valor , int):
                self.__estoque = valor

        @classmethod
        def get_ano(cls):
            return cls.ano
        

        @classmethod
        def set_ano(cls , valor):
            cls.ano = valor
    
        
        @staticmethod
        def gerar_codigo():
            cod = randint(100,999)
            return cod
        

if  __name__ == " __main__ ":
       p1 = Produto(Produto.gerar_codigo(), "mouse " , 30)
       print(p1.nome , p1.estoque)
       p1.__estoque = 5
       print(p1.nome , p1 ._Produto__estoque)
       print(p1.__dict__)    
          
