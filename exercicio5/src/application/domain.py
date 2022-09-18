from datetime import date,timedelta


def quant_domingos(primeira_data_tradada,segunda_data_tradada):
    quant_domingos = 0

    primeira_data = date(year=int(primeira_data_tradada[4:]), month=int(primeira_data_tradada[2:4]), day=int(primeira_data_tradada[:2]))
    segunda_data = date(year=int(segunda_data_tradada[4:]), month=int(segunda_data_tradada[2:4]), day=int(segunda_data_tradada[:2])) 
    resultado_dias = segunda_data-primeira_data

    for dia in range(resultado_dias.days):
        cada_dia = primeira_data + timedelta(days=dia)
        if cada_dia.weekday() == 6:
            quant_domingos+=1

    return quant_domingos 

      

    

    

    




#574





