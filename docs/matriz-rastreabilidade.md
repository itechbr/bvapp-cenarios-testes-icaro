# 🔍 Matriz de Rastreabilidade de Testes

**Autor:** Ícaro Pontes  
**Módulo:** Gestão de Ativos - Turbinas Eólicas  

Esta matriz mapeia a relação entre os cenários de teste funcionais e os requisitos especificados na Epic 2.1.2.

| Cenário | Título do Cenário | Requisito Relacionado | Tipo de Teste |
| :--- | :--- | :--- | :--- |
| **UCS001** | Manter Turbinas Eólicas (CRUD Completo) | FEATURE-2.1.2.1 / 2.1.2.2 / 2.1.2.3 / 2.1.2.4 | Fluxo Principal / Integracional |
| **UCS002** | Variação de CRUD - Limites Operacionais | FEATURE-2.1.2.1 / 2.1.2.2 / 2.1.2.3 / 2.1.2.4 | Fluxo de Exceção / Limites Numéricos |
| **UCS003** | Inclusão com Dados Inválidos | FEATURE-2.1.2.1 | Fluxo Alternativo / Validação UI/API |
| **UCS004** | Consulta de Turbina Inexistente | FEATURE-2.1.2.2 | Fluxo Alternativo / Tratamento HTTP 404 |
| **UCS005** | Consulta com Lista de Turbinas Vazia | FEATURE-2.1.2.2 | Estado Inicial / Interface Neutra |
| **UCS006** | Atualização com Dados Inválidos | FEATURE-2.1.2.3 | Fluxo Alternativo / Validação de Edição |
| **UCS007** | Exclusão de Turbina Inexistente | FEATURE-2.1.2.4 | Fluxo de Erro / Integridade Referencial |
| **UCS008** | Exportação de Relatório (Fluxo Padrão) | FEATURE Exportação | Fluxo Principal / Relatórios CSV/PDF |
| **UCS009** | Exportação com Filtro Ativo | FEATURE Exportação / FEATURE-2.1.2.2 | Fluxo Combinado / Extração Filtrada |
| **UCS010** | Exportação com Lista Vazia | FEATURE Exportação | Regra de Negócio / Bloqueio de Extração |