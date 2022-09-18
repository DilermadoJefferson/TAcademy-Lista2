from src.application.config import lista_de_numeros
from src.application.input import solicita_numero
from src.application.domian import procura_numero_na_lista_binaria

if __name__== "__main__":
            
    numero = solicita_numero()
    procura_numero_na_lista_binaria(lista_de_numeros,numero)