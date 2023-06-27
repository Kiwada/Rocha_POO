from historico import Historico

class Conta:

    def __init__(self, numero : int, saldo : float, titular : str):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular
        self.historico = []

    def get_numero(self): return self.__numero

    def get_saldo(self): return self.__saldo

    def get_titular(self): return self.__titular

    def mostrar_saldo(self):
        print(f"Conta.........: {self.get_numero()}")
        print(f"Titular.......: {self.get_titular()}")
        print(f"Saldo em conta: R$ {self.get_saldo():.2f}")

    def depositar(self, valor):
        self.__saldo += valor
        self.gravar_historico(valor, "DE")

    def sacar(self, valor):
        if self.get_saldo() > valor:
            self.__saldo -= valor
            self.gravar_historico(-valor, "SA")
            return True
        return False

    def transferir(self, destino, valor):
        if self.get_saldo() > valor:
            self.__saldo -= valor
            destino.__saldo += valor
            self.gravar_historico(-valor, "TR")
            destino.gravar_historico(valor, "TR")
            return True
        return False

    def extrato(self):
        print(f"Conta....: {self.get_numero()}")
        print(f"Titular..: {self.get_titular()}")
        print("====================================")
        print(f"DATA           OP      VALOR (R$)")
        print("------------------------------------")
        for h in self.historico:
            print(f"{h.data}", end="")
            print(" " * (15 - len(h.data)), end="")
            print(f"{h.operacao}", end="")
            print(" " * (10 - len(h.operacao)), end="")
            print(f"{h.valor:8.2f}")
        print("====================================")
        print(f"Saldo atual (R$): {self.get_saldo():8.2f}")

    def gravar_historico(self, valor, operacao):
        self.historico.append(Historico(valor, operacao))
