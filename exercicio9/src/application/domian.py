def procura_numero_na_lista_sequencial(lista_de_numeros:list,numero_entrada:int): 
    numero_na_lista = 0
    tem_na_lista = [1 for numero in lista_de_numeros if numero == numero_entrada]
    if len(tem_na_lista) == 1:
        numero_na_lista+=1

    return numero_na_lista

    
            
    

    

    


