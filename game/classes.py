#classes.py

from database import DataBase
from game import *
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

    def get_ataque(self):
        return self.ataque
    
    def get_especial(self):
        return self.habilidade.especial

    def adicionar_instancia_item(self, instancia_item):
        self.inventario.adicionar_instancia_item(instancia_item)

    def treinar_habilidade(self, habilidade):
        self.habilidade += 1  # Aumenta a habilidade do jogador
        print(f"Sua habilidade agora é {self.habilidade}.")
        pass


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
        self.id_missao_requisito = id_missao_requisito
 

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


class Inventario:
    def __init__(self):
        self.capacidade = 10
        self.instancias_itens = []

    def adicionar_instancia_item(self, instancia_item):
        # Lógica para adicionar uma instância de item ao inventário
        self.instancias_itens.append(instancia_item)

class Arena:
    def __init__(self, jogador_id, adversarios, connection):
        self.jogador_id = jogador_id
        self.adversarios = adversarios
        self.connection = connection
        self.treinadores = []
        self.data_base = DataBase()

    
    def exibir_status_jogador(self):
        jogador_details = DataBase.get_player_details(self.connection, self.jogador_id)
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
        while True:
            print("\nEscolha uma opção:")
            print("1 - Lutar contra um adversário")
            print("2 - Treinar com um mestre")
            print("3 - Ver status do jogador")
            print("4 - Sair da Arena")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                vitoria = self.iniciar_batalha(self.jogador_id)
                if vitoria:
                    return True
            elif escolha == "2":
                print("\nFaça sua primeira batalha para desbloquear o treinamento com os mestres!\n")
                pass
            elif escolha == "3":
                self.exibir_status_jogador()
                pass
            elif escolha == "4":
                print("Saindo da Arena...")
                pass
            else:
                print("Opção inválida. Tente novamente.")
                pass

    def arena_de_barro(self):
        while True:
            print("Bem-vindo à Arena do Distrito de Barro!")
            DataBase.get_arena_details(self.connection, 4)
            print("\nEscolha uma opção:")
            print("1 - Lutar contra um adversário")
            print("2 - Treinar com um mestre")
            print("3 - Ver status do jogador")
            print("4 - Sair da Arena")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                vitoria = self.iniciar_batalha(self.jogador_id)
                if vitoria:
                    return True            
            elif escolha == "2":
                print("\nFuncionalidade de treino ainda não está pronta\n")
                pass
            elif escolha == "3":
                self.exibir_status_jogador()
                pass
            elif escolha == "4":
                self.midgame()
                break
            else:
                print("Opção inválida. Tente novamente.")
                pass

    def arena_de_prata(self):
        print("Bem-vindo à Arena do Distrito de Prata!")
        DataBase.get_arena_details(self.connection, 5)
        print("\nEscolha uma opção:")
        print("1 - Lutar contra um adversário")
        print("2 - Treinar com um mestre")
        print("3 - Ver status do jogador")
        print("4 - Sair da Arena")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            vitoria = self.iniciar_batalha(self.jogador_id)
            if vitoria:
                return True
        elif escolha == "2":
            print("\nFuncionalidade de treino ainda não está pronta\n")
            pass
        elif escolha == "3":
            self.exibir_status_jogador()
            pass
        elif escolha == "4":
            self.midgame()
        else:
            print("Opção inválida. Tente novamente.")
            pass

    def arena_de_ouro(self):
        print("Bem-vindo à Arena do Distrito de Ouro!")
        DataBase.get_arena_details(self.connection, 2)
        print("\nEscolha uma opção:")
        print("1 - Lutar contra um adversário")
        print("2 - Treinar com um mestre")
        print("3 - Ver status do jogador")
        print("4 - Sair da Arena")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            vitoria = self.iniciar_batalha(self.jogador_id)
            if vitoria:
                return True
        elif escolha == "2":
            print("\nFuncionalidade de treino ainda não está pronta\n")
            pass
        elif escolha == "3":
            self.exibir_status_jogador()
            pass
        elif escolha == "4":
            return False
        else:
            print("Opção inválida. Tente novamente.")
            pass

    def iniciar_batalha(self, jogador_id):
        adversario_details = self.data_base.get_adversario_details(self.connection, self.data_base.get_adversario_atual(self.connection, self.jogador_id))  # Retorna detalhes do adversario atual
        adversario = Adversario(adversario_details[0], adversario_details[1], adversario_details[2], adversario_details[3], adversario_details[4])  # Cria instância de adversario

        if adversario is None:
            print("Você decidiu sair da Arena. Até a próxima!")
            return

        jogador_details = self.data_base.get_player_details(self.connection, jogador_id)  # Atualize esta linha
        jogador = Jogador(jogador_details[0], jogador_details[1], jogador_details[2], jogador_details[3], jogador_details[4], jogador_details[5])  # Adicione esta linha
        print(f" {jogador}")
        batalha = Batalha(jogador_id, adversario, self.connection)
        print("Batalha iniciada!\n")

        while True:
            try:
                especial = 0
                acao = int(input("Escolha uma ação (1 para atacar, 2 para defender, 3 para desistir): "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
            if acao == 1:
                print(f"Antes de atacar - Vida do adversário: {adversario.vida}")
                derrotou_adversario = batalha.atacar(jogador, adversario)  # Atualize esta
                especial += 1 
                if derrotou_adversario:
                    DataBase.missao_concluida(self.connection, jogador.id_jogador)
                    DataBase.upar_jogador(self.connection, jogador.id_jogador)
                    print("Você venceu a batalha! Você fica um pouco mais forte")
                    return True
                    break
                adversario_atacou = batalha.contra_ataque(jogador, adversario)  # Atualize esta linha
                if adversario_atacou:
                    break
            elif acao == 2:
                print("Você defendeu o ataque do adversário.")
                adversario_atacou = batalha.contra_ataque_defendido(jogador, adversario)  # Atualize esta linha
                if adversario_atacou:
                    break
                pass
            
            elif acao == 3:
                print("Você desistiu da batalha. Até a próxima!")
                break

            elif acao == 4:
                if especial > 4:
                    print(f"Antes de atacar - Vida do adversário: {adversario.vida}")
                    derrotou_adversario = batalha.especial(jogador, adversario)  # Atualize esta
                    especial = 0

                    if derrotou_adversario:
                        DataBase.missao_concluida(self.connection, jogador.id_jogador)
                        print("Você venceu a batalha! Você fica um pouco mais forte")
                        
                        return True
                        break
                    adversario_atacou = batalha.contra_ataque(jogador, adversario)  # Atualize esta linha

                    if adversario_atacou:
                        break

    def treinar_com_mestre(self):
        print("Escolha um mestre para treinar:")
        for i, treinador in enumerate(self.treinadores, start=1):
            print(f"{i}. {treinador.nome}")

        try:
            escolha_treinador = int(input("Escolha um mestre (digite o número): "))
            if 1 <= escolha_treinador <= len(self.treinadores):
                treinador_escolhido = self.treinadores[escolha_treinador - 1]
                treinador_escolhido.treinar_jogador(self.jogador)
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


class Batalha:
    def __init__(self, jogador, adversario, connection):
        self.jogador = jogador
        self.adversario = adversario
        self.connection = connection


    def atacar(self, jogador, adversario):
        # Lógica para ataque
        dano = jogador.get_ataque() - adversario.resistencia

        adversario.vida -= dano
        print(f"Você ataca o adversário e causa {dano} de dano!")

        if adversario.vida <= 0:
            print(f"Você derrotou o {adversario.descricao}!")
            return True  # Indica que o adversário foi derrotado
        else:
            print(f"O adversário agora tem {adversario.vida} de vida.\n")
            return False  # Indica que o adversário ainda está vivo
    
    def especial(self, jogador, adversario):
        dano = jogador.get_especial() - adversario.resistencia

        adversario.vida -= dano
        print(f"Você usou um esepcial no adversário e causa {dano} de dano!")

        if adversario.vida <= 0:
            print(f"Você derrotou o {adversario.descricao}!")
            return True  # Indica que o adversário foi derrotado
        else:
            print(f"O adversário agora tem {adversario.vida} de vida.\n")
            return False  # Indica que o adversário ainda está vivo

    def iniciar(self):
        print("Batalha iniciada!")

        while True:
            print("Escolha uma ação:\n")
            print("1 - Atacar\n")
            print("2 - Defender\n")
            print("3 - Desistir\n")

            escolha = input("Escolha uma opção: ")
            cont_ataque = 0
            especial = 0

            if escolha == "1":
                derrotou_adversario = self.atacar(Jogador, self.adversario)
                cont_ataque += 1

                if cont_ataque > 3:
                    especial += 1
                    cont_ataque = 0

                if derrotou_adversario:
                    # Lógica para o jogador vencer a batalha
                    print("Você venceu a batalha!")
                    break
                else:
                    # Lógica para permitir que o adversário contra-ataque
                    self.contra_ataque()
            elif escolha == "2":
                self.defender(self.jogador)
                especial += 1
                # Lógica para permitir que o adversário ataque enquanto o jogador está defendendo
                self.contra_ataque()
            elif escolha == "3":
                print("Você desistiu da batalha.")
                # Lógica para sair da batalha
                break
#            elif escolha == "4":
#                if especial > 4:
#                    derrotou_adversario = self.especial(Jogador, self.adversario)
#
#                    especial = 0
#
#                    if derrotou_adversario:
#                        # Lógica para o jogador vencer a batalha
#                        print("Você venceu a batalha!")
#                        break
#                    else:
#                        # Lógica para permitir que o adversário contra-ataque
#                        self.contra_ataque()
#                else:
#                    print("Você ainda não consegue utilizar o especial")
            else:
                print("Opção inválida. Tente novamente.")

    def contra_ataque(self, jogador, adversario):
        # Lógica para o adversário contra-atacar
        dano_adversario = self.adversario.ataque - jogador.resistencia
        jogador.vida -= dano_adversario
        print(f"O adversário ataca e causa {dano_adversario} de dano!")

        if jogador.vida <= 0:
            print("Você foi derrotado!")
            return True  # Indica que o jogador foi derrotado
        else:
            print(f"Você agora tem {jogador.vida} de vida.\n")
            return False  # Indica que o jogador ainda está vivo

    def contra_ataque_defendido(self, jogador, adversario):
        # Lógica para o adversário contra-atacar enquanto o jogador está defendido
        dano_adversario = int((self.adversario.ataque - jogador.resistencia) / 2)
        jogador.vida -= dano_adversario
        print(f"O adversário ataca e causa {dano_adversario} de dano!")
        if jogador.vida <= 0:
            print("Você foi derrotado!")
            return True  # Indica que o jogador foi derrotado
        else:
            print(f"Você agora tem {jogador.vida} de vida.\n")
            return False  # Indica que o jogador ainda está vivo



