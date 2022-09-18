from math import ceil


def procura_numero_na_lista_binaria(lista_de_numeros:list,numero_entrada:int):
    while True:
        if numero_entrada in lista_de_numeros[:ceil(len(lista_de_numeros)/2)]:
            print(f"O numero {numero_entrada} está na lista")
            break

        elif numero_entrada in lista_de_numeros[ceil(len(lista_de_numeros)/2):]:
            print(f"O numero {numero_entrada} está na lista")
            break

        else:
            print("O numero não está na lista")
            break


        


    
    


