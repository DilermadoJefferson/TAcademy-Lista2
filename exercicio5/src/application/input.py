def recebe_primeira_data():

    while True:
        primeira_data = input("Digite a primeira data: \nEx 00/00/0000\n")

        if len(primeira_data) > 10 or len(primeira_data ) < 8 or len(primeira_data ) == 9 : 
            print ('Por favor coloque a data como o exemplo')
        elif len(primeira_data) == 8:
            if not (int(primeira_data[:2]) in range(1,31)): print("Data digitada está errada")      
            elif not (int(primeira_data[2:4]) in range(1,12)):print("Mês digitado está errado")
            elif not (int(primeira_data[4:])) in range(0000,9999):print("Ano digitado está errad0")     
            else:
                segunda_data_tradada=primeira_data      
                return segunda_data_tradada


        elif ("-" in primeira_data) or ("/" in primeira_data):
            primeira_data_tradada = primeira_data.replace("-","").replace("/","")
            if len(primeira_data_tradada) == 8:
                if not (int(primeira_data_tradada[:2]) in range(1,31)): print("Data digitada está errada")      
                elif not (int(primeira_data_tradada[2:4]) in range(1,12)):print("Mês digitado está errado")
                elif not (int(primeira_data_tradada[4:])) in range(0000,9999):print("Ano digitado está errado")  

                return primeira_data_tradada


def recebe_Segunda_data():

    while True:
        segunda_data = input("Digite a segunda data: \nEx 00/00/0000\n")
        

        if len(segunda_data) > 10 or len(segunda_data ) < 8 or len(segunda_data ) == 9 : 
            print ('Por favor coloque a data como o exemplo')
        elif len(segunda_data) == 8:
            if not (int(segunda_data[:2]) in range(1,31)): print("Data digitada está errada")      
            elif not (int(segunda_data[2:4]) in range(1,12)):print("Mês digitado está errado")
            elif not (int(segunda_data[4:])) in range(0000,9999):print("Ano digitado está errado")     
            else:
                segunda_data_tradada=segunda_data       
                return segunda_data_tradada


        elif ("-" in segunda_data) or ("/" in segunda_data):
            segunda_data_tradada = segunda_data.replace("-","").replace("/","")
            if len(segunda_data_tradada) == 8:
                if not (int(segunda_data_tradada[:2]) in range(1,31)): print("Data digitada está errada")      
                elif not (int(segunda_data_tradada[2:4]) in range(1,12)):print("Mês digitado está errado")
                elif not (int(segunda_data_tradada[4:])) in range(0000,9999):print("Ano digitado está errado")  

                return segunda_data_tradada

 



