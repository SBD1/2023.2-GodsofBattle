## Histórico de versões

| Versão |    Data    | Descrição                | Autor                                              | Revisão |
| :----: | :--------: | ------------------------ | -------------------------------------------------- | ------- |
| `1.0`  | 29/09/2023 | Criação do documento DER |  [Isabella Carneiro](https://github.com/isabellacgmsa)|         |
| `1.1`  | 02/10/2023 | Criação do documento DER | [Luana Torres](https://github.com/luanatorress) e [Samuel Castro](https://github.com/SamuelCastro7) e [Thiago Vivan](https://github.com/thiago-vivan) e [Isabella Carneiro](https://github.com/isabellacgmsa)|         |


# DD - Dicionário de dados

## Entidade: Mundo
### Descrição: Representa o único universo no qual o jogo se desenrola. Este mundo abriga todos os elementos, personagens e eventos do jogo, servindo como o cenário principal para as interações dos jogadores.

| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Mundo    |     int      | Identificador do mundo |   PK    |
|   Nome    |     varchar      | Nome do mundo |         -          |
|   Historia    |     varchar      |    História do jogo    |           -        |

## Entidade: Região
### Descrição: Uma área específica dentro do mundo do jogo onde os personagens interagem e exploram. As regiões delimitam espaços geográficos distintos dentro do universo do jogo.
### Observação: Esta tabela possui uma chave estrangeira (FK) que se relaciona com a tabela "Mundo", indicando a associação das regiões com o mundo principal do jogo.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Nome    |     varchar      |      Nome da região       |      PK             |
|   Descrição    |     varchar      |      Descrição da região       |           -        |
|   Id_Mundo    |     int      |  Mundo a qual a região pertence |      FK             |

## Entidade: Local
### Descrição: Representa um lugar específico dentro de uma região no mundo do jogo. Locais são pontos de interesse onde os personagens podem realizar ações e interagir com o ambiente
### Observação: Esta tabela possui uma chave estrangeira (FK) que se relaciona com a tabela "Região", indicando a associação dos locais com as Regiões do jogo
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Local    |     int      | Identificador do local |   PK    |
|   Nome    |     varchar      |      Nome do local       |         -          |
|   Descrição    |     varchar      |      Descrição do local       |         -          |


## Entidade: Jogador
### Descrição: Representa o personagem principal no mundo do jogo.
### Observação: Possui uma Fk vinda da tabela Local e uma da tabela Missão permitindo a conexão dos jogadores com os locais e missões relevantes no mundo do jogo.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Jogador    |     int      | Identificador do jogador |   PK    |
|   Vida    |     int      |   Numero de pontos de vida    |     -  |
|   Ataque    |     int      |   Dano causado a vida do adversario   |     -  |
|   Resistência    |     int      |   resistencia a dano recebido    |   -    |
|   Habilidade    |     int      |  Poderes ofensivos aprendidos   |    -   |
|   Id_Local    |     int      |  Local que o jogador pertence |      FK             |
|   Id_Missão   |     int      |  Missão que o jogador tem que cumprir |      FK             |


## Entidade: Adversário
### Descrição: Representa um oponente ou inimigo que o jogador pode encontrar e enfentar no mundo do jogo.
### Observação: A utilização de uma chave estrangeira (FK) advinda da tabela local conecta os adversários ao local específico onde podem ser encontrados no jogo.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Jogador    |     int      | Identificador do adversário |   PK    |
|   Vida    |     int      |  |   -    |
|   Ataque    |     int      |  |  -     |
|   Resistência    |     int      |  | -      |
|   Descrição    |     varchar      |  |  -     |
|   Id_Local    |     int      |  Local que o adversário pertence |      FK             |

## Entidade: Missão
### Descrição: Representa tarefas e objetivos que o jogador deve cumprir para avançar no jogo.
### Observação: A chave estrangeira (FK) para a tabela "Adversário" indica qual adversário deve ser derrotado para completar a missão, enquanto a FK para a própria tabela "Missão" estabelece requisitos de missões anteriores que devem ser cumpridos antes de iniciar a missão atual.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Missão    |     int      | Identificador da missão |   PK    |
|   DescriçãoMissão    |     varchar      | Descrição da missão  |    -   |
|   Requisito    |     int      |  |    -   |
|   Status    |     int      |  |  -     |
|   Id_Adversário   |     int      |  Adversário a ser enfrentado na missão |      FK       |
|   Id_MissãoRequisito   |     int      | Missão que deve ter sido cumprida anteriormente |    FK    |


## Entidade: Loot
### Descrição: Representa os itens ou recompensas que os jogadores obtêm após vencer uma batalha. Os loots são geralmente itens valiosos que podem melhorar o progresso ou as habilidades dos jogadores.
### Observação:  A chave estrangeira (FK) para a tabela "Batalha" vincula o loot à batalha específica em que foi obtido.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Loot   |     int      | Identificador do loot |   PK    |
|   Id_Batalha   |     int      |  Batalha em que ocorreu o loot |      FK       |

## Entidade: Batalha
### Descrição: Representa um confronto no jogo envolvendo um jogador e um adversário. As batalhas são eventos significativos onde a ação e a estrátegia são testadas, esseciais para o desenvolver do jogo.
### Observação: As chaves estrangeiras (FKs) vinculam as batalhas aos jogadores e adversários envolvidos na ação.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Batalha    |     int      | Identificador da batalha |   PK    |
|   Id_Adversário   |     int      |  Adversário a ser enfrentado na batalha |      FK       |
|   Id_Jogador  |     int      |  Jogador que está na batalha |      FK       |


## Entidade: Treino
### Descrição: Tabela que indica o relacionamento entre o treinador, jogador e habilidade, representando o jogador aprendendo habilidades novas.
### Observação: As chaves estrangeiras (FKs) relacionam o jogador com a habilidade que está sendo aprimorada e o treinador que está conduzindo o treinamento. Isso permite acompanhar a evolução das habilidades dos jogadores ao longo do tempo.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Skill    |     int      | Identificador da skill a ser aprimorada |   FK    |
|   Id_Treinador   |     int      |  Treinador que ajudará o jogador |      FK       |
|   Id_Jogador  |     int      |  Jogador que está no treino |      FK       |

## Entidade: Habilidade
### Descrição: Habilidades que o personagem principal pode desbloquear e usar contra inimigos
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|    Id_Skill   |      int     |   Identificador da Habilidade    |  PK    |
|  Dano         |  int         |  Quantidade de pontos de vida retirados do adversário ao utilizar a habilidade   |   -   | 
|  DescricaoSkill |  varchar   |  Descricao da Habilidade   |    -  | 


## Entidade: Inventário
### Descrição: Local onde o Jogador guarda e carrega seus itens
### Observação: a chave estrangeira (FK) que conecta o inventário ao jogador proprietário do inventário, permitindo rastrear o inventário do jogador.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
| Id_inventario  |  int   |  Identificador unico  do inventário  |      | 
|       Capacidade      |      int       |        Quantas instancias de item cabem no inventário     |  |
|  Id_Jogador |   int  |  Identificador unico do Jogador   |   FK   | 


## Entidade: IntanciaItem
### Descrição: Essa entidade representa uma instância de um item.
### Observação: as chaves estrangeiras (FKs) que conectam a instância de item à tabela "Item" para identificar o item associado, à tabela "Inventário" para indicar onde a instância de item está armazenada e à tabela "Loot" para rastrear a fonte de onde a instância de item foi obtida. Isso permite um gerenciamento detalhado das instâncias de itens no jogo.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
| Id_IntanciaItem |  int   | Identificador unico da instancia | PK |
| Id_Item | int | Identificador Unico do item | FK |
| Id_Inventario | int  | Identificador unico do inventario | FK |
| Id_Loot | int | Identificador unico do loot | FK |

## Entidade: NPC
### Descrição: Personagem não jogavel, responsaveis por desempenhar papeis específicos no jogo.
### Observação: a chave estrangeira (FK) que conecta o NPC à tabela "Local" para indicar onde o NPC está localizado no mundo do jogo.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Nome    |     varchar      |      Nome do NPC       |      PK             |
|   Tipo    |     varchar      | Tipo do NPC |  -     |
|   Id_Local    |     int      |  Local que o NPC pertence |      FK             |

## Entidade: Treinador
### Descrição: NPC responsável por treinar o jogador e ensinar novas habilidades.
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Treinador    |     int      |       Identificador do treinador      |      PK             |
|   Nome    |     varchar      | Nome do treinador |  FK     |
|   Moedas    |     int      | Quantidade de dinheiro do npc  |             -      |
|   Descrição    |     varchar      |  Descricao fisica do npc |      -            |
|   História    |     varchar      | trechos de historias relacionadas ao npc  |      -            |

## Entidade: Mercador
### Descrição: NPC responsavel pela loja do jogo
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Mercador    |     int      |       Identificador do Mercador      |      PK             |
|   Nome    |     varchar      | Nome do Mercador |  FK     |
|   Moedas    |     int      | Quantidade de dinheiro do npc  |      -             |
|   Descrição    |     varchar      | Descricao fisica do npc |      -            |
|   História    |     varchar      |  trechos de historias relacionadas ao npc  |      -            |


## Entidade: Venda
### Descrição: Tabela gerada pela interação entre um mercador, jogador e intancia de item, indicando uma compra ou venda
### Observação: Possui uma (FK) vinda da tabela Mercador, outra (FK) vinda da tabela intanciaItem e outra (FK) vinda da tabela jogador.
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Mercador    |     int      |      Mercador que está vendendo     |      FK             |
|   Id_InstanciaItem  |     int      |       Item que está sendo vendido     |      FK             |
|   Id_Jogador   |     int      |       Jogador que está comprando      |      FK             |

## Entidade: Equipamento
### Descrição: Itens disponiveis para o jogador
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Item   |     int      |      Identificador do item     |      PK             |
|   Tipo  |     varchar      |       Tipo do item    |      -             |

## Entidade: Equipável
### Descrição: Itens que são ativamente equipados pelo jogador e fornecem bonus de ataque ou resistencia
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Equipavel   |     int      |      Identificador do item equipável     |      PK             |
|   Id_Item   |     int      |      Identificador do item     |      FK             |
|   DescriçãoItem  |     varchar      |   Descrição fisica do item   |      -             |
|   Valor  |     int      |   Valor que custa o item   |      -             |
|   Tipo  |     varchar      |   Tipo do item   |      -             |
|   Bonus  |     varchar      |   Bonus de vida ou ataque fornecido pelo item   |      -             |

## Entidade: Melhoria
### Descrição: Item que são utilizados para melhorar itens equipaveis
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Melhoria   |     int      |      Identificador do item de Melhoria     |      PK             |
|   Id_Item   |     int      |      Identificador do item     |      FK             |
|   DescriçãoItem  |     varchar      |   Descrição fisica do item   |      -             |
|   Valor  |     int      |   Valor que custa o item   |      -             |
|   Tipo  |     varchar      |  Tipo do item    |      -             |
|   TipoMelhoria  |     varchar      |      |      -             |

## Entidade: Consumivel
### Descrição: Item ao qual o jogador pode utilizar para recuperar pontos de vida em batalha
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Consumivel   |     int      |      Identificador do item de Consumivel     |      PK             |
|   Id_Item   |     int      |      Identificador do item     |      FK             |
|   DescriçãoItem  |     varchar      |  Descrição fisica do item    |      -             |
|   Valor  |     int      |   Valor que custa o item   |      -             |
|   TipoConsumivel  |     varchar      |      |      -             |
|   VidaRegenerada  |     varchar      |      |      -             |
