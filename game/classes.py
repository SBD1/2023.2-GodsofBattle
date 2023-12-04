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
