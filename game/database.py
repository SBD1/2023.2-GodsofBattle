import psycopg2
import pandas as pd
from classes import *
import random

class DataBase():
    def create_connection():
        connect = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres")
        return connect
    
    def create_new_player(connection):
        cursor = connection.cursor()

        query = """
            INSERT INTO Jogador (Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao)
            VALUES (100, 20, 10, 5, 1, 1)
            RETURNING Id_Jogador;
        """

        # Utilizando RETURNING Id_Jogador para obter o ID do jogador recém-inserido
        cursor.execute(query)
        Id_Jogador = cursor.fetchone()[0]

        connection.commit()
        cursor.close()

        return Id_Jogador

    def create_new_inventory(connection, Id_Jogador):
        cursor = connection.cursor()

        query = """
            INSERT INTO Inventario (Capacidade, Id_Jogador)
            VALUES (50, %s)
            RETURNING Id_Inventario;
        """

      
        cursor.execute(query, (Id_Jogador,))
        inventory_id = cursor.fetchone()[0]

        connection.commit()
        cursor.close()

        return inventory_id

#Testando a classe de criar jogador já com o inventário acoplado.

    
    # def create_new_player(connection):
    #     cursor = connection.cursor()

    #     player_query = """
    #         INSERT INTO Jogador (Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao)
    #         VALUES (100, 20, 10, 5, 1, 1)
    #         RETURNING Id_Jogador;
    #     """
    #     cursor.execute(player_query)
    #     Id_Jogador = cursor.fetchone()[0]

    #     inventory_query = """
    #         INSERT INTO Inventario (Capacidade, Id_Jogador)
    #         VALUES (50, %s)
    #         RETURNING Id_Inventario;
    #     """
    #     cursor.execute(inventory_query, (Id_Jogador,))
    #     inventory_id = cursor.fetchone()[0]

    #     connection.commit()
    #     cursor.close()

    #     return Id_Jogador, inventory_id


    