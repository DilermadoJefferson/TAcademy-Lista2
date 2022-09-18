from src.application.input import pega_numero
from src.application.negocio import guarda_numero
from src.application.output  import mostra_resultado



if (__name__ == '__main__'):

    numero = pega_numero()
    lista = guarda_numero(numero)
    mostra_resultado(lista)
    


