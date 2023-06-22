class Pessoa:
    def __init__(self, nome, fone, email):
        self.nome = nome
        self.fone = fone
        self.email = email

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Fone: {self.fone}")
        print(f"Email: {self.email}")


class Professor(Pessoa):
    def __init__(self, nome, fone, email, titulo):
        super().__init__(nome, fone, email)
        self.titulo = titulo

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Titulo: {self.titulo}")


class Estudante(Pessoa):
    def __init__(self, nome, fone, email, curso):
        super().__init__(nome, fone, email)
        self.curso = curso

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Curso: {self.curso}")


p1 = Pessoa("Ana", 123456, "ana@uespi.br")
p1.mostrar_dados()
prof1 = Professor("Ivo", 234567, "ivo@uespi.br", "Doutor")
prof1.mostrar_dados()
est1 = Estudante("Edu", 345678, "edu@uespi.br", "Computação")
est1.mostrar_dados()