from src.application.domain import abre_menu
from src.application.input import entra_opcao
from src.application.output import mostra_menu


if __name__ == '__main__':
    lista_final = abre_menu()
    mostra_menu(lista_final)
    opcao = entra_opcao(lista_final)
    
