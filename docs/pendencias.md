# ❓ Registro de Dúvidas e Inconsistências (Stakeholders)

**Autor:** Ícaro Pontes  
**Módulo:** Gestão de Ativos - Turbinas Eólicas  

Conforme orientação da atividade, as dúvidas e lacunas identificadas nos requisitos da Epic 2.1.2 foram registradas abaixo para alinhamento futuro com os stakeholders, evitando a invenção de regras não especificadas:

1. **Dúvida 01 — Política de Exclusão (Física vs. Lógica):**
   * *Inconsistência:* O documento FEATURE-2.1.2.4 não especifica explicitamente se a exclusão de uma turbina eólica deve realizar um *soft delete* (desativação lógica mantendo histórico de geração) ou *hard delete* (remoção física do banco).
   * *Ação Registrada:* Assumiu-se para o cenário UCS001 a exclusão física caso não haja amarras históricas, mas o comportamento para ativos com medições legadas precisa ser homologado com o PO.

2. **Dúvida 02 — Formato Padrão e Limite de Registros na Exportação:**
   * *Inconsistência:* A especificação da FEATURE Exportação não estabelece um limite máximo de linhas para geração de arquivos PDF/XLSX em tempo de execução.
   * *Ação Registrada:* Registrada a dúvida sobre a necessidade de paginação ou assincronismo (background job) para bases contendo mais de 10.000 turbinas.