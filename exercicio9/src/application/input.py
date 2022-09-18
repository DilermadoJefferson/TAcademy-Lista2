def solicita_numero():
    while True:
        try:
            numero_entrada = int(input("Digite o numero que deseja pesquisar"))
            break
        except:
            print("Por favor digite um numero")
            
    return numero_entrada


