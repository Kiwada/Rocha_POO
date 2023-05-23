from QuestãoFATURA import Fatura


fatura = Fatura(1, "Livros de programacao", 4, 80.00)

print("Total da fatura = ",fatura.calcular_valor_fatura())