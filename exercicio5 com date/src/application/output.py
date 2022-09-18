def saida_de_resultado(primeira_data,segunda_data,quant_domingos):
    print(f'O periodo escolhido é de {primeira_data.strftime("%d ,%b %Y")} até {segunda_data.strftime("%d ,%b %Y")}.')
    print(f"Neste intervalo de datas temos {quant_domingos} domingos ")