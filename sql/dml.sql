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
INSERT INTO Mundo (Id_Mundo, Nome, Historia) VALUES (default, 'Reino de Eldoria', 'Um vasto reino onde se desenrola a história do jovem plebeu em busca do amor da princesa e da glória no famoso Festival Sangrento.');

-- Inserir dados na tabela Regiao
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Planície Verde', 'Uma vasta planície onde o protagonista inicia seu treinamento e enfrenta os desafios iniciais.', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Montanhas do Desafio', 'Montanhas escarpadas onde os guerreiros mais destemidos treinam e enfrentam adversários poderosos.', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Floresta dos Mistérios', 'Uma densa floresta onde segredos antigos e criaturas mágicas testam a coragem do protagonista.', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Deserto da Perdição', 'Um deserto vasto e implacável, lar de bandidos e criaturas das sombras, onde a verdadeira determinação é posta à prova.', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Distrito do Barro', 'Região mais pobre do reino de Eudoria, ocupada majoritariamente por trabalhadores rurais', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Distrito da Prata', 'Região mais populosa do reino de Eudoria, ocupada por burgueses e cidadões de classe média', 1);
INSERT INTO Regiao (Nome, Descricao, Id_Mundo) VALUES ('Distrito do Ouro', 'Região mais rica do reino de Eudoria, ocupada por nobres e cidadões de classe superior', 1);

-- Inserir dados na tabela Local
INSERT INTO Local (Id_Local, Nome, Descricao, Id_Regiao) VALUES (default, 'Casa do Mestre', 'Local onde o protagonista treina suas habilidades com seu mestre.', 'Distrito da Prata');
INSERT INTO Local (Id_Local, Nome, Descricao, Id_Regiao) VALUES (default, 'Arena Principal', 'Uma arena construida no centro do reino, decorada em ouro e com dezenas de fileiras lotadas de cidadões ansiosos por sangue derramado. Nela ocorrem as batalhas principais do Festival Sangrento, todas as batalhas nessa arena contam com a presença do Rei.', 'Distrito do Ouro');
INSERT INTO Local (Id_Local, Nome, Descricao, Id_Regiao) VALUES (default, 'Bosque dos Encantos', 'Um local mágico na Floresta dos Mistérios, onde segredos ancestrais são revelados.', 'Distrito do Barro');
INSERT INTO Local (Id_Local, Nome, Descricao, Id_Regiao) VALUES (default, 'Arena Distrito de Barro', 'Uma Arena construída com madeira de forma precária e desleixada, onde as batalhas mais insignificantes aos olhos do rei vão acontecer.', 'Distrito do Barro');
INSERT INTO Local (Id_Local, Nome, Descricao, Id_Regiao) VALUES (default, 'Arena Distrito da Prata', 'Uma Arena construída com madeira ornamentada de forma preciosista e cheia de detalhes, onde as batalhas entre alguns dos sujeitos mais ricos do reino vão acontecer.', 'Distrito da Prata'); 

-- Inserir dados na tabela Adversario
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (1, 50, 10, 5, 'João, Trabalhador Rural', 4);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (2, 70, 15, 8, 'Mendigo Combativo', 4);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (3, 90, 20, 10, 'Willian, Vendedor de Frutas', 4);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (4, 60, 12, 6, 'Carlos, Trombadinha de Rua', 4);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (5, 80, 18, 9, 'Marcio, Dono da Taverna Copo Sujo', 4);

INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (6, 100, 22, 12, 'Dr. Rodrigo, Médico Ilustre', 5);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (7, 70, 15, 8, 'Eng. Roger, Construtor Renomado', 5);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (8, 90, 20, 10, 'Fabiano, Comerciante de Pedras preciosas', 5);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (9, 110, 25, 14, 'Julio, Advogado de Sucesso', 5);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (10, 80, 18, 9, 'Renato, Filho do Banqueiro', 5);

INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (11, 100, 22, 12, 'Duque Guilherme, Nobre Renomado', 3);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (12, 120, 28, 16, 'Duque Alfredo, Irmão mais velho do Duque Guilherme', 3);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (13, 90, 20, 10, 'Barão Maurício, O maior detentor de terras do reino', 3);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (14, 110, 25, 14, 'Conde Ricardo, Guerreiro Experiente e capitão da guarda real', 3);
INSERT INTO Adversario (Id_Adversario, Vida, Ataque, Resistencia, Descricao, Id_Local) VALUES (15, 130, 30, 18, 'Príncipe Alexander, Herdeiro do reino vizinho', 3);

-- Inserir dados na tabela Missao 
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (1, 'Desafie João, Trabalhador Rural', 0, 1, NULL);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (2, 'Supere o Mendigo Combativo', 0, 2, 1);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (3, 'Derrote Willian, Vendedor de Frutas', 0, 3, 2);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (4, 'Vença Carlos, Trombadinha de Rua', 0, 4, 3);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (5, 'Conquiste Marcio, Dono da Taverna Copo Sujo', 0, 5, 4);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (6, 'Desafie Dr. Rodrigo, Médico Ilustre', 0, 6, 5);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (7, 'Supere Eng. Roger, Construtor Renomado', 0, 7, 6);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (8, 'Derrote Fabiano, Comerciante de Pedras preciosas', 0, 8, 7);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (9, 'Vença Julio, Advogado de Sucesso', 0, 9, 8);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (10, 'Conquiste Renato, Filho do Banqueiro', 0, 10, 9);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (11, 'Desafie Duque Guilherme, Nobre Renomado', 0, 11, 10);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (12, 'Supere Duque Alfredo, Irmão mais velho do Duque Guilherme', 0, 12, 11);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (13, 'Derrote Barão Maurício, O maior detentor de terras do reino', 0, 13, 12);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (14, 'Vença Conde Ricardo, Guerreiro Experiente e capitão da guarda real', 0, 14, 13);
INSERT INTO Missao (Id_Missao, DescricaoMissao, Status, Id_Adversario, Id_MissaoRequisito) VALUES (15, 'Conquiste Príncipe Alexander, Herdeiro do reino vizinho', 0, 15, 14);

-- Inserir dados na tabela Jogador
-- INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (1, 100, 20, 10, 5, 1, 1);
-- INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (2, 100, 15, 15, 5, 2, 1);
-- INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (3, 100, 20, 10, 5, 3, 1);
-- INSERT INTO Jogador (Id_Jogador, Vida, Ataque, Resistencia, Habilidade, Id_Local, Id_Missao) VALUES (4, 100, 20, 15, 10, 1, 2);


-- Inserir dados na tabela Batalha
--INSERT INTO Batalha (Id_Batalha, Id_Adversario, Id_Jogador) VALUES (1, 1, 1);
--INSERT INTO Batalha (Id_Batalha, Id_Adversario, Id_Jogador) VALUES (2, 2, 1);
--INSERT INTO Batalha (Id_Batalha, Id_Adversario, Id_Jogador) VALUES (3, 3, 1);

-- Inserir dados na tabela Loot
--INSERT INTO Loot (Id_Loot, Id_Batalha) VALUES (1, 1);
--INSERT INTO Loot (Id_Loot, Id_Batalha) VALUES (2, 2);
--INSERT INTO Loot (Id_Loot, Id_Batalha) VALUES (3, 3);



-- Inserir dados na tabela Habilidade
INSERT INTO Habilidade (Dano, DescricaoSkill) VALUES ( 10, 'Ataque Rápido');
INSERT INTO Habilidade (Dano, DescricaoSkill) VALUES ( 15, 'Investida Poderosa');
INSERT INTO Habilidade (Dano, DescricaoSkill) VALUES ( 20, 'Técnica da Sombra');
INSERT INTO Habilidade (Dano, DescricaoSkill) VALUES ( 25, 'Explosão Arcana');


-- Inserir dados na tabela Inventario
--INSERT INTO Inventario (Id_Inventario, Capacidade, Id_Jogador) VALUES (1, 50, 1);
--INSERT INTO Inventario (Id_Inventario, Capacidade, Id_Jogador) VALUES (2, 50, 2);


-- Inserir dados na tabela Item
INSERT INTO Item (Id_Item, Tipo) VALUES (1, 'Consumível');
INSERT INTO Item (Id_Item, Tipo) VALUES (2, 'Equipável');
INSERT INTO Item (Id_Item, Tipo) VALUES (3, 'Melhoria');

-- Inserir dados na tabela InstanciaItem
--INSERT INTO InstanciaItem (Id_Item, Id_Inventario, Id_Loot) VALUES ( 1, 1, 1);
--INSERT INTO InstanciaItem (Id_Item, Id_Inventario, Id_Loot) VALUES ( 2, 1, 2);
--INSERT INTO InstanciaItem (Id_Item, Id_Inventario, Id_Loot) VALUES ( 3, 1, 3);

-- Inserir dados na tabela NPC
INSERT INTO NPC (Nome, Tipo, Id_Local) VALUES ('Mago Velho', 'Mago', 3);
INSERT INTO NPC (Nome, Tipo, Id_Local) VALUES ('Guarda Real', 'Soldado', 2);
INSERT INTO NPC (Nome, Tipo, Id_Local) VALUES ('Cidadão Comum', 'Civil', 1);


-- Inserir dados na tabela Treinador
INSERT INTO Treinador (Id_Treinador, Nome, Moedas, Descricao, Historia) VALUES (1, 'Mestre Kuro', 200, 'Um mestre experiente que guia o protagonista em sua jornada.', 'Mestre Kuro é um antigo guerreiro lendário, conhecido por sua habilidade em treinar jovens talentos.');
INSERT INTO Treinador (Id_Treinador, Nome, Moedas, Descricao, Historia) VALUES (2, 'Treinadora Líria', 250, 'Uma treinadora ágil e astuta que desafia o protagonista.', 'Líria é uma treinadora habilidosa, famosa por suas técnicas inovadoras e estilo de luta único.');


-- Inserir dados na tabela Treino
--INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (1, 1, 1);
--INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (2, 1, 1);
--INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (3, 2, 1);
--INSERT INTO Treino (Id_Skill, Id_Treinador, Id_Jogador) VALUES (4, 2, 1);

-- Inserir dados na tabela Mercador
INSERT INTO Mercador (Id_Mercador, Nome, Moedas, Descricao, Historia) VALUES (1, 'Mercador Rurik', 300, 'Um mercador viajante que oferece itens raros e valiosos.', 'Rurik é conhecido em todo o reino por suas mercadorias de alta qualidade e habilidade em negociar.');
INSERT INTO Mercador (Id_Mercador, Nome, Moedas, Descricao, Historia) VALUES (2, 'Mercadora Elara', 280, 'Uma mercadora carismática que vende itens mágicos e encantados.', 'Elara é uma mercadora habilidosa, especializada em itens mágicos e encantados que podem mudar o curso de uma batalha.');

-- Inserir dados na tabela Venda
--INSERT INTO Venda (Id_Mercador, Id_InstanciaItem, Id_Jogador) VALUES (1, 1, 1);
--INSERT INTO Venda (Id_Mercador, Id_InstanciaItem, Id_Jogador) VALUES (2, 2, 1);


-- Inserir dados na tabela Equipavel
INSERT INTO Equipavel (Id_Equipavel, Id_Item, DescricaoItem, Valor, Tipo, Bonus) VALUES (1, 2, 'Espada afiada', 50, 'Equipável', '+10 de Ataque');
INSERT INTO Equipavel (Id_Equipavel, Id_Item, DescricaoItem, Valor, Tipo, Bonus) VALUES (2, 3, 'Escudo resistente', 30, 'Equipável', '+5 de Resistência');

-- Inserir dados na tabela Melhoria
INSERT INTO Melhoria (Id_Melhoria, Id_Item, DescricaoItem, Valor, Tipo, TipoMelhoria) VALUES (1, 1, 'Poção fortificante', 20, 'Melhoria', 'VidaRegenerada');

-- Inserir dados na tabela Consumivel
INSERT INTO Consumivel (Id_Consumivel, Id_Item, DescricaoItem, Valor, TipoConsumivel, VidaRegenerada) VALUES (1, 1, 'Poção de Cura', 15, 'Vida', '+20');
INSERT INTO Consumivel (Id_Consumivel, Id_Item, DescricaoItem, Valor, TipoConsumivel, VidaRegenerada) VALUES (2, 1, 'Poção de Energia', 25, 'Energia', '+15');
