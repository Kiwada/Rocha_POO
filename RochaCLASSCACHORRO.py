class Pet:
    def __init__(self, cor, idade, cpf):
        self.__cor = cor 
        self.__idade = idade 
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf   

    def get_cor(self, cor):     
        return self.__cor
    
    def set_cor(self, cor):
        self.__cor = cor

p1 = Pet("caramelo", 2, 123456)
print(f"P1: {p1.get_cpf()}")
p1.__cor = "branco"
print(f"P1: {p1.get_cor()}")