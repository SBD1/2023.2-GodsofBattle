# game.py

import psycopg2
from database import DataBase
from classes import *
import os
import sys



class Game:
    def __init__(self):
        self.connection = DataBase.create_connection()
        self.jogador = Jogador(-1, -1, -1, -1, -1, -1, -1)
        self.cursor = self.connection.cursor()


    def logo(self):
        print("\n " * 10)
        print("   ______                _     _                   _          _____                                                 _           ")
        print("  |  ____|              | |   (_)                 | |        / ____|                                               | |          ")
        print("  | |__      ___   ___  | |_   _  __   __   __ _  | |       | (___     __ _   _ __     __ _   _ __    ___   _ __   | |_    ___  ")
        print("  |  __|    / _ \ / __| | __| | | \ \ / /  / _` | | |        \___ \   / _` | | '_ \   / _` | | '__|  / _ \ | '_ \  | __|  / _ \ ")
        print("  | |      |  __/ \__ \ | |_  | |  \ V /  | (_| | | |        ____) | | (_| | | | | | | (_| | | |    |  __/ | | | | | |_  | (_) |")
        print("  |_|       \___| |___/  \__| |_|   \_/    \__,_| |_|       |_____/   \__,_| |_| |_|  \__, | |_|     \___| |_| |_|  \__|  \___/ ")
        print("                                                                                       __/ |                                    ")
        print("                                                                                      |___/                                     ")
        print("\n ")

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

        print(f"Bem-vindo ao jogo, Jogador seu id é: {self.jogador_id}!\n")

        missao = DataBase.get_missao_details(self.connection, 1)
        id_adversario = missao[4]  
        detalhes_adversario = DataBase.get_adversario_details(self.connection, id_adversario)
        print(f"Você recebeu uma nova missão: {missao[1]}\n")
        DataBase.att_missao_ativa(self.connection, missao[0], self.jogador_id)

        print("Sua inscrição no festival foi bem sucedida e sua primeira batalha já ira começar!\n")
        print("Você vai em direção da nova estrutura chamativa construida no meio do distrito de barro.\n")

        arena_pebleus = Arena(self.jogador_id, [detalhes_adversario], self.connection)
        arena_pebleus.iniciar_desafio()

if __name__ == "__main__":
    game_instance = Game()  
    game_instance.logo()
    game_instance.apresentacao()

    escolha = input(">> ")

    if escolha == "1":
        game_instance.iniciar_jogo()
    elif escolha == "2":
        print("Carregando Jogo... (funcionalidade ainda não implementada)\n")
    elif escolha == "3":
        print("Ajuda... (funcionalidade ainda não implementada)\n")
    elif escolha == "4":
        print("Saindo do Jogo...\n")
    else:
        print("Opção inválida. Saindo do Jogo...")
