import random
import time

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.habilidade = 10
        self.moedas = 0

class Inimigo:
    def __init__(self, nome, vida, habilidade, recompensa_moedas):
        self.nome = nome
        self.vida = vida
        self.habilidade = habilidade
        self.recompensa_moedas = recompensa_moedas

def titulo():
    print("Bem-vindo ao Festival Sangrento!")
    print("Escolha uma opção:")
    print("1 - Iniciar Jogo")
    print("2 - Carregar Jogo")
    print("3 - Ajuda")
    print("4 - Sair")

    escolha = input("Digite o número da opção desejada: ")
    return escolha

def iniciar_jogo():
    nome_jogador = input("Digite o nome do seu personagem: ")
    jogador_personagem = Jogador(nome_jogador)

    print(f"\nBom jogo, {jogador_personagem.nome}!")
    time.sleep(1)
    return jogador_personagem

def carregar_jogo():
    # Adicione a lógica para carregar o jogo aqui
    print("Função de carregar jogo ainda não implementada.")
    return None

def ajuda():
    print("Este é um jogo de aventura onde você participará do Festival Sangrento.")
    print("Seu objetivo é enfrentar inimigos e avançar no torneio para conquistar a princesa.")
    print("Boa sorte herói!")

def main():
    while True:
        escolha = titulo()

        if escolha == '1':
            jogador_personagem = iniciar_jogo()
            treinamento(jogador_personagem)
            festival_sangrento(jogador_personagem)
        elif escolha == '2':
            carregar_jogo()
        elif escolha == '3':
            ajuda()
        elif escolha == '4':
            print("Até mais! Volte logo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
