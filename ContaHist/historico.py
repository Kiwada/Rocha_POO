from datetime import date

class Historico:

    @staticmethod
    def gerar_data():
        dia = date.today().day
        mes = date.today().month
        ano = date.today().year
        if dia < 10: dia = f"0{dia}"
        if mes < 10: mes = f"0{mes}"
        return f"{dia}/{mes}/{ano}"

    def __init__(self, valor, operacao):
        self.data = Historico.gerar_data()
        self.valor = valor
        self.operacao = operacao