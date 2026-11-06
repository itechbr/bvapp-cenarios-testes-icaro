"""
UCS003 — Manter turbinas eólicas com validação de datas e vínculos patrimoniais

Autoria / responsável acadêmico: Ícaro Pontes
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Grupo de requisitos: Gestão de Turbinas Eólicas — EPIC 2.1.2.

OBJETIVO
Exercitar o ciclo CRUD com ênfase nas regras de validação de pares de datas
(compra, instalação, entrada em operação), vínculos patrimoniais (usina/inversor)
e referências indisponíveis. Objetivo distinto dos UCS001 e UCS002.

REQUISITOS RELACIONADOS
Features 2.1.2.1 Inclusão, 2.1.2.2 Consulta,
2.1.2.3 Atualização e 2.1.2.4 Exclusão.
CAs exercitados: CA-2.1.2.1.11, CA-2.1.2.1.13, CA-2.1.2.1.14,
CA-2.1.2.1.15, CA-2.1.2.1.16, CA-2.1.2.3.09, CA-2.1.2.3.10,
CA-2.1.2.3.11, CA-2.1.2.3.12, CA-2.1.2.4.02.

ATOR
Usuário autenticado com autorização para as quatro operações.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado.
- Inversor INV-ESTUDO-003 ativo, vinculado à Usina Estudo A.
- Usina Estudo B existente e ativa, diferente da Usina Estudo A.
- Fornecedor Inativo FornecedorInativo-X cadastrado mas com status Inativo.
- Turbina TUR-ESTUDO-003 cadastrada inicialmente sem datas.
- Turbina TUR-ESTUDO-COM-OS possui ordem de serviço ativa associada.

DADOS DE TESTE
Série: TUR-ESTUDO-003.
Data de Compra válida: 10/03/2026; Garantia de Compra válida: 24 (meses).
Data de Instalação anterior à compra (inválida): 09/03/2026.
Data de Instalação válida: 15/03/2026; Garantia de Instalação: 12 (meses).
Data de Entrada em Operação anterior à instalação (inválida): 11/03/2026.
Data de Entrada em Operação válida: 15/03/2026 (igual à instalação).
Os dados são fictícios; não definem novos limites ou domínios.

[FP] FLUXO PRINCIPAL — CRUD COM DATAS E VÍNCULOS

1. CRIAR com par de compra incompleto. Preencher campos obrigatórios e
   apenas a Data de Compra (10/03/2026), deixando a Garantia de Compra
   em branco. Acionar Salvar.
   Esperado: inclusão recusada por par incompleto. Ref.: CA-2.1.2.1.13.

2. CRIAR com instalação anterior à compra. Preencher Data de Compra
   10/03/2026 e Garantia de Compra 24. Preencher Data de Instalação
   09/03/2026. Acionar Salvar.
   Esperado: inclusão recusada; instalação anterior à compra identificada.
   Ref.: CA-2.1.2.1.14.

3. CRIAR com entrada em operação anterior. Preencher Data de Compra
   10/03/2026, Data de Instalação 15/03/2026 e Data de Entrada em
   Operação 11/03/2026. Acionar Salvar.
   Esperado: inclusão recusada; entrada em operação anterior à instalação
   identificada. Ref.: CA-2.1.2.1.15.

4. CRIAR com datas válidas. Preencher todos os campos com os dados válidos
   descritos acima: Compra 10/03/2026 + Garantia 24, Instalação 15/03/2026
   + Garantia 12, Entrada em Operação 15/03/2026. Acionar Salvar.
   Esperado: cadastro concluído com sucesso; datas iguais de Instalação e
   Entrada em Operação são aceitas.

5. CRIAR com vínculo de usina incompatível. Preparar nova turbina com
   Inversor INV-ESTUDO-003 (vinculado à Usina Estudo A) e selecionar
   explicitamente Usina Estudo B. Acionar Salvar.
   Esperado: inclusão recusada por incompatibilidade de usina.
   Ref.: CA-2.1.2.1.11.

6. CONSULTAR. Localizar TUR-ESTUDO-003 na listagem e confirmar datas
   e vínculos do passo 4.

7. ATUALIZAR com referência inexistente. Abrir edição de TUR-ESTUDO-003.
   Selecionar FornecedorInativo-X (inativo) como Fornecedor. Acionar Salvar.
   Esperado: atualização recusada; referência indisponível informada.
   Ref.: CA-2.1.2.3.09.

8. ATUALIZAR datas na edição. Manter o Fornecedor original. Alterar a
   Data de Instalação para 09/03/2026 (anterior à compra de 10/03/2026).
   Acionar Salvar.
   Esperado: atualização recusada pela sequência de datas inválida.
   Ref.: CA-2.1.2.3.11.

9. EXCLUIR com vínculo impeditivo. Localizar TUR-ESTUDO-COM-OS e solicitar
   exclusão. Confirmar na caixa de diálogo.
   Esperado: exclusão recusada; motivo informado; turbina preservada.
   Ref.: CA-2.1.2.4.02.

[A] FLUXOS ALTERNATIVOS

1. Data de compra futura. Preencher Data de Compra com data posterior à
   data atual. Acionar Salvar.
   Esperado: inclusão recusada. Ref.: CA-2.1.2.1.13.

2. Garantia de compra negativa. Preencher Data de Compra válida e Garantia
   de Compra com valor -1. Acionar Salvar.
   Esperado: inclusão recusada. Ref.: CA-2.1.2.1.13.

3. Garantia zero não equivale a vazio. Preencher Data de Compra válida e
   Garantia de Compra com valor 0 (zero). Acionar Salvar.
   Esperado: salvamento permitido; zero não é tratado como campo vazio.
   Ref.: CA-2.1.2.1.13.

REGRAS DE NEGÓCIO E ORÁCULO
- Datas iguais de Instalação e Entrada em Operação são aceitas.
- Par de datas: sempre informar data e garantia juntas, ou deixar as duas vazias.
- Referência inativa impede o vínculo em novo cadastro e em edição.
- Resultados derivam dos CAs, não da implementação atual.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Nenhum resultado observado nesta entrega; nenhum teste executado.
- Em execução futura: registrar versão, data, massa, passo, esperado,
  observado e evidência.

PENDÊNCIAS PARA STAKEHOLDERS
Exigência de preenchimento conjunto de Cooperados/Cooperativa na inclusão;
equivalência de regras de inclusão com edição para usina/inversor; unidade
de garantia (meses e equivalência de dias); concorrência.
"""
