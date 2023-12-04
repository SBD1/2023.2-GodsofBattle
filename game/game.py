# game.py

import psycopg2

from classes import Mundo, Regiao, Local, Jogador, Adversario, Mercador, Treinador, Inventario, InstanciaItem

def apresentacao():
    print("Em um reino próspero e rico, o rei decide celebrar um festival grandioso para encontrar um pretendente digno para sua adorável filha, a princesa Isabella.")
    print("No coração da cidade, uma arena majestosa é construída para duelos emocionantes entre corajosos guerreiros. Pronto para encarar o desafio?")
    print("\nEscolha uma opção:")
    print("1 - Iniciar Jogo")
    print("2 - Carregar Jogo")
    print("3 - Ajuda")
    print("4 - Sair")

def iniciar_jogo():
    print("Iniciando o jogo...\n")

    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )

    cursor = conn.cursor()

    # Exemplo de consulta para obter informações do jogador
    cursor.execute("SELECT id_jogador, nome, vida, ataque, resistencia, habilidade, missao_ativa FROM Jogador WHERE id_jogador = 1")
    dados_jogador = cursor.fetchone()

    # Criar instância do jogador com base nos dados do banco de dados
    jogador_principal = Jogador(*dados_jogador)

    # Fechar a conexão com o banco de dados
    conn.close()

    # Retornar a instância do jogador para que ela possa ser usada no jogo
    return jogador_principal

if __name__ == "__main__":
    apresentacao()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        jogador_principal = iniciar_jogo()
        # Agora você pode usar jogador_principal em outras partes do seu código
        print(f"{jogador_principal.nome}, você está no {local_inicial.descricao}.")
    elif escolha == "2":
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )
    
        cursor = conn.cursor()
    
        cursor.execute("SELECT Nome FROM Mundo")

        dado = cursor.fetchone()
        print(dado)
        ##print("Carregando Jogo... (funcionalidade ainda não implementada)")
    elif escolha == "3":
        print("Ajuda... (funcionalidade ainda não implementada)")
    elif escolha == "4":
        print("Saindo do Jogo...")
    else:
        print("Opção inválida. Saindo do Jogo...")
