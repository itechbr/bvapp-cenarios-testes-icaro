"""
UCS004 — Manter turbinas eólicas com alteração de status e controle de acesso

Autoria / responsável acadêmico: Ícaro Pontes
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Grupo de requisitos: Gestão de Turbinas Eólicas — EPIC 2.1.2.

OBJETIVO
Exercitar o ciclo CRUD focando na operação de alteração isolada de Status
(Ativo/Inativo), no controle de acesso por operação e no comportamento de
confirmação e cancelamento. Exercita também a consulta com distinção entre
estados do sistema. Objetivo distinto dos UCS001, UCS002 e UCS003.

REQUISITOS RELACIONADOS
Features 2.1.2.1 Inclusão, 2.1.2.2 Consulta,
2.1.2.3 Atualização e 2.1.2.4 Exclusão.
CAs exercitados: CA-2.1.2.1.19, CA-2.1.2.2.01, CA-2.1.2.2.10,
CA-2.1.2.3.01, CA-2.1.2.3.03, CA-2.1.2.3.07, CA-2.1.2.3.08,
CA-2.1.2.4.01, CA-2.1.2.4.06.

ATOR PRINCIPAL
Usuário autorizado para inclusão, consulta, edição e exclusão.

ATOR ALTERNATIVO
Usuário sem autorização de inclusão e sem autorização de exclusão
(somente consulta); usado nos fluxos alternativos.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado.
- Turbina TUR-ESTUDO-004 cadastrada com Status Ativo e dados cadastrais
  conhecidos (Potência 1800 W, Modelo Modelo Estudo C, Fornecedor
  Fornecedor Estudo C).
- Turbina TUR-ESTUDO-EXCLUIDA foi removida do sistema antes do fluxo
  (usada no passo 6).
- Usuário sem autorização disponível para os fluxos alternativos.

DADOS DE TESTE
Série: TUR-ESTUDO-004; Status inicial: Ativo; Potência: 1800 W.
Os dados são fictícios; não definem novos limites ou domínios.

[FP] FLUXO PRINCIPAL — CRUD COM STATUS E ACESSO

1. CRIAR. Preencher os campos obrigatórios e acionar Salvar.
   (Este passo é coberto em detalhe pelo UCS001; aqui valida a
   pré-condição do cenário. TUR-ESTUDO-004 já está pré-cadastrada.)

2. CONSULTAR — distinção de estados. Acessar a listagem de turbinas.
   Observar separadamente: (a) listagem em carregamento; (b) resultado
   sem turbinas com o filtro aplicado; (c) falha na obtenção da lista.
   Esperado: o sistema distingue visualmente espera, nenhum resultado
   e falha; uma falha não confirma ausência de ativos.
   Ref.: CA-2.1.2.2.10.

3. ATUALIZAR Status — cancelar. Acionar a alteração de Status de
   TUR-ESTUDO-004 para Inativo. Verificar que o sistema apresenta o
   Número de Série e a situação escolhida (Inativo). Acionar Cancelar.
   Esperado: TUR-ESTUDO-004 permanece Ativo; nenhuma alteração registrada.
   Ref.: CA-2.1.2.3.07.

4. ATUALIZAR Status — confirmar. Repetir a alteração para Inativo.
   Desta vez acionar Confirmar.
   Esperado: TUR-ESTUDO-004 passa a exibir Status Inativo; Potência 1800 W,
   Modelo e Fornecedor permanecem inalterados.
   Ref.: CA-2.1.2.3.03, CA-2.1.2.3.07.

5. ATUALIZAR Status — repetir mesmo estado. Solicitar Inativo novamente
   para TUR-ESTUDO-004 (já Inativo).
   Esperado: o sistema processa sem alterar a identificação nem os demais
   dados. Ref.: CA-2.1.2.3.03.

6. ATUALIZAR ativo indisponível. Abrir o formulário de edição de
   TUR-ESTUDO-EXCLUIDA.
   Esperado: atualização recusada; informação de que o registro não está
   disponível. Ref.: CA-2.1.2.3.08.

7. EXCLUIR sem autorização. Usar o usuário sem permissão de exclusão e
   tentar confirmar a exclusão de TUR-ESTUDO-004.
   Esperado: operação recusada; cadastro preservado. Ref.: CA-2.1.2.4.01.

8. EXCLUIR com falha. Simular falha durante a exclusão de TUR-ESTUDO-004
   (autorizado).
   Esperado: falha apresentada sem confirmar a remoção; turbina preservada.
   Ref.: CA-2.1.2.4.06.

[A] FLUXOS ALTERNATIVOS

1. Inclusão sem autorização. Usar o usuário sem permissão de inclusão e
   tentar concluir o cadastro de uma nova turbina.
   Esperado: inclusão recusada. Ref.: CA-2.1.2.1.19.

2. Consulta sem autorização. Usar o usuário sem permissão de consulta e
   tentar acessar a listagem.
   Esperado: listagem não apresentada. Ref.: CA-2.1.2.2.01.

3. Alteração sem autorização. Usar o usuário somente-consulta e tentar
   salvar uma alteração de dados ou de Status.
   Esperado: ambas as operações são recusadas. Ref.: CA-2.1.2.3.01.

REGRAS DE NEGÓCIO E ORÁCULO
- Autorização de consulta não implica autorização de inclusão, edição ou exclusão.
- Cancelamento de Status não altera os dados; confirmar aplica somente Status.
- Falha não é confirmação de sucesso.
- Resultados derivam dos CAs, não da implementação atual.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Nenhum resultado observado nesta entrega; nenhum teste executado.
- Em execução futura: registrar versão, data, massa, passo, esperado,
  observado e evidência.

PENDÊNCIAS PARA STAKEHOLDERS
Conciliação de Ativo/Inativo com estados de manutenção, defeito ou descarte;
equivalência de perfis para exclusão; auditoria e log de mudança de status;
recuperação após perda de resposta durante alteração.
"""
