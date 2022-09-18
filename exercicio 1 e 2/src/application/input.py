def entra_opcao(lista_final):
    valor_opcao_menu = []
    
    for linha in lista_final:
       linha = (linha.opcao_menu)
       valor_opcao_menu.append(linha)

    valor_opcao_menu.append(0)  

    while True:
        opcao = input('Digite Sua opção:  ')
        if not opcao.isdigit():
            print('Digite apenas numeros')

        else :
            if int(opcao) in valor_opcao_menu:
                print(f'opcao escolida: {opcao}')
                break

            else:
                print(f'Opcao escolida: {opcao}, e essa opcao é inválida \nTente novamente')    

    return opcao            
            


    




   