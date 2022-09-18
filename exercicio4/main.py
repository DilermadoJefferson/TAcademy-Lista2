from src.application.input import pega_intervalo_de_numeros
from src.application.domain import calcula_intervalo_de_numeros
from src.application.output import mostra_resultado


if __name__=="__main__":
    range = pega_intervalo_de_numeros()
    primos = calcula_intervalo_de_numeros(range)
    mostra_resultado(primos)

