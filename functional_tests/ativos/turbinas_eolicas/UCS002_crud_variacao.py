"""
UCS002 — Manter turbinas eólicas com validação de campos e regras de unicidade

Autoria / responsável acadêmico: Ícaro Pontes
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Grupo de requisitos: Gestão de Turbinas Eólicas — EPIC 2.1.2.

OBJETIVO
Exercitar o ciclo CRUD focando nas validações de campos obrigatórios,
unicidade do número de série, regras de potência e comportamento do
campo Status durante inclusão e atualização. Objetivo distinto do
UCS001: aqui o foco é nas recusas e nas regras de negócio, não no
caminho feliz.

REQUISITOS RELACIONADOS
Features 2.1.2.1 Inclusão, 2.1.2.2 Consulta,
2.1.2.3 Atualização e 2.1.2.4 Exclusão.
CAs exercitados: CA-2.1.2.1.02, CA-2.1.2.1.05, CA-2.1.2.1.06,
CA-2.1.2.1.07, CA-2.1.2.1.09, CA-2.1.2.1.12, CA-2.1.2.1.17,
CA-2.1.2.2.09, CA-2.1.2.3.02, CA-2.1.2.3.05, CA-2.1.2.4.04.

ATOR
Usuário autenticado com autorização para as quatro operações.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado.
- Turbina TUR-ESTUDO-002 pré-cadastrada com Potência 1500 W e Status Ativo,
  usada como referência de duplicidade.
- Turbina TUR-ESTUDO-VAL inexistente antes do passo 1.
- Inversor INV-ESTUDO-002, Modelo Modelo Estudo B e Fornecedor Fornecedor
  Estudo B ativos e disponíveis.
- Nenhum registro de controle é alterado durante o cenário.

DADOS DE TESTE
Série válida: TUR-ESTUDO-VAL; Potência válida: 3000 W.
Série duplicada: TUR-ESTUDO-002 (já cadastrada).
Série com espaços: "   " (três espaços, sem caracteres visíveis).
Potência negativa: -100; Potência vazia: em branco.
Os dados são fictícios; não definem novos limites ou domínios.

[FP] FLUXO PRINCIPAL — CRUD COM FOCO EM VALIDAÇÕES

1. CRIAR com série de espaços. Abrir o formulário. Preencher o campo
   Número de Série somente com espaços ("   "). Preencher os demais
   campos obrigatórios com valores válidos. Acionar Salvar.
   Esperado: inclusão recusada; número de série sem conteúdo válido
   identificado. Ref.: CA-2.1.2.1.12.

2. CRIAR com potência negativa. Preencher Número de Série com
   TUR-ESTUDO-VAL e Potência com -100. Acionar Salvar.
   Esperado: inclusão recusada; campo Potência identificado como inválido.
   Ref.: CA-2.1.2.1.05.

3. CRIAR com potência vazia. Manter Número de Série TUR-ESTUDO-VAL e
   deixar o campo Potência em branco. Acionar Salvar.
   Esperado: inclusão recusada; campo Potência identificado como vazio.
   Ref.: CA-2.1.2.1.05.

4. CRIAR com Status Inativo antes de salvar. Preencher todos os campos
   obrigatórios com valores válidos. Verificar que o Status inicial é
   Ativo. Mudar o Status para Inativo antes de acionar Salvar.
   Esperado: cadastro concluído com Status Inativo; a consulta apresenta
   o estado Inativo — sem converter automaticamente para exclusão.
   Ref.: CA-2.1.2.1.06, CA-2.1.2.1.17.

5. CONSULTAR. Localizar TUR-ESTUDO-VAL na listagem e confirmar que o
   Status exibido é Inativo.
   Esperado: a tabela exibe TUR-ESTUDO-VAL com Status Inativo.

6. ATUALIZAR com campo obrigatório apagado. Abrir a edição de
   TUR-ESTUDO-VAL. Apagar o valor do campo Potência. Acionar Salvar.
   Esperado: salvamento recusado; campo Potência identificado como
   obrigatório e vazio. Ref.: CA-2.1.2.3.02, CA-2.1.2.3.05.

7. CRIAR com série duplicada. Tentar cadastrar nova turbina com
   Número de Série TUR-ESTUDO-002 (já existente).
   Esperado: inclusão recusada; duplicidade informada.
   Ref.: CA-2.1.2.1.07.

8. EXCLUIR com cancelamento. Acionar Excluir para TUR-ESTUDO-VAL.
   Verificar que a caixa apresenta o Número de Série TUR-ESTUDO-VAL.
   Acionar Cancelar.
   Esperado: nenhuma exclusão realizada; turbina permanece disponível.
   Ref.: CA-2.1.2.4.04.

[A] FLUXOS ALTERNATIVOS

1. Número de série com 101 caracteres. Tentar cadastrar com série
   excedendo o limite de 100 caracteres.
   Esperado: inclusão recusada ou campo limitado pelo sistema.
   Ref.: CA-2.1.2.1.12.

2. Formulário aberto sem dados. Apenas abrir o formulário de inclusão
   sem preencher nenhum campo e tentar salvar.
   Esperado: todos os campos obrigatórios identificados; nenhuma turbina
   incluída. Ref.: CA-2.1.2.1.09.

REGRAS DE NEGÓCIO E ORÁCULO
- Status Inativo na inclusão não equivale a exclusão.
- Espaços externos no número de série não contam como conteúdo válido.
- Garantia zero não equivale a campo vazio (CA-2.1.2.1.13).
- Resultados derivam dos CAs, não da implementação atual.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Nenhum resultado observado nesta entrega; nenhum teste executado.
- Em execução futura: registrar versão, data, massa, passo, esperado,
  observado e evidência.

PENDÊNCIAS PARA STAKEHOLDERS
Mensagem exibida ao ultrapassar 100 caracteres na série; comportamento
exato ao combinar Status Inativo com exclusão futura; concorrência.
"""
