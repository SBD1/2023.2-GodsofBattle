# classes.py
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
        return f"Jogador {self.nome}: Vida={self.vida}, Ataque={self.ataque}, Resistencia={self.resistencia}, Habilidade={self.habilidade}, Missao Ativa={self.missao_ativa}"

    def __init__(self, id_jogador, nome, vida, ataque, resistencia, habilidade, missao_ativa=None):
        self.id_jogador = id_jogador
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.resistencia = resistencia
        self.habilidade = habilidade
        self.missao_ativa = missao_ativa
        self.inventario = Inventario()

    def adicionar_instancia_item(self, instancia_item):
        self.inventario.adicionar_instancia_item(instancia_item)

    def treinar_habilidade(self, habilidade):
        # Lógica para treinar a habilidade do jogador
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


class Treinador(NPC):
    def __init__(self, id_treinador, nome, historia, descricao, moedas):
        super().__init__(nome, historia, descricao)
        self.id_treinador = id_treinador
        self.moedas = moedas

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
    def __init__(self, jogador, adversarios, treinadores):
        self.jogador = jogador
        self.adversarios = adversarios
        self.treinadores = treinadores

    def iniciar_desafio(self):
        print("Bem-vindo à Arena do Reino dos Pebleus!")
        print("Escolha uma opção:")
        print("1 - Lutar contra um adversário")
        print("2 - Treinar com um mestre")
        print("3 - Ver status do jogador")
        print("4 - Sair da Arena")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            self.iniciar_batalha()
        elif escolha == "2":
            self.treinar_com_mestre()
        elif escolha == "3":
            self.jogador.exibir_status()
            self.iniciar_desafio()
        elif escolha == "4":
            print("Saindo da Arena...")
        else:
            print("Opção inválida. Tente novamente.")
            self.iniciar_desafio()

    def iniciar_batalha(self):
        # Lógica para iniciar uma batalha
        # Pode escolher um adversário aleatório ou permitir ao jogador escolher
        adversario = random.choice(self.adversarios)
        
        print(f"Você está enfrentando: {adversario.descricao}")
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
            
    def treinar_com_mestre(self):
        # Lógica para treinar com um treinador
        # Pode escolher um treinador aleatório ou permitir ao jogador escolher
        treinador = random.choice(self.treinadores)
        treinador.treinar_jogador(self.jogador)
        self.iniciar_desafio()

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