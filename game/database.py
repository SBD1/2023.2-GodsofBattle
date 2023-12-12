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
        params = (100, 20, 1, 5, 1, 1)

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
    def att_missao_ativa(connection, missao_id, jogador_id):
        query = "UPDATE Jogador SET Id_Missao = %s WHERE Id_Jogador = %s;"
        params = (missao_id, jogador_id)
        DataBase.execute_query(connection, query, params)

    @staticmethod
    def missao_concluida(connection, jogador_id):
        query = "UPDATE Jogador SET Id_Missao = (SELECT Id_Missao FROM Missao WHERE Id_MissaoRequisito = Jogador.Id_Missao) WHERE Id_Jogador = %s;"
        params = (jogador_id,)
        DataBase.execute_query(connection, query, params)

    def upar_jogador(connection, jogador_id):
         # Obtenha os detalhes do jogador
        jogador_detalhes = DataBase.get_player_details(connection, jogador_id)
        vida_jogador = jogador_detalhes[1]
        ataque_jogador = jogador_detalhes[2]
        res_jogador = jogador_detalhes[3]

         # Calcule o novo valor de vida, ataque e resistência
        novo_vida = vida_jogador + 10
        novo_ataque = ataque_jogador + 5
        novo_res = res_jogador + 1

         # Atualize os valores de vida, ataque e resistência do jogador
        query = "UPDATE Jogador SET Vida = %s, Ataque = %s, Resistencia = %s WHERE Id_Jogador = %s;"
        params = (novo_vida, novo_ataque, novo_res, jogador_id)
        DataBase.execute_query(connection, query, params)


    @staticmethod
    def treinar_com_mestre(connection, jogador_id, custo_treinamento):
        # Verifique se o jogador tem moedas suficientes para treinar
        jogador_detalhes = DataBase.get_player_details(connection, jogador_id)
        moedas_jogador = jogador_detalhes[6]  # Assumindo que o número de moedas está na posição 6, ajuste conforme necessário

        if moedas_jogador >= custo_treinamento:
            # Atualize o número de moedas do jogador após o treinamento
            novo_saldo_moedas = moedas_jogador - custo_treinamento
            query = "UPDATE Jogador SET Moedas = %s WHERE Id_Jogador = %s;"
            params = (novo_saldo_moedas, jogador_id)
            DataBase.execute_query(connection, query, params)
            return True  # Indica que o treinamento foi bem-sucedido
        else:
            return False  # Indica que o jogador não tem moedas suficientes para treinar

    
    @staticmethod
    def get_adversario_atual(connection, jogador_id):
        query = "SELECT Id_Adversario FROM Missao WHERE Id_Missao = (SELECT Id_Missao FROM Jogador WHERE Id_Jogador = %s) ;"
        params = (jogador_id,)
        adversario_id = DataBase.execute_query(connection, query, params, fetchone=True)
        return adversario_id[0] if adversario_id else None

    @staticmethod
    def get_adversario_details(connection, adversario_id):
        # Lógica para obter detalhes do adversário com base no ID
        query = f"SELECT * FROM Adversario WHERE Id_Adversario = {adversario_id}"
        cursor = connection.cursor()
        cursor.execute(query)
        detalhes_adversario = cursor.fetchone()
        return detalhes_adversario

    @staticmethod
    def get_arena_details(connection, arena_id):
        # Lógica para obter detalhes da arena com base no ID
        query = f"SELECT Descricao FROM Local WHERE Id_Local = {arena_id}"
        cursor = connection.cursor()
        cursor.execute(query)
        detalhes_arena = cursor.fetchone()
        print(f"{detalhes_arena[0]}")


    @staticmethod
    def escolher_adversario_missao(connection):
        from classes import Adversario
       
        missao = DataBase.get_missao_details(connection, 1)
        id_adversario = missao[4]
        detalhes_adversario = DataBase.get_adversario_details(connection, id_adversario)

        # Certifique-se de que a estrutura da tabela Adversario está correta
        if detalhes_adversario:
            id_adversario = detalhes_adversario[0]
            vida = detalhes_adversario[1]
            ataque = detalhes_adversario[2]
            resistencia = detalhes_adversario[3]
            descricao = detalhes_adversario[4]

            adversario = Adversario(id_adversario, vida, ataque, resistencia, descricao)
            return adversario

        return None

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


    