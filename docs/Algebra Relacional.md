## Histórico de versões

| Versão |    Data    | Descrição                | Autor                                              | Revisão |
| :----: | :--------: | ------------------------ | -------------------------------------------------- | ------- |
| `1.0`  | 30/10/2023 | Criação do documento e adição de consultas iniciais |  [Isabella Carneiro](https://github.com/isabellacgmsa)|         |

# Álgebra Relacional
##  Todos os jogadores que estão em uma determinada região (Região1).
  ```sql
  σ(Id_Regiao = 'Região1')(Jogador ⨝ Local)
  ```

## Todas as habilidades de todos os jogadores, sem duplicatas.
  ```sql
  π(Id_Skill)(Habilidade) ∪ π(Id_Skill)(Jogador.Habilidade)
  ```

## Todas as missões associadas a um jogador específico
  ```sql
  π(Id_Missao, Descricao)(Jogador ⨝ Missao)
  ```

## Todas as missões ativas de jogadores e missões concluídas de jogadores e suas descrições.
  ```sql
  π(Id_Missao, Descricao)(Jogador ⨝ Missao ⨝ (σ(Missao.status = 'Ativa' ∪ Missao.status = 'Concluída')(Jogador)))
  ```

## Jogadores que não têm uma missão ativa.
  ```sql
  π(Id_Jogador)(Jogador) - π(Id_Jogador)(Jogador ⨝ (σ(Missao.status = 'Ativa')(Jogador)))
  ```

## Jogadores que têm uma missão ativa e sua respectiva missão com descrição.
  ```sql
  π(Jogador.Id_Jogador, Jogador.Vida, Missao.Descricao)(Jogador ⨝ (σ(Missao.status = 'Ativa')(Jogador.Missao)))
  ```
