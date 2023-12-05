-- --------------------------------------------------------------------------------------
-- Data Criacao ...........: 29/10/2023                                                --
-- Autor(es) ..............: Samuel Macedo                                           --
-- Versao ..............: 1.0                                                          --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descricao .........: Inclusão de CREATE TABLE de todas as tabelas do banco de dados.--
-- --------------------------------------------------------------------------------------
-- | Atualizacao : 30/10/2023 | Autor(es):                      |      --
--                            | Descricao:                      |      --
-- --------------------------------------------------------------------------------------

-- Tabela: Mundo
begin;
    CREATE TABLE IF NOT EXISTS Mundo (
        Id_Mundo SERIAL PRIMARY KEY, 
        Nome VARCHAR,
        Historia VARCHAR
    );
commit;

-- Tabela: Regiao
begin;
    CREATE TABLE IF NOT EXISTS Regiao (
        Nome VARCHAR PRIMARY KEY,
        Descricao VARCHAR,
        Id_Mundo INT,
        FOREIGN KEY (Id_Mundo) REFERENCES Mundo(Id_Mundo)
    );
commit;

-- Tabela: Local
begin;
    CREATE TABLE IF NOT EXISTS Local (
        Id_Local SERIAL PRIMARY KEY,
        Nome VARCHAR,
        Descricao VARCHAR,
        Id_Regiao VARCHAR,
        FOREIGN KEY (Id_Regiao) REFERENCES Regiao(Nome)
    );
commit;

-- Tabela: Adversario
begin;
    CREATE TABLE IF NOT EXISTS Adversario (
        Id_Adversario SERIAL PRIMARY KEY,
        Vida INT,
        Ataque INT,
        Resistencia INT,
        Descricao VARCHAR,
        Id_Local INT,
        FOREIGN KEY (Id_Local) REFERENCES Local(Id_Local)
    );
commit;

-- Tabela: Missao
begin;
    CREATE TABLE IF NOT EXISTS Missao (
        Id_Missao SERIAL PRIMARY KEY,
        DescricaoMissao VARCHAR,
        Requisito INT,
        Status INT,
        Id_Adversario INT,
        Id_MissaoRequisito INT,
        FOREIGN KEY (Id_Adversario) REFERENCES Adversario(Id_Adversario),
        FOREIGN KEY (Id_MissaoRequisito) REFERENCES Missao(Id_Missao)
    );
commit;

-- Tabela: Jogador
begin; 
    CREATE TABLE IF NOT EXISTS Jogador (
        Id_Jogador SERIAL PRIMARY KEY,
        Vida INT,
        Ataque INT,
        Resistencia INT,
        Habilidade INT,
        Id_Local INT,
        Id_Missao INT,
        FOREIGN KEY (Id_Local) REFERENCES Local(Id_Local),
        FOREIGN KEY (Id_Missao) REFERENCES Missao(Id_Missao)
    );
commit;


-- Tabelas de Batalha
begin;
    CREATE TABLE IF NOT EXISTS Batalha (
        Id_Batalha SERIAL PRIMARY KEY,
        Id_Adversario INT,
        Id_Jogador INT,
        FOREIGN KEY (Id_Adversario) REFERENCES Adversario(Id_Adversario),
        FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador)
    );
commit;

--Tabela Loot
begin;
    CREATE TABLE IF NOT EXISTS Loot (
        Id_Loot SERIAL PRIMARY KEY,
        Id_Batalha INT,
        FOREIGN KEY (Id_Batalha) REFERENCES Batalha(Id_Batalha)
    );
commit;

-- Tabela: Habilidade
begin;  
    CREATE TABLE IF NOT EXISTS Habilidade (
        Id_Skill SERIAL PRIMARY KEY,
        Dano INT,
        DescricaoSkill VARCHAR
    );
commit;

-- Tabela: Inventario
begin;
    CREATE TABLE IF NOT EXISTS Inventario (
        Id_Inventario SERIAL PRIMARY KEY,
        Capacidade INT,
        Id_Jogador INT,
        FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador)
    );
commit;

-- Tabela: NPC
begin;
    CREATE TABLE IF NOT EXISTS NPC (
        Nome VARCHAR PRIMARY KEY,
        Tipo VARCHAR,
        Id_Local INT,
        FOREIGN KEY (Id_Local) REFERENCES Local(Id_Local)
    );
commit;

--Tabela: Treinador
begin;  
    CREATE TABLE IF NOT EXISTS Treinador (
        Id_Treinador SERIAL PRIMARY KEY,
        Nome VARCHAR,
        Moedas INT,
        Descricao VARCHAR,
        Historia VARCHAR
    );
commit;

-- Tabela: Mercador
begin;
    CREATE TABLE IF NOT EXISTS Mercador (
        Id_Mercador SERIAL PRIMARY KEY,
        Nome VARCHAR,
        Moedas INT,
        Descricao VARCHAR,
        Historia VARCHAR
    );
commit;


-- Tabela Treino
begin;
    CREATE TABLE IF NOT EXISTS Treino (
        Id_Skill INT,
        Id_Treinador INT,
        Id_Jogador INT,
        FOREIGN KEY (Id_Skill) REFERENCES Habilidade(Id_Skill),
        FOREIGN KEY (Id_Treinador) REFERENCES Treinador(Id_Treinador),
        FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador),
        PRIMARY KEY (Id_Skill, Id_Treinador, Id_Jogador)
    );
commit;

-- Tabela: Item
begin;  
    CREATE TABLE IF NOT EXISTS Item (
        Id_Item SERIAL PRIMARY KEY,
        Tipo VARCHAR
    );
commit;

-- Tabela: InstanciaItem
begin;
    CREATE TABLE IF NOT EXISTS InstanciaItem (
        Id_InstanciaItem SERIAL PRIMARY KEY,
        Id_Item INT,
        Id_Inventario INT,
        Id_Loot INT,
        FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item),
        FOREIGN KEY (Id_Inventario) REFERENCES Inventario(Id_Inventario),
        FOREIGN KEY (Id_Loot) REFERENCES Loot(Id_Loot)
    );
commit;

-- Tabela: Equipavel
begin;
    CREATE TABLE IF NOT EXISTS Equipavel (
        Id_Equipavel SERIAL PRIMARY KEY,
        Id_Item INT,
        DescricaoItem VARCHAR,
        Valor INT,
        Tipo VARCHAR,
        Bonus VARCHAR,
        FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item)
    );
commit;

-- Tabela: Melhoria
begin;
    CREATE TABLE IF NOT EXISTS Melhoria (
        Id_Melhoria SERIAL PRIMARY KEY,
        Id_Item INT,
        DescricaoItem VARCHAR,
        Valor INT,
        Tipo VARCHAR,
        TipoMelhoria VARCHAR,
        FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item)
    );
commit;

-- Tabela: Consumivel
begin;
    CREATE TABLE IF NOT EXISTS Consumivel (
        Id_Consumivel SERIAL PRIMARY KEY,
        Id_Item INT,
        DescricaoItem VARCHAR,
        Valor INT,
        TipoConsumivel VARCHAR,
        VidaRegenerada VARCHAR,
        FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item)
    );
commit;

-- Tabela: Venda
begin;
    CREATE TABLE IF NOT EXISTS Venda (
        Id_Mercador INT,
        Id_InstanciaItem INT,
        Id_Jogador INT,
        FOREIGN KEY (Id_Mercador) REFERENCES Mercador(Id_Mercador),
        FOREIGN KEY (Id_InstanciaItem) REFERENCES InstanciaItem(Id_InstanciaItem),
        FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador),
        PRIMARY KEY (Id_Mercador, Id_InstanciaItem, Id_Jogador)
    );
commit;