from src.application.config import lista_de_numeros
from src.application.input import solicita_numero
from src.application.domian import procura_numero_na_lista_sequencial
from src.application.output import mostra_resultado

if __name__== "__main__":
            
    numero = solicita_numero()
    tem_numero=procura_numero_na_lista_sequencial(lista_de_numeros,numero)
    mostra_resultado(tem_numero,numero)
