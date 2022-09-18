from dataclasses import dataclass

@dataclass
class Menu:
    opcao_menu:int
    discricao_menu:str

def abre_menu()->list:

    lista_final = []

    with open("asset/arquivo_menu.txt","r") as arquivo2:
        linhas = arquivo2.readlines()
        for linha in linhas:
            linha = linha.replace('\n',"")
            campos=linha.split(';')
            tratamento_final = Menu(int(campos[0]), campos[1])

            lista_final.append(tratamento_final)

    return lista_final   





    
    
    
    
        
        




