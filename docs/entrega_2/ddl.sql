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

CREATE TABLE Mundo (
    Id_Mundo INT PRIMARY KEY,
    Nome VARCHAR,
    Historia VARCHAR
);

CREATE TABLE Regiao (
    Nome VARCHAR PRIMARY KEY,
    Descricao VARCHAR,
    Id_Mundo INT,
    FOREIGN KEY (Id_Mundo) REFERENCES Mundo(Id_Mundo)
);

-- Tabela: Local
CREATE TABLE Local (
    Id_Local INT PRIMARY KEY,
    Nome VARCHAR,
    Descricao VARCHAR
);

CREATE TABLE Jogador (
    Id_Jogador INT PRIMARY KEY,
    Vida INT,
    Ataque INT,
    Resistencia INT,
    Habilidade INT,
    Id_Local INT,
    Id_Missao INT,
    FOREIGN KEY (Id_Local) REFERENCES Local(Id_Local),
    FOREIGN KEY (Id_Missao) REFERENCES Missao(Id_Missao)
);

CREATE TABLE Adversario (
    Id_Adversario INT PRIMARY KEY,
    Vida INT,
    Ataque INT,
    Resistencia INT,
    Descricao VARCHAR,
    Id_Local INT,
    FOREIGN KEY (Id_Local) REFERENCES Local(Id_Local)
);

CREATE TABLE Missao (
    Id_Missao INT PRIMARY KEY,
    DescricaoMissao VARCHAR,
    Requisito INT,
    Status INT,
    Id_Adversario INT,
    Id_MissaoRequisito INT,
    FOREIGN KEY (Id_Adversario) REFERENCES Adversario(Id_Adversario),
    FOREIGN KEY (Id_MissaoRequisito) REFERENCES Missao(Id_Missao)
);

CREATE TABLE Loot (
    Id_Loot INT PRIMARY KEY,
    Id_Batalha INT,
    FOREIGN KEY (Id_Batalha) REFERENCES Batalha(Id_Batalha)
);


CREATE TABLE Batalha (
    Id_Batalha INT PRIMARY KEY,
    Id_Adversario INT,
    Id_Jogador INT,
    FOREIGN KEY (Id_Adversario) REFERENCES Adversario(Id_Adversario),
    FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador)
);


CREATE TABLE Treino (
    Id_Skill INT,
    Id_Treinador INT,
    Id_Jogador INT,
    FOREIGN KEY (Id_Skill) REFERENCES Habilidade(Id_Skill),
    FOREIGN KEY (Id_Treinador) REFERENCES Treinador(Id_Treinador),
    FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador),
    PRIMARY KEY (Id_Skill, Id_Treinador, Id_Jogador)
);

CREATE TABLE Habilidade (
    Id_Skill INT PRIMARY KEY,
    Dano INT,
    DescricaoSkill VARCHAR
);

CREATE TABLE Inventario (
    Id_Inventario INT PRIMARY KEY,
    Capacidade INT,
    Id_Jogador INT,
    FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador)
);

CREATE TABLE InstanciaItem (
    Id_InstanciaItem INT PRIMARY KEY,
    Id_Item INT,
    Id_Inventario INT,
    Id_Loot INT,
    FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item),
    FOREIGN KEY (Id_Inventario) REFERENCES Inventario(Id_Inventario),
    FOREIGN KEY (Id_Loot) REFERENCES Loot(Id_Loot)
);

CREATE TABLE NPC (
    Nome VARCHAR PRIMARY KEY,
    Tipo VARCHAR,
    Id_Local INT,
    FOREIGN KEY (Id_Local) REFERENCES Local(Id_Local)
);


CREATE TABLE Treinador (
    Id_Treinador INT PRIMARY KEY,
    Nome VARCHAR,
    Moedas INT,
    Descricao VARCHAR,
    Historia VARCHAR
);


CREATE TABLE Mercador (
    Id_Mercador INT PRIMARY KEY,
    Nome VARCHAR,
    Moedas INT,
    Descricao VARCHAR,
    Historia VARCHAR
);


CREATE TABLE Venda (
    Id_Mercador INT,
    Id_InstanciaItem INT,
    Id_Jogador INT,
    FOREIGN KEY (Id_Mercador) REFERENCES Mercador(Id_Mercador),
    FOREIGN KEY (Id_InstanciaItem) REFERENCES InstanciaItem(Id_InstanciaItem),
    FOREIGN KEY (Id_Jogador) REFERENCES Jogador(Id_Jogador),
    PRIMARY KEY (Id_Mercador, Id_InstanciaItem, Id_Jogador)
);


CREATE TABLE Item (
    Id_Item INT PRIMARY KEY,
    Tipo VARCHAR
);


CREATE TABLE Equipavel (
    Id_Equipavel INT PRIMARY KEY,
    Id_Item INT,
    DescricaoItem VARCHAR,
    Valor INT,
    Tipo VARCHAR,
    Bonus VARCHAR,
    FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item)
);


CREATE TABLE Melhoria (
    Id_Melhoria INT PRIMARY KEY,
    Id_Item INT,
    DescricaoItem VARCHAR,
    Valor INT,
    Tipo VARCHAR,
    TipoMelhoria VARCHAR,
    FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item)
);


CREATE TABLE Consumivel (
    Id_Consumivel INT PRIMARY KEY,
    Id_Item INT,
    DescricaoItem VARCHAR,
    Valor INT,
    TipoConsumivel VARCHAR,
    VidaRegenerada VARCHAR,
    FOREIGN KEY (Id_Item) REFERENCES Item(Id_Item)
);

