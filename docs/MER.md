## Histórico de versões

| Versão |    Data    | Descrição                | Autor                                              | Revisão |
| :----: | :--------: | ------------------------ | -------------------------------------------------- | ------- |
| `1.0`  | 25/09/2023 | Criação do documento MER | [Samuel Castro](https://github.com/SamuelCastro7) |         |


# Modelo Entidade-Relacionamento (MER)

O **Modelo Entidade-Relacionamento (MER)** em bancos de dados é um modelo conceitual que descreve as entidades de um domínio de negócios, incluindo seus atributos e os relacionamentos que existem entre elas.

**Principais componentes do MER:**

1. **Entidades:** Representam os objetos da realidade que estamos modelando. São elementos fundamentais do domínio de negócios em questão.

2. **Relacionamentos:** Refletem as associações ou conexões entre as entidades. Os relacionamentos indicam como as entidades interagem ou se relacionam umas com as outras.

3. **Atributos:** São características específicas de uma entidade. Eles descrevem informações detalhadas sobre uma entidade e ajudam a definir suas propriedades.

O MER é uma ferramenta essencial na modelagem de dados, permitindo uma representação clara e abstrata das informações de um sistema ou domínio, facilitando assim o projeto e o entendimento de um banco de dados.

## 1. Entidades

- **Mundo**
- **História**
- **Jogador**
- **NPC**
- **Batalha**
- **Região**
- **Loja**
- **Inventário**
- **Equipamentos**
  - **Poção**
  - **Arma**  

## 2. Atributos

- **Mundo**: <ins>nome_mundo</ins>;
- **História**: <ins>ID_história</ins>;
- **Jogador**: <ins>nome_jogador</ins>, <ins>ID_jogador</ins>, nivel, moedas, vida;
- **NPC**: <ins>nome_npc</ins>, <ins>ID_npc</ins>, tipo_npc, nivel_npc, localização;
- **Batalha**: <ins>ID_batalha</ins>, <ins>local_batalha</ins>, vencedor, perdedor;
- **Loja**: <ins>nome_loja</ins>, localização, estoque;
- **Inventário**: <ins>ID_inventário</ins>, <ins>nome_jogador</ins>, equipamento, itens;
- **Equipamento**: <ins>Tipo_Equipamento</ins>, <ins>Nome_equipamento</ins>, atributo;



## 3. Relacionamentos

**Mundo – possui – Região**

- Um mundo possui uma ou várias regiões (1,N).<br>
- Uma região pertence a um só mundo (1,1).
