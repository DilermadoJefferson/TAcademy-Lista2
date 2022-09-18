from src.application.input import recebe_primeira_data,recebe_Segunda_data
from src.application.output import saida
from src.application.domain import quant_domingos


if __name__== "__main__":
    while True:
        primeira_data = recebe_primeira_data()
        segunda_data=recebe_Segunda_data()
        if segunda_data < primeira_data:
            print('Aprimeira data e maior que a segunda\nTente novamente!')
        else: break    
        
    domingos=quant_domingos(primeira_data,segunda_data)
    saida(primeira_data,segunda_data,domingos)
    
