# DD - Dicionário de dados

## Entidade: Mundo
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Mundo    |     int      | Identificador do mundo |   PK    |
|   Nome    |     varchar      | Nome do mundo |                   |
|   Historia    |     varchar      |  |                   |

## Entidade: Região
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Nome    |     varchar      |      Nome da região       |      PK             |
|   Descrição    |     varchar      |      Descriçãi da região       |                   |
|   Id_Mundo    |     int      |  Mundo a qual a região pertence |      FK             |

## Entidade: Local
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Local    |     int      | Identificador do local |   PK    |
|   Nome    |     varchar      |      Nome do local       |                   |
|   Descrição    |     varchar      |      Descriçãi da região       |                   |


## Entidade: Jogador
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Jogador    |     int      | Identificador do jogador |   PK    |
|   Vida    |     int      |  |       |
|   Ataque    |     int      |  |       |
|   Resistência    |     int      |  |       |
|   Habilidade    |     int      |  |       |
|   Id_Local    |     int      |  Local que o jogador pertence |      FK             |
|   Id_Missão   |     int      |  Missão que o jogador tem que cumprir |      FK             |


## Entidade: Adversário
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Jogador    |     int      | Identificador do adversário |   PK    |
|   Vida    |     int      |  |       |
|   Ataque    |     int      |  |       |
|   Resistência    |     int      |  |       |
|   Descrição    |     int      |  |       |
|   Id_Local    |     int      |  Local que o adversário pertence |      FK             |

## Entidade: Missão
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|   Id_Missão    |     int      | Identificador da missão |   PK    |
|   DescriçãoMissão    |     int      |  |       |
|   Requisito    |     int      |  |       |
|   Status    |     int      |  |       |
|   Id_Adversário   |     int      |  Adversário a ser enfrentado na missão |      FK             |
|   Id_MissãoRequisito   |     int      | Missão que deve ter sido cumprida para aquela  |      FK             |


## Entidade: Batalha
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|       |           |             |                   |

## Entidade: Habilidade
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|       |           |             |                   |

## Entidade: Inventário
### Descrição: 
### Observação: 
| Nome Variável |     Tipo     |         Descrição          |  Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: |
|       |           |             |                   |
