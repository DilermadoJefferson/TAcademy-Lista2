from src.application.input import pegar_primeira_data,pegar_segunda_data
from src.application.domain import quant_domingos
from src.application.output import saida_de_resultado
if __name__=="__main__":
    data_um = pegar_primeira_data()
    data_dois = pegar_segunda_data()
    domingos = quant_domingos(data_um,data_dois)
    saida_de_resultado(data_um,data_dois,domingos)



