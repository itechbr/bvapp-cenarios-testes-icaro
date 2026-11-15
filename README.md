# BVAPP — Cenários de Teste de Ícaro

Mini projeto individual da atividade **Elaboração de cenários de teste do BVapp**, da disciplina **Verificação, Validação e Teste de Software (VVTS)**.

**Responsável acadêmico:** Ícaro Pontes.  
**Data:** 15/11/2026.  
**Módulo:** Gestão de Ativos — Turbinas Eólicas (EPIC 2.1.2).  

## 🎯 Arquitetura da Entrega

Em conformidade direta com o feedback do professor:
1. **1 Cenário de CRUD Completo (`UCS001 — Manter turbinas eólicas`):**
   - **Fluxo Principal (`[FP]`):** É a **Inclusão** do ativo (passos 1 a 5 comentados por linha `#`).
   - **Fluxos Alternativos (`[A...]`):** A partir do passo 6, comentados por linha (`#`), abrangem a **Consulta**, **Atualização/Edição**, **Exclusão** e todas as variações de validação de regras de negócio (campos vazios, duplicidade de série, valores negativos, cronologia de datas, par de garantias, inversor inativo, alteração rápida de status com confirmação/cancelamento, impedimentos de exclusão por histórico e controle de autorização). Não existem testes separados para incluir, consultar, editar ou excluir, pois todos se enquadram no CRUD.
2. **Cenários Isolados para Funcionalidades Não-CRUD:**
   - **`UCS002 — Exportar consulta de turbinas eólicas`:** Funcionalidade de extração em lote da consulta filtrada nos formatos CSV e PDF.
   - **`UCS003 — Exportar ficha técnica individual de turbina eólica`:** Funcionalidade de emissão diagramada da ficha técnica de um ativo selecionado em PDF.

> **Nota:** Não há implementação de código executável do produto, interface gráfica ou automação de testes. Os arquivos `.py` guardam exclusivamente documentação de especificação de testes, estruturados com cabeçalho em docstring e fluxos comentados por linha (`#`), estritamente conforme o padrão da Aula 06 do professor (`UCS001-manter-produtos.py`).

---

## 📋 Lista de Cenários de Teste

| Identificador | Título do Cenário | Arquivo | Natureza | Descrição Resumida |
| :--- | :--- | :--- | :--- | :--- |
| **UCS001** | [Manter turbinas eólicas](functional_tests/ativos/turbinas_eolicas/UCS001_manter_turbinas_eolicas.py) | `UCS001_manter_turbinas_eolicas.py` | CRUD Completo | FP: Inclusão (passos 1 a 5). Alternativos: Consulta, Atualização, Exclusão, validações de campos, unicidade, datas, garantias, status e controle de acesso. |
| **UCS002** | [Exportar consulta de turbinas eólicas](functional_tests/ativos/turbinas_eolicas/UCS002_exportar_consulta_turbinas_eolicas.py) | `UCS002_exportar_consulta_turbinas_eolicas.py` | Funcionalidade Não-CRUD | FP: Exportação CSV da consulta com filtros além da página. Alternativos: PDF coletivo, filtros combinados, consulta vazia e concorrência. |
| **UCS003** | [Exportar ficha técnica individual de turbina eólica](functional_tests/ativos/turbinas_eolicas/UCS003_exportar_ficha_individual_turbina.py) | `UCS003_exportar_ficha_individual_turbina.py` | Funcionalidade Não-CRUD | FP: Geração em PDF da ficha técnica completa de ativo selecionado. Alternativos: seções complementares, ativo inexistente e acesso negado. |

---

## 🧭 Como Revisar o Projeto

1. Ler [Escopo e Fontes](docs/escopo-e-fontes.md) para contextualização dos requisitos da Epic 2.1.2.
2. Abrir cada arquivo `.py` em `functional_tests/ativos/turbinas_eolicas/`:
   - Verificar a docstring inicial de cabeçalho.
   - Acompanhar os passos 1 a 5 do Fluxo Principal em comentários de linha (`#`).
   - Acompanhar os Fluxos Alternativos a partir do passo 6 em comentários de linha (`#`).
   - Conferir as Regras de Negócio em comentários de linha (`#`).
3. Consultar a [Matriz de Rastreabilidade](docs/matriz-rastreabilidade.md) para verificar a aderência aos Critérios de Aceitação (CAs).
4. Analisar o catálogo de [Pendências](docs/pendencias.md) dos requisitos.
5. Consultar o [Roteiro de Apresentação de 5 Minutos](docs/roteiro-apresentacao.md).
