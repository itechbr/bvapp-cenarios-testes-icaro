# ❓ Registro de Dúvidas e Inconsistências (Stakeholders)

**Autor:** Ícaro Pontes  
**Módulo:** Gestão de Ativos - Turbinas Eólicas  

Conforme orientação da atividade e análise do documento de *Walkthrough* de revisão, foram identificadas severas ambiguidades e lacunas nos requisitos originais da Epic 2.1.2. Os cenários de teste foram especificados, mas a execução da automação e a aprovação dos critérios de aceite dependem da resolução formal dos seguintes pontos com os *stakeholders*:

1. **Dúvida 01 — Ambiguidade de Unidades (Potência e Datas):**
   * *Inconsistência:* O CA de Inclusão descreve a potência nominal como valor numérico inteiro em Watts (W), mas a Feature de Exportação exige W/kW sem definir a regra de conversão. Além disso, as regras pedem "Data de Entrada em Operação (anos)", o que aplica equivocadamente uma métrica de duração a um campo de data. A tabela usa mês de 30 dias para garantia sem validação contratual.

2. **Dúvida 02 — Campo "Operadora de Energia" e Vínculos de Posse:**
   * *Inconsistência:* O CA-2.1.2.1.03 exige o preenchimento da Operadora de Energia, mas o efeito prático e o filtro associado a esse campo estão marcados como pendentes. Faltam decisões sobre a aceitação de potência zero e exigências contratuais de cooperados associados.

3. **Dúvida 03 — Autorização e Matriz de Acesso Indefinidas:**
   * *Inconsistência:* O *Walkthrough* constatou que a autorização para incluir turbinas, editar o *status* isoladamente e acessar modalidades de exportação não possui fonte documental aprovada, invalidando testes de segurança (RBAC) neste momento.

4. **Dúvida 04 — Tabela de Decisão para Exclusão e Associações:**
   * *Inconsistência:* Os CA-2.1.2.4.02 e .03 listam bloqueio de exclusão física por "histórico" e "associações críticas" sem delimitar exatamente o que compõe esse conjunto (além de "serviços associados"). 

5. **Dúvida 05 — Interrupção e Comportamento de Exportação Vazia:**
   * *Inconsistência:* A especificação oferece alternativas incompatíveis (bloqueio vs. geração de arquivo vazio) para a exportação sem resultados, e não prevê como o sistema deve reagir na repetição de uma exclusão que foi executada mas cuja resposta de rede foi perdida.