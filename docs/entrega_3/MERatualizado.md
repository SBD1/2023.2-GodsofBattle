## Histórico de versões

| Versão |    Data    | Descrição                | Autor                                              | Revisão |
| :----: | :--------: | ------------------------ | -------------------------------------------------- | ------- |
| `1.0`  | 25/09/2023 | Criação do documento MER | [Samuel Castro](https://github.com/SamuelCastro7)  |         |
| `1.1`  | 30/09/2023 |    Atualização do MER    | [Luana Torres](https://github.com/luanatorress)    |         |
| `1.2`  | 02/10/2023 |    Atualização do MER    | [Samuel Castro](https://github.com/SamuelCastro7)    |         |
| `1.3`  | 03/12/2023 |    Atualização do MER pós feedback do professor   | [Luana Torres](https://github.com/luanatorress)    |         |



# Modelo Entidade-Relacionamento (MER)

O **Modelo Entidade-Relacionamento (MER)** em bancos de dados é um modelo conceitual que descreve as entidades de um domínio de negócios, incluindo seus atributos e os relacionamentos que existem entre elas.

**Principais componentes do MER:**

1. **Entidades:** Representam os objetos da realidade que estamos modelando. São elementos fundamentais do domínio de negócios em questão.

2. **Relacionamentos:** Refletem as associações ou conexões entre as entidades. Os relacionamentos indicam como as entidades interagem ou se relacionam umas com as outras.

3. **Atributos:** São características específicas de uma entidade. Eles descrevem informações detalhadas sobre uma entidade e ajudam a definir suas propriedades.

O MER é uma ferramenta essencial na modelagem de dados, permitindo uma representação clara e abstrata das informações de um sistema ou domínio, facilitando assim o projeto e o entendimento de um banco de dados.

## 1. Entidades

- **Região**
- **Local**
- **Jogador**
- **NPC**
  - **Mercador**
  - **Treinador**  
  - **Adversário**
- **Batalha**
- **Inventário**
- **Habilidades**
- **Equipamentos**
  - **Consumível**
  - **Equipável**  
  - **Melhoria**
- **Missão**
- **Loot**
- **InstanciaItem**

## 2. Atributos

- **Região**: <ins>Nome</ins>, Descrição;
- **Local**: <ins>Id_Local</ins>, Descrição;
- **Jogador**:  <ins> Id_Jogador </ins>, Vida, Ataque, Resistencia, MissaoAtiva;
- **NPC**: <ins>Nome</ins>, Historia, Descricao, Moedas;
    - **Mercador**
    <ins>Id_mercador</ins>;
    - **Treinador**
    <ins>Id_Treinador</ins>;
    - **Adversário**
    <ins>Id_Adversario</ins>, Vida, Ataque, Resistencia;
- **Batalha**: <ins>Id_Batalha</ins>, Id_jogador, Id_adversario;
- **Inventário**: <ins>Id_Jogador</ins>, Capacidade;
- **Habilidade**: <ins>Id_Skill</ins>, Dano, DescricaoSkill;
- **Equipamentos**: <ins>Id_Item</ins>, Descricao, Valor, Tipo;
  - **Consumível**
  <ins>Id_Consumivel</ins>, TipoConsumivel, VidaRegenerada;
  - **Equipável**  
 <ins>Id_Equipavel</ins>, TipoEquipavel, Descricao, Bonus;
  
  - **Melhoria**
  <ins>Id_Melhoria</ins>, TipoMelhoria;

- **Missão**: <ins>Id_Missao</ins>, Descricao, ProximaMissao, Status;
- **Inventário**: <ins> Id_Jogador</ins>, Capacidade;
- **Loot**: <ins>Id_Loot</ins>;
- **InstanciaItem**: <ins>Id_loot</ins>, Id_InstanciaItem;
- **vende**: Id_jogador, Id_InstanciaItem, Id_mercador;
- **Treino**: ID_jogador, Id_skill, Id_treinador;






## 3. Relacionamentos

**Regiao – possui – Local**

- Uma região possui um ou vários locais (1,N).
- Uma local pertence a uma região (1,1).


**Local – contém – NPC**

- Um local contém zero ou vários NPCs (0,N).
- Um NPC está em um só local (1,1).

**Treinador – treina – Jogador**

- Um treinador treina zero ou mais jogadores (0,N).
- Um jogador é treinado por um ou mais treinadores (0,N).

**Jogador – treina – Habilidade**

- Um jogador treina uma ou mais habilidades (1,N).
- Uma habilidade é treinada por um ou mais jogadores (1,N).

**Jogador – possui – Inventário**

- Um jogador possui um inventário (1,1).
- Um inventário pertence a um jogador (1,1).

**Jogador – possui – Missao**

- Um jogador tem uma missão (1,1).
- Uma missão tem um ou mais jogadores (1,N).

**Jogador – luta – Adversário**
- Um jogador luta com um adversário (1,1).
- Um adversário luta com um jogador (1,1).

**Jogador – está em – Local**

- Um local tem um jogador (1,1).
- Uma jogador está em um só local (1,1).

**Jogador - compra - IntanciaItem**

- Um jogador compra 1 ou mais InstanciaItem (1,n).
- Uma IntanciaItem é comprada por um ou mais jogadores (1,n).

**Missao – desbloqueia – Missao**

- Uma missão atual desbloqueia uma missão posterior (1,1).
- Uma missão nova é desbloqueada por uma missão anterior (1,1).

**Missão – indica – Adversário**

- Uma missão indica um adversário (1,1).
- Um adversário é indicado por uma missão (1,1).

**Adversario – está em – Local**

- Um adversário está em um local (1,1).
- Um local tem um só adversário (1,1).

**Batalha – dropa – Loot**

- Um adversário dropa um loot (1,1)
- Um loot é dropado por um ou mais adversários (1,N).

**Loot – possui – InstanciaItem**

- Um loot possui uma ou mais InstanciaItem (1,N).
- Uma InstanciaItem possui um loot (1,1).

**Mercador – vende – InstanciaItem**

- Um mercador vende uma ou mais InstanciaItem (1,N).
- Uma InstanciaItem é vendida por um mercador (1,1).

**Inventario – carrega – InstanciaItem**

- Um inventário carrega zero ou mais InstanciaItem (0,N).
- Uma InstanciaItem é carregada por um inventário (1,1).

**InstanciaItem – tipifica – Equipamento**

- Uma InstanciaItem tipifica zero ou mais equipamentos (0,N).
- Um equipamento é tipifica por uma InstanciaItem (1,1).
