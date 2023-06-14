from produto import Produto
from notafiscal  import NotaFiscal



if __name__ == " __main__ ":
     with open ("dados.txt " , " r") as file :
          linhas = [linha.strip() for linha in file if  linha.strip() ]
          file.close()


print(linhas)
for item in linhas :
      print(item)