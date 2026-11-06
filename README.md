# 📝 Mini Projeto: Cenários de Teste - Gestão de Ativos

**Autor:** Ícaro Pontes  
**Módulo:** Gestão de Ativos (Turbinas Eólicas)  
**Disciplina:** Verificação e Teste de Software (VTTS)  

Este repositório contém a documentação dos cenários de teste para o módulo de **Gestão de Turbinas Eólicas** do BVapp. Os cenários foram especificados com base nos requisitos funcionais e regras de negócio da Epic 2.1.2.

O primeiro cenário (UCS001) engloba o fluxo completo das quatro operações (CRUD) conforme exigido pela atividade.

## 📋 Lista de Cenários

| Identificador | Título do Cenário | Requisito Relacionado | Arquivo |
| :--- | :--- | :--- | :--- |
| **UCS001** | Manter Turbinas Eólicas (CRUD Completo) | Epic 2.1.2 | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS001_manter_turbinas.py) |
| **UCS002** | Variação de CRUD - Turbina com Capacidade Máxima | Epic 2.1.2 | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS002_crud_variacao.py) |
| **UCS003** | Inclusão com Dados Inválidos | FEATURE-2.1.2.1 | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS003_inclusao_dados_invalidos.py) |
| **UCS004** | Consulta de Turbina Inexistente | FEATURE-2.1.2.2 | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS004_consulta_inexistente.py) |
| **UCS005** | Consulta com Lista Vazia | FEATURE-2.1.2.2 | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS005_consulta_lista_vazia.py) |
| **UCS006** | Atualização com Dados Inválidos | FEATURE-2.1.2.3 | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS006_atualizacao_dados_invalidos.py) |
| **UCS007** | Exclusão de Turbina Inexistente | FEATURE-2.1.2.4 | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS007_exclusao_inexistente.py) |
| **UCS008** | Exportação de Turbinas (Fluxo Padrão) | FEATURE Exportação | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS008_exportacao_1.py) |
| **UCS009** | Exportação - Filtro por Modelo | FEATURE Exportação | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS009_exportacao_2.py) |
| **UCS010** | Exportação com Lista Vazia | FEATURE Exportação | [Acessar](./functional_tests/ativos/turbinas_eolicas/UCS010_exportacao_3.py) |

---
*Documentação elaborada para a avaliação final de requisitos.*