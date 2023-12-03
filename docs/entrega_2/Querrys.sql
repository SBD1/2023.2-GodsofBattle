--Descrição de Locais e Regiões onde XXX representa nomes especificos
SELECT Descricao FROM Regiao WHERE Regiao.Nome = 'XXX';

SELECT Descricao FROM Local WHERE Local.Nome = 'XXX';

--Estatísticas do player
SELECT Vida, Ataque, Resistencia FROM Jogador;

--Missao Ativa e sua descrição
SELECT M.Id_Missao, M.DescricaoMissao FROM Jogador J, Missao M 
WHERE J.Id_Missao = M.Id_Missao AND M.Status = 'ativa'

--Estatísticas do Adversário 
SELECT A.vida, A.Ataque, A.Resistencia 
FROM Jogador J join Missao M ON M.Id_Missao = J.Id_Missao
JOIN Adversario A ON M.Id_Adversario = A.Id_Adversario;

--Itens no Inventario
SELECT item.Id_InstanciaItem
FROM Jogador J JOIN Inventario I ON I.Id_Jogador = J.Id_Jogador
JOIN InstanciaItem AS item ON I.Id_Inventario = item.Id_Inventario;

--NPC no Local
SELECT NPC.Nome 
FROM Jogador J JOIN Local L ON J.Id_Local = J.Id_Local
JOIN NPC ON L.Id_Local = NPC.Id_Local;

--Regiões do Mundo 
Select R.Nome, R.Descricao
FROM Mundo M JOIN Regiao R ON M.Id_Mundo = R.Id_Mundo;
