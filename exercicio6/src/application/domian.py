from dataclasses import dataclass
import json

@dataclass
class ArrumandoJson:
    nome : str
    classe : str
    age : int

def transformando_arquivo_json_em_classe():
    with open("asset/arquivo.json", encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)
        linha_arquivo = ArrumandoJson(dados["Name"],dados["Class"],dados["Age"])
    return linha_arquivo    
