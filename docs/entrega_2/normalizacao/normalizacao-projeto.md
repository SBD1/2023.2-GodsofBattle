## Histórico de versões

| Versão |    Data    | Descrição                | Autor                                              | Revisão |
| :----: | :--------: | ------------------------ | -------------------------------------------------- | ------- |
| `1.0`  | 30/10/2023 | Criação do documento Normalização | [Luana Torres](https://github.com/luanatorress)| [Samuel Castro](https://github.com/SamuelCastro7) |

# Normalização 

A normalização é uma teoria muito utilizada em bancos de dados para formalizar uma melhoria num projeto, tem como obejtivo evitar redundâncias e garantir consistência.

Para normalizar o projeto, o primeiro a se fazer é identificar as dependências funcionais. A partir das tabelas definidas no [Modelo Relacional](../MREL.md), encontraram-se as seguintes dependências funcionais:

## Dependências Funcionais:

- **Tabela Mundo**: Id_Mundo → Nome, História
- **Tabela Região**: Nome → Descrição, Id_Mundo
- **Tabela Local**: Id_Local → Nome, Descrição, Id_Região
- **Tabela Jogador**: Id_Jogador → Vida, Ataque, Resistência, Habilidade, Id_Local, Id_Missão
- **Tabela Adversário**: Id_Adversário → Vida, Ataque, Resistência, Descrição, Id_Local
- **Tabela Local**:
- **Tabela Missão**: Id_Missão → DescriçãoMissão, Requisito, Status, Id_Adversário, Id_MissãoRequisito
- **Tabela Batalha**: Id_Batalha → Id_Adversário
- **Tabela Habilidade**: Id_Skill → Dano, DescricaoSkill
- **Tabela Inventário**: Id_inventario → Capacidade, Id_Jogador
- **Tabela InstanciaItem**: Id_IntanciaItem → Id_Item, Id_Inventario, Id_Loot
- **Tabela NPC**: Nome → Tipo, Id_Local
- **Tabela Treinador**: Id_Treinador → Nome, Moedas, Descrição, História
- **Tabela Mercador**: Id_Mercador → Nome, Moedas, Descrição, História
- **Tabela Equipamento**: Id_Item → Tipo
- **Tabela Equipável**: Id_Equipavel, Id_Item → DescriçãoItem, Valor, Tipo, Bonus 
- **Tabela Melhoria**: Id_Melhoria, Id_Item → DescriçãoItem, Valor, Tipo, TipoMelhoria
- **Tabela Consumível**: Id_Consumivel, Id_Item → DescriçãoItem, Valor, TipoConsumivel, VidaRegenerada

Analisando as tabelas e dependências funcionais fornecidas, foram utilizadas as regras das Formas Normais de 1 a 4. Analisou-se se todos os atributos são monovalorados e atômicos, se atributos comuns não dependem parcialmente de qualquer chave, se atributos comuns não dependem transitivamente de qualquer superchave e se não possui dependências multivaloradas.

## Conclusão

As tabelas não possuem dependências transitivas ou dependências paciais. Também não possuem dependências multivaloradas e seus atributos são monovalorados e atômicos. Desta forma, as tabelas apresentadas já estão normalizadas.