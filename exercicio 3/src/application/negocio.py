def e_numero_primo(numero)->bool:
    if (numero == 2): return True
    if (numero % 2) == 0: return False

    metade = int(numero/2) + 1

    for i in range(3, metade+1):
        if((numero % i) == 0):
            return False

    return True
def guarda_numero (numero):
    contador_numeros_primos = 0
    n_primos = []
    numero_verificado = 2
    while (contador_numeros_primos < numero):

        if e_numero_primo(numero_verificado):
            n_primos.append(numero_verificado)
            contador_numeros_primos+=1

        numero_verificado += 1    
    return  n_primos