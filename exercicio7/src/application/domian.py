def procura_numero_na_lista_sequencial(lista_de_numeros:list,numero_entrada:int):
    numero_na_lista = 0
    for numero in lista_de_numeros:
        if numero == numero_entrada:
            numero_na_lista+=1
    if numero_na_lista == 1 :
        print(f"O numero {numero_entrada} está na lista")
    else:
        print(f"O numero {numero_entrada} não está na lista")



    

    


