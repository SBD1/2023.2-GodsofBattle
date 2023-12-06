# game.py

import psycopg2
from database import DataBase
from classes import *


class Game:
    def __init__(self):
        self.connection = DataBase.create_connection()
        self.jogador = Jogador(-1, -1, -1, -1, -1, -1, -1)

    @staticmethod
    def apresentacao():
        print("Em um reino próspero e rico, o rei decide celebrar um festival grandioso para encontrar um pretendente digno para sua adorável filha, a princesa Isabella.")
        print("No coração da cidade, uma arena majestosa é construída para duelos emocionantes entre corajosos guerreiros")
        print("Você, josivaldo, um jovem camponês que ajuda seus pais em uma plantação de batatas nos arredores da cidade, fica sabendo do festival e decide se inscrever!")
        print("\nEscolha uma opção:")
        print("1 - Iniciar Jogo")
        print("2 - Carregar Jogo")
        print("3 - Ajuda")
        print("4 - Sair")

    def iniciar_jogo(self):
        print("Iniciando o jogo...\n")

        self.jogador_id = DataBase.create_new_player(self.connection)

        print(f"Bem-vindo ao jogo, Jogador {self.jogador_id}!\n")
        arena_pebleus = Arena(self.jogador, adversarios_pebleus, treinadores_pebleus)
        arena_pebleus.iniciar_desafio()
        
    def exibir_status_jogador(self):
        jogador_details = DataBase.get_player_details(self.connection, self.jogador_id)
        if jogador_details:
            print(f"Detalhes do Jogador:\n{jogador_details}")
        else:
            print("Erro ao obter detalhes do jogador.")        

if __name__ == "__main__":
    game_instance = Game()  # Crie uma instância da classe Game
    game_instance.apresentacao()
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        game_instance.iniciar_jogo()
        game_instance.exibir_status_jogador()
    elif escolha == "2":
        print("Carregando Jogo... (funcionalidade ainda não implementada)")
    elif escolha == "3":
        print("Ajuda... (funcionalidade ainda não implementada)")
    elif escolha == "4":
        print("Saindo do Jogo...")
    else:
        print("Opção inválida. Saindo do Jogo...")
