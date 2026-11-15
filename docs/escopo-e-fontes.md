# Escopo e Fontes

## 1. Autoridade e Diretrizes

A atividade avaliativa da disciplina de Verificação, Validação e Teste de Software (VVTS) estabelece as seguintes premissas metodológicas:
- **Cenário de CRUD Único:** Se um requisito ou conjunto funcional envolver operações de CRUD, todas as quatro operações (criar, consultar, atualizar e excluir) devem ser descritas no mesmo cenário como um ciclo completo. Não se criam testes individuais de incluir, consultar, editar e excluir, pois todos se enquadram em CRUD; no máximo, tornam-se fluxos alternativos.
- **Fluxo Principal no Manter:** O fluxo principal no cenário de Manter é estritamente a **Inclusão** (passos 1 a 5 comentados por linha `#`). As operações de Consultar, Editar e Excluir são fluxos alternativos a partir do passo 6.
- **Funcionalidades Não-CRUD:** O que não for CRUD fica organizado em testes separados para cada funcionalidade.

## 2. Cenários Desenvolvidos

Este mini projeto contempla:
1. **`UCS001 — Manter turbinas eólicas` (CRUD Completo):**
   Engloba integralmente as Features 2.1.2.1, 2.1.2.2, 2.1.2.3 e 2.1.2.4 do BVapp.
   - Fluxo Principal (Passos 1 a 5 comentados por linha): Inclusão com campos válidos.
   - Fluxos Alternativos (Passo 6 em diante comentados por linha): Consulta, Edição, Exclusão, Validação de campos vazios, Unicidade de número de série, Potência negativa, Cronologia de datas, Pares de garantia, Vínculo com inversor/usina, Alteração de status com confirmação e cancelamento, Exclusão com impedimentos de ordens de serviço ativas e Controle de permissões.
2. **`UCS002 — Exportar consulta de turbinas eólicas` (Funcionalidade Não-CRUD):**
   Extração da listagem de turbinas eólicas filtradas em CSV e PDF, assegurando abrangência além da página visível, aplicação de filtros combinados e tratamento de concorrência e consulta vazia.
3. **`UCS003 — Exportar ficha técnica individual de turbina eólica` (Funcionalidade Não-CRUD):**
   Geração em formato PDF da ficha técnica completa e isolada de uma turbina selecionada na tela de detalhes, contemplando parâmetros de engenharia e seções complementares de histórico.

## 3. Fontes de Requisitos da Epic 2.1.2

- **FEATURE-2.1.2.1:** Inclusão de turbinas eólicas (CA-2.1.2.1.01 a .19)
- **FEATURE-2.1.2.2:** Consulta de turbinas eólicas (CA-2.1.2.2.01 a .13 e US #28740)
- **FEATURE-2.1.2.3:** Atualização de turbinas eólicas (CA-2.1.2.3.01 a .14 e US #29056)
- **FEATURE-2.1.2.4:** Exclusão de turbinas eólicas (CA-2.1.2.4.01 a .06)
- **FEATURE:** Exportação de turbinas eólicas (Formatos; Filtros; Ficha individual; Entrega)

## 4. Referências Didáticas

- [Aula 06 — Introdução ao TDD (Prof. Maxwell Amaral)](https://maxwellamaral.github.io/aula-eng-testes/docs/06-introducao-tdd/).
- [Exemplo de Referência: UCS001 — Manter produtos](https://raw.githubusercontent.com/maxwellamaral/maxwellamaral.github.io/refs/heads/main/specs/tests/products/UCS001-manter-produtos.py).
