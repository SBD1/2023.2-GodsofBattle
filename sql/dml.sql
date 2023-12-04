-- --------------------------------------------------------------------------------------
-- Data Criacao ...........: 30/10/2023                                                --
-- Autor(es) ..............: Luana Torres                                              --
-- Versao ..............: 1.0                                                          --
-- Banco de Dados .........: PostgreSQL                                                --
-- Descricao .........: Inclusão de INSERT TABLE de todas as tabelas do banco de dados.--
-- --------------------------------------------------------------------------------------
-- | Atualizacao : 30/10/2023 | Autor(es):                      |      --
--                            | Descricao:                      |      --
-- --------------------------------------------------------------------------------------


-- Inserir dados na tabela Mundo
INSERT INTO Mundo (Id_Mundo, Nome, Historia) VALUES (1, 'Reino de Eldoria', 'Um vasto reino onde se desenrola a história do jovem plebeu em busca do amor da princesa e da glória no famoso Festival Sangrento.');

-- Inserir dados na tabela Regiao
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Planície Verde', 'Uma vasta planície onde o protagonista inicia seu treinamento e enfrenta os desafios iniciais.', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Montanhas do Desafio', 'Montanhas escarpadas onde os guerreiros mais destemidos treinam e enfrentam adversários poderosos.', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Floresta dos Mistérios', 'Uma densa floresta onde segredos antigos e criaturas mágicas testam a coragem do protagonista.', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Deserto da Perdição', 'Um deserto vasto e implacável, lar de bandidos e criaturas das sombras, onde a verdadeira determinação é posta à prova.', 1);

-- Inserir dados na tabela Local
INSERT INTO Local (Id_Local, Nome, Descricao) VALUES (1, 'Casa do Mestre', 'Local onde o protagonista treina suas habilidades com seu mestre.');
INSERT INTO Local (Id_Local, Nome, Descricao) VALUES (2, 'Arena do Festival', 'A arena onde ocorrem as batalhas do Festival Sangrento.');
INSERT INTO Local (Id_Local, Nome, Descricao) VALUES (3, 'Bosque dos Encantos', 'Um local mágico na Floresta dos Mistérios, onde segredos ancestrais são revelados.');


-- Inserir dados na tabela Adversario
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (1, 50, 10, 5, 'Bandido da Planície', 1);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (2, 70, 15, 8, 'Orc das Montanhas', 2);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (3, 90, 20, 10, 'Guardião da Floresta', 3);

-- Inserir dados na tabela Missao
INSERT INTO Missao (Id_Missao, DescricaoMissao, Requisito, Status, Id_Adversario, Id_MissaoRequisito) VALUES (1, 'Desafie o Bandido da Planície', NULL, 0, 1, NULL);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Requisito, Status, Id_Adversario, Id_MissaoRequisito) VALUES (2, 'Derrote o Orc das Montanhas', 1, 0, 2, 1);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Requisito, Status, Id_Adversario, Id_MissaoRequisito) VALUES (3, 'Supere o Guardião da Floresta', 2, 0, 3, 2);

-- Inserir dados na tabela Jogador
INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (1, 100, 20, 10, 5, 1, 1);
INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (2, 100, 15, 15, 5, 2, 1);
INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (3, 100, 20, 10, 5, 3, 1);
INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (4, 100, 20, 15, 10, 1, 2);


-- Inserir dados na tabela Batalha
INSERT INTO Batalha (Id_Batalha, Id_Adversario, Id_Jogador) VALUES (1, 1, 1);
INSERT INTO Batalha (Id_Batalha, Id_Adversario, Id_Jogador) VALUES (2, 2, 1);
INSERT INTO Batalha (Id_Batalha, Id_Adversario, Id_Jogador) VALUES (3, 3, 1);

-- Inserir dados na tabela Loot
INSERT INTO Loot (Id_Loot, Id_Batalha) VALUES (1, 1);
INSERT INTO Loot (Id_Loot, Id_Batalha) VALUES (2, 2);
INSERT INTO Loot (Id_Loot, Id_Batalha) VALUES (3, 3);



-- Inserir dados na tabela Habilidade
INSERT INTO Habilidade (Id_Skill, Dano, DescricaoSkill) VALUES (1, 10, 'Ataque Rápido');
INSERT INTO Habilidade (Id_Skill, Dano, DescricaoSkill) VALUES (2, 15, 'Investida Poderosa');
INSERT INTO Habilidade (Id_Skill, Dano, DescricaoSkill) VALUES (3, 20, 'Técnica da Sombra');
INSERT INTO Habilidade (Id_Skill, Dano, DescricaoSkill) VALUES (4, 25, 'Explosão Arcana');


-- Inserir dados na tabela Inventario
INSERT INTO Inventario (Id_Inventario, Capacidade, Id_Jogador) VALUES (1, 50, 1);
INSERT INTO Inventario (Id_Inventario, Capacidade, Id_Jogador) VALUES (2, 50, 2);


-- Inserir dados na tabela Item
INSERT INTO Item (Id_Item, Tipo) VALUES (1, 'Consumível');
INSERT INTO Item (Id_Item, Tipo) VALUES (2, 'Equipável');
INSERT INTO Item (Id_Item, Tipo) VALUES (3, 'Melhoria');

-- Inserir dados na tabela InstanciaItem
INSERT INTO InstanciaItem (Id_InstanciaItem, Id_Item, Id_Inventario, Id_Loot) VALUES (1, 1, 1, 1);
INSERT INTO InstanciaItem (Id_InstanciaItem, Id_Item, Id_Inventario, Id_Loot) VALUES (2, 2, 1, 2);
INSERT INTO InstanciaItem (Id_InstanciaItem, Id_Item, Id_Inventario, Id_Loot) VALUES (3, 3, 1, 3);

-- Inserir dados na tabela NPC
INSERT INTO NPC (Nome, Tipo, Id_Local) VALUES ('Mago Velho', 'Mago', 3);
INSERT INTO NPC (Nome, Tipo, Id_Local) VALUES ('Guarda Real', 'Soldado', 2);
INSERT INTO NPC (Nome, Tipo, Id_Local) VALUES ('Cidadão Comum', 'Civil', 1);


-- Inserir dados na tabela Treinador
INSERT INTO Treinador (Id_Treinador, Nome, Moedas, Descricao, Historia) VALUES (1, 'Mestre Kuro', 200, 'Um mestre experiente que guia o protagonista em sua jornada.', 'Mestre Kuro é um antigo guerreiro lendário, conhecido por sua habilidade em treinar jovens talentos.');
INSERT INTO Treinador (Id_Treinador, Nome, Moedas, Descricao, Historia) VALUES (2, 'Treinadora Líria', 250, 'Uma treinadora ágil e astuta que desafia o protagonista.', 'Líria é uma treinadora habilidosa, famosa por suas técnicas inovadoras e estilo de luta único.');


-- Inserir dados na tabela Treino
INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (1, 1, 1);
INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (2, 1, 1);
INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (3, 2, 1);
INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (4, 2, 1);

-- Inserir dados na tabela Mercador
INSERT INTO Mercador (Id_Mercador, Nome, Moedas, Descricao, Historia) VALUES (1, 'Mercador Rurik', 300, 'Um mercador viajante que oferece itens raros e valiosos.', 'Rurik é conhecido em todo o reino por suas mercadorias de alta qualidade e habilidade em negociar.');
INSERT INTO Mercador (Id_Mercador, Nome, Moedas, Descricao, Historia) VALUES (2, 'Mercadora Elara', 280, 'Uma mercadora carismática que vende itens mágicos e encantados.', 'Elara é uma mercadora habilidosa, especializada em itens mágicos e encantados que podem mudar o curso de uma batalha.');

-- Inserir dados na tabela Venda
INSERT INTO Venda (Id_Mercador, Id_InstanciaItem, Id_Jogador) VALUES (1, 1, 1);
INSERT INTO Venda (Id_Mercador, Id_InstanciaItem, Id_Jogador) VALUES (2, 2, 1);



-- Inserir dados na tabela Equipavel
INSERT INTO Equipavel (Id_Equipavel, Id_Item, DescricaoItem, Valor, Tipo, Bonus) VALUES (1, 2, 'Espada afiada', 50, 'Equipável', '+10 de Ataque');
INSERT INTO Equipavel (Id_Equipavel, Id_Item, DescricaoItem, Valor, Tipo, Bonus) VALUES (2, 3, 'Escudo resistente', 30, 'Equipável', '+5 de Resistência');

-- Inserir dados na tabela Melhoria
INSERT INTO Melhoria (Id_Melhoria, Id_Item, DescricaoItem, Valor, Tipo, TipoMelhoria) VALUES (1, 1, 'Poção fortificante', 20, 'Melhoria', 'VidaRegenerada');

-- Inserir dados na tabela Consumivel
INSERT INTO Consumivel (Id_Consumivel, Id_Item, DescricaoItem, Valor, TipoConsumivel, VidaRegenerada) VALUES (1, 1, 'Poção de Cura', 15, 'Vida', '+20');
INSERT INTO Consumivel (Id_Consumivel, Id_Item, DescricaoItem, Valor, TipoConsumivel, VidaRegenerada) VALUES (2, 1, 'Poção de Energia', 25, 'Energia', '+15');
