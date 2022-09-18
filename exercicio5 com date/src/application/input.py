from datetime import datetime
def pegar_primeira_data():
    while True:
        try:
            primeira_data = datetime.strptime(input('Digite a primeira data ex:dia/mês/ano \n'),'%d/%m/%Y')
            break
        except:
            print("Data digitada errada. \nPor favor digite no formato solicitado.")
    return(primeira_data)    

def pegar_segunda_data():
    while True:
        try:
            segunda_data = datetime.strptime(input('Digite a segunda data ex:dia/mês/ano \n'),'%d/%m/%Y')
            break
        except:
            print("Data digitada errada. \nPor favor digite no formato solicitado.")

    return(segunda_data)   


