# 🎙️ Roteiro de Apresentação — 5 Minutos

**Aluno:** Ícaro Pontes  
**Disciplina:** Verificação, Validação e Teste de Software (VVTS)  
**Módulo:** Gestão de Ativos — Turbinas Eólicas (EPIC-2.1.2)  

---

### [0:00 - 0:50] Introdução e Alinhamento Arquitetural
- "Boa tarde a todos e ao professor. Apresento meu mini projeto individual de especificação de cenários de teste para o módulo de **Gestão de Turbinas Eólicas** do BVapp.
- Seguindo rigorosamente as diretrizes da disciplina e o feedback do professor:
  1. Unificamos todo o ciclo de vida do ativo em **1 único teste de CRUD completo (`UCS001 — Manter turbinas eólicas`)**.
  2. As funcionalidades que não são CRUD foram organizadas em **testes separados para cada funcionalidade**, gerando o teste de **Exportação Coletiva da Consulta (`UCS002`)** e o teste de **Exportação da Ficha Técnica Individual (`UCS003`)**.
  3. Não existem testes individuais isolados de inclusão, consulta, edição ou exclusão; todas as validações de regras de negócio viraram fluxos alternativos dentro do CRUD."

---

### [0:50 - 2:40] Demonstração do Cenário de CRUD (UCS001)
- "No arquivo `UCS001_manter_turbinas_eolicas.py`, adotamos estritamente a convenção do exemplo da aula:
  - Cabeçalho em docstring contendo identificador, objetivo, requisitos relacionados e ator.
  - **Fluxo Principal (`[FP]`):** É a **Inclusão** (passos 1 a 5 comentados por linha `#`), demonstrando o preenchimento dos campos obrigatórios, herança de usina a partir do inversor e confirmação de sucesso.
  - **Fluxos Alternativos (`[A...]`):** A partir do passo 6, também em comentários de linha (`#`), cobrimos:
    - Consulta e Detalhamento (`[A1]`), Atualização (`[A2]`) e Exclusão (`[A3]`).
    - Validações de campos obrigatórios (`[A4]`), duplicidade de número de série (`[A5]`) e potência inválida (`[A6]`).
    - Cronologia temporal de datas (`[A7]`) e consistência do par de garantia (`[A8]`).
    - Alteração rápida de status com confirmação e cancelamento (`[A10]`, `[A11]`).
    - Bloqueio de exclusão física para turbinas com histórico de ordens de serviço (`[A13]`)."

---

### [2:40 - 4:00] Funcionalidades Não-CRUD (UCS002 e UCS003)
- "Para o que não é CRUD, estruturamos testes dedicados por funcionalidade:
  - **UCS002 — Exportar Consulta:** Cobre a extração em lote da listagem filtrada para arquivos CSV (com as 13 colunas obrigatórias) e PDF consolidado, assegurando abrangência além da página visível, filtros combinados (AND), prevenção contra duplo clique e tratamento de consulta vazia.
  - **UCS003 — Exportar Ficha Individual:** Cobre a geração diagramada da ficha técnica em PDF de um equipamento específico na tela de detalhes, garantindo o isolamento dos dados da turbina selecionada e tratamento para identificadores inexistentes."

---

### [4:00 - 5:00] Rastreabilidade, Dúvidas de Requisitos e Encerramento
- "Em `docs/matriz-rastreabilidade.md`, todos os critérios de aceitação da Epic 2.1.2 estão mapeados aos fluxos.
- Em `docs/pendencias.md`, registrei ambiguidades reais encontradas na especificação de origem, como a conversão de unidades de potência (W para kW) e as regras de exclusão definitiva.
- A entrega é puramente documental, padronizada e pronta para fundamentar futuras etapas de automação de testes funcionais. Muito obrigado!"
