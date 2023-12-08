import psycopg2
import pandas as pd
import random

class DataBase:
    @staticmethod
    def create_connection():
        connect = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres")
        return connect

    @staticmethod
    def execute_query(connection, query, params=None, fetchone=False, fetchall=False):
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            if fetchone:
                return cursor.fetchone()
            elif fetchall:
                return cursor.fetchall()
            else:
                connection.commit()

    @staticmethod
    def create_new_player(connection):
        query = "INSERT INTO Jogador (Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (%s, %s, %s, %s, %s, %s) RETURNING Id_Jogador;"
        # Remova o valor para Id_Jogador, pois ele será gerado automaticamente
        params = (100, 20, 10, 5, 1, 1)

        # Execute a consulta e obtenha o ID do jogador recém-criado
        player_id = DataBase.execute_query(connection, query, params, fetchone=True)
        return player_id[0]  # Retorna o ID do jogador

    @staticmethod
    def get_player_details(connection, player_id):
        query = "SELECT * FROM Jogador WHERE Id_Jogador = %s;"
        params = (player_id,)
        return DataBase.execute_query(connection, query, params, fetchone=True)

    @staticmethod
    def get_missao_details(connection, missao_id):
        query = "SELECT * FROM Missao WHERE Id_Missao = %s;"
        params = (missao_id,)
        return DataBase.execute_query(connection, query, params, fetchone=True)

    @staticmethod
    def get_adversario_details(connection, adversario_id):
        # Lógica para obter detalhes do adversário com base no ID
        # Substitua isso pela lógica real de consulta ao banco de dados
        query = f"SELECT * FROM Adversario WHERE Id_Adversario = {adversario_id}"
        cursor = connection.cursor()
        cursor.execute(query)
        detalhes_adversario = cursor.fetchone()
        return detalhes_adversario
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


    