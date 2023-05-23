class Fatura:

    def __init__(self, num, nome, quantidade=0, preco_unitario=0):   #Definindo O Metodo Construtor e os Argumentos !
        self.numero = num   
        self.nome = nome
        if (quantidade < 0):
            quantidade = 0
        self.__quantidade = quantidade
        if (preco_unitario < 0):
            preco_unitario = 0
        self.__preco_unitario = preco_unitario