from datetime import timedelta

def quant_domingos(primeira_data,segunda_data):
    quant_domingos = 0
    resultado_dias = segunda_data-primeira_data

    for dia in range(resultado_dias.days+1):
        cada_dia = primeira_data + timedelta(days=dia)
        if cada_dia.weekday() == 6:
            quant_domingos+=1

    return quant_domingos 

      











