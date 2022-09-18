
from src.application.config import lista_de_numeros
from src.application.domian import procura_numero_par_e_impar
from src.application.output import mostra_resposta


if __name__== "__main__":
            
    pares =procura_numero_par_e_impar(lista_de_numeros)
    mostra_resposta(pares,lista_de_numeros)