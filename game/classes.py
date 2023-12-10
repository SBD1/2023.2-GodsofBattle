#classes.py

from database import DataBase
import random
import psycopg2

class InstanciaItem:
    def __init__(self, id_instancia_item, descricao, valor):
        self.id_instancia_item = id_instancia_item
        self.descricao = descricao
        self.valor = valor


class Mundo:
    def __init__(self, id_mundo, nome, historia):
        self.id_mundo = id_mundo
        self.nome = nome
        self.historia = historia
        self.regioes = []

    def adicionar_regiao(self, regiao):
        self.regioes.append(regiao)


class Regiao:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.locais = []

    def adicionar_local(self, local):
        self.locais.append(local)


class Local:
    def __init__(self, id_local, descricao):
        self.id_local = id_local
        self.descricao = descricao
        self.npcs = []

    def adicionar_npc(self, npc):
        self.npcs.append(npc)


class Jogador:
    def __str__(self):
        return f"Jogador {self.id_jogador}: Vida={self.vida}, Ataque={self.ataque}, Resistencia={self.resistencia}, Habilidade={self.habilidade}, Missao Ativa={self.missao_ativa}"

    def __init__(self, id_jogador, vida, ataque, resistencia, habilidade, moedas, missao_ativa=None):
        self.id_jogador = id_jogador
        self.vida = vida
        self.ataque = ataque
        self.resistencia = resistencia
        self.habilidade = habilidade
        self.missao_ativa = missao_ativa
        self.inventario = Inventario()
        self.moedas = moedas

    def adicionar_instancia_item(self, instancia_item):
        self.inventario.adicionar_instancia_item(instancia_item)

    def treinar_habilidade(self, habilidade):
        self.habilidade += 1  # Aumenta a habilidade do jogador
        print(f"Sua habilidade agora é {self.habilidade}.")
        pass

    def participar_batalha(self, adversario):
        # Lógica para a participação em batalhas
        pass

    def adicionar_instancia_item(self, instancia_item):
        # Lógica para adicionar uma instância de item ao inventário
        self.inventario.adicionar_instancia_item(instancia_item)


class Adversario:
    def __init__(self, id_adversario, vida, ataque, resistencia, descricao):
        self.id_adversario = id_adversario
        self.vida = vida
        self.ataque = ataque
        self.resistencia = resistencia
        self.descricao = descricao


class NPC:
    def __init__(self, nome, historia, descricao):
        self.nome = nome
        self.historia = historia
        self.descricao = descricao


class Mercador(NPC):
    def __init__(self, id_mercador, nome, historia, descricao, moedas):
        super().__init__(nome, historia, descricao)
        self.id_mercador = id_mercador
        self.moedas = moedas

    def vender_item(self, instancia_item, jogador):
        # Lógica para vender um item ao jogador
        jogador.adicionar_instancia_item(instancia_item)

class Missao:
    def __init__(self, id_missao, descricao_missao, status, id_adversario, id_missao_requisito=None):
        self.id_missao = id_missao
        self.descricao_missao = descricao_missao
        self.status = status
        self.id_adversario = id_adversario
        self.id_missao_requisito = id_missao_requisitoS
 

class Treinador(NPC):
    def __init__(self, id_treinador, nome, historia, descricao, moedas):
        super().__init__(nome, historia, descricao)
        self.id_treinador = id_treinador
        self.moedas = moedas

    def treinar_jogador(self, jogador, habilidade):
        custo_treinamento = 10  # Defina o custo como necessário
        if jogador.moedas >= custo_treinamento:
            jogador.treinar_habilidade(habilidade)
            jogador.moedas -= custo_treinamento
            print(f"Você treinou sua habilidade {habilidade} com {self.nome}.")
            print(f"Você agora tem {jogador.moedas} moedas.")
        else:
            print("Você não tem moedas suficientes para treinar.")


    def treinar_jogador(self, jogador, habilidade):
        # Lógica para treinar o jogador
        pass


class Inventario:
    def __init__(self):
        self.capacidade = 10
        self.instancias_itens = []

    def adicionar_instancia_item(self, instancia_item):
        # Lógica para adicionar uma instância de item ao inventário
        self.instancias_itens.append(instancia_item)

class Arena:
    def __init__(self, jogador, adversarios, connection):
        self.jogador = jogador
        self.adversarios = adversarios
        self.connection = connection
        self.treinadores = []

    
    def exibir_status_jogador(self):
        jogador_details = DataBase.get_player_details(self.connection, self.jogador)
        missao_details = DataBase.get_missao_details(self.connection, jogador_details[6])
        if jogador_details:
            print(f"\n Detalhes do Jogador:\n")
            print(f"Id: {jogador_details[0]}")
            print(f"Vida: {jogador_details[1]}")
            print(f"Ataque: {jogador_details[2]}")
            print(f"Resistência: {jogador_details[3]}")
            print(f"Missao Ativa: {missao_details[1]}\n")

        else:
            print("Erro ao obter detalhes do jogador.")
  

    def iniciar_desafio(self):

        print("Bem-vindo à Arena do Distrito de Barro!")
        DataBase.get_arena_details(self.connection, 4)
        print("\nEscolha uma opção:")
        print("1 - Lutar contra um adversário")
        print("2 - Treinar com um mestre")
        print("3 - Ver status do jogador")
        print("4 - Sair da Arena")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            self.iniciar_batalha()
        elif escolha == "2":
            print("Faça sua primeira batalha para desbloquear o treinamento com os mestres!")
            self.iniciar_desafio()
        elif escolha == "3":
            self.exibir_status_jogador()
            self.iniciar_desafio()
        elif escolha == "4":
            print("Saindo da Arena...")
        else:
            print("Opção inválida. Tente novamente.")
            self.iniciar_desafio()

    def treinar_com_mestre(self):
        print("Escolha um mestre para treinar:")
        for i, treinador in enumerate(self.treinadores, start=1):
            print(f"{i}. {treinador.nome}")

        try:
            escolha_treinador = int(input("Escolha um mestre (digite o número): "))
            if 1 <= escolha_treinador <= len(self.treinadores):
                treinador_escolhido = self.treinadores[escolha_treinador - 1]
                treinador_escolhido.treinar_jogador(self.jogador)
                self.iniciar_desafio()
            else:
                print("Escolha inválida. Tente novamente.")
                self.treinar_com_mestre()
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            self.treinar_com_mestre()

    def iniciar_batalha(self):
        # Pode escolher um adversário aleatório ou permitir ao jogador escolher
        adversario = self.escolher_adversario_missao()  # Adicione esta linha
        batalha = Batalha(self.jogador, adversario)
        batalha.iniciar()
        print(f"Você está enfrentando: {adversario[1]}")
        print("Escolha uma ação:")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Desistir")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            derrotou_adversario = Comandos.atacar(self.jogador, adversario)
            if derrotou_adversario:
                # Lógica para o jogador vencer a batalha
                pass
            else:
                # Lógica para permitir que o adversário contra-ataque
                pass
        elif escolha == "2":
            Comandos.defender(self.jogador)
            # Lógica para permitir que o adversário ataque enquanto o jogador está defendendo
        elif escolha == "3":
            print("Você desistiu da batalha.")
            # Lógica para sair da batalha
        else:
            print("Opção inválida. Tente novamente.")
            self.iniciar_batalha()



    def escolher_adversario_missao(self):
        missao = DataBase.get_missao_details(self.connection, 1)
        id_adversario = missao[4]
        detalhes_adversario = DataBase.get_adversario_details(self.connection, id_adversario)
        return detalhes_adversario

    def treinar_com_mestre(self):
        print("Escolha um treinador para treinar:")
        for i, treinador in enumerate(self.treinadores, start=1):
            print(f"{i}. {treinador.nome}")

        escolha_treinador = int(input("Escolha um treinador (digite o número): "))
        if 1 <= escolha_treinador <= len(self.treinadores):
            treinador_escolhido = self.treinadores[escolha_treinador - 1]
            treinador_escolhido.treinar_jogador(self.jogador)
            self.iniciar_desafio()
        else:
            print("Escolha inválida. Tente novamente.")
            self.treinar_com_mestre()

class Comandos:
    @staticmethod
    def atacar(jogador, adversario):
        # Lógica para ataque
        dano = jogador.ataque - adversario.resistencia
        adversario.vida -= dano
        print(f"Você ataca o adversário e causa {dano} de dano!")

        if adversario.vida <= 0:
            print("Você derrotou o adversário!")
            return True  # Indica que o adversário foi derrotado
        else:
            print(f"O adversário agora tem {adversario.vida} de vida.")
            return False  # Indica que o adversário ainda está vivo

    @staticmethod
    def defender(jogador):
        # Lógica para defesa
        jogador.resistencia += 5
        print("Você está se defendendo. Sua resistência aumentou!")

    # Adicione mais métodos para outros comandos, se necessário

class Batalha:
    def __init__(self, jogador, adversarios):
        self.jogador = jogador
        self.adversarios = adversarios

    def iniciar(self):
        print("Batalha iniciada!")

    # Adicione métodos relevantes para a lógica de batalha, como ataques, defesas, etc.