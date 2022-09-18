from src.application.domian import transformando_arquivo_json_em_classe
from src.application.output import mostra_resultado

if __name__== "__main__":
            
    arquivo_tratado = transformando_arquivo_json_em_classe()
    mostra_resultado(arquivo_tratado)