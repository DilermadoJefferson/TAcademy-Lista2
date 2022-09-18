
def calcula_intervalo_de_numeros(numero_entrada:int):

    contador_numeros_primos = 0
    n_primos = []
    numero_verificado = 2
    while (contador_numeros_primos < numero_entrada):
        resultado = [1 if numero_verificado % i == 0 else 0 for i in range(2, int(numero_verificado/2)+1) ]
        if (sum(resultado) == 0):
            n_primos.append(numero_verificado)
            contador_numeros_primos+=1

        numero_verificado += 1

    return n_primos        

     



