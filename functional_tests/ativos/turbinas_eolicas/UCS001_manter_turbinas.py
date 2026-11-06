"""
UCS001 — Manter turbinas eólicas

Autoria / responsável acadêmico: Ícaro Pontes
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Grupo de requisitos: Gestão de Turbinas Eólicas — EPIC 2.1.2.

OBJETIVO
Descrever o ciclo completo de criar, consultar, atualizar e excluir turbinas
eólicas, reunindo as quatro operações no mesmo cenário, sem dividi-las em
quatro cenários contados separadamente. Exercita o fluxo principal de cada
operação com dados válidos e situação padrão.

REQUISITOS RELACIONADOS
Features 2.1.2.1 Inclusão, 2.1.2.2 Consulta,
2.1.2.3 Atualização e 2.1.2.4 Exclusão.
CAs exercitados: CA-2.1.2.1.01, CA-2.1.2.1.02, CA-2.1.2.1.05,
CA-2.1.2.1.07, CA-2.1.2.1.08, CA-2.1.2.1.09, CA-2.1.2.1.17,
CA-2.1.2.2.01, CA-2.1.2.2.02, CA-2.1.2.2.09,
CA-2.1.2.3.02, CA-2.1.2.3.04, CA-2.1.2.3.05,
CA-2.1.2.4.01, CA-2.1.2.4.04, CA-2.1.2.4.05.

ATOR
Usuário autenticado com autorização de inclusão, consulta, edição e exclusão
de ativos. Na exclusão, a fonte exige perfil específico; a equivalência de
perfis permanece pendente de definição.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado, sem dados de produção nem ações reais.
- Massa sintética e vínculos preparados antes do fluxo; nenhum registro de
  controle é alterado durante o cenário.
- Inversor INV-ESTUDO-001 ativo e disponível, associado à Usina Estudo A.
- Modelo Modelo Estudo A ativo; Fornecedor Fornecedor Estudo A ativo.
- Número de série TUR-ESTUDO-001 inexistente no sistema antes do passo 1.
- Autorização verificada por operação; acesso à listagem não implica permissão
  de inclusão, edição ou exclusão.
- Tratar as decisões em aberto nas pendências antes de aprovar etapas dependentes.

DADOS DE TESTE
Número de Série: TUR-ESTUDO-001; Potência: 2000 (W); Inversor: INV-ESTUDO-001;
Modelo: Modelo Estudo A; Fornecedor: Fornecedor Estudo A; Status inicial: Ativo.
Atualização: Potência alterada de 2000 para 2500 (W).
Os nomes e valores são fictícios e servem apenas de exemplo de entrada.
Não constituem novos limites, domínios, permissões ou regras de negócio.

[FP] FLUXO PRINCIPAL — CRUD COMPLETO

1. CRIAR. Preencher os cinco campos obrigatórios (Número de Série, Potência,
   ID Inversor, Modelo e Fornecedor) com os dados de teste. Verificar que o
   campo Status está marcado como Ativo por padrão antes de salvar. Acionar
   Salvar uma vez.
   Esperado: a turbina é criada; o sistema exibe a mensagem
   "Turbina eólica cadastrada com sucesso".

2. CONSULTAR. Buscar TUR-ESTUDO-001 na listagem. Abrir a linha correspondente
   e conferir que Número de Série, Potência, Modelo, Fornecedor, Inversor e
   Status correspondem aos dados cadastrados no passo 1.
   Esperado: a tabela exibe a turbina com os valores corretos; o detalhe
   apresenta os mesmos dados do cadastro.

3. ATUALIZAR. Abrir o formulário de edição de TUR-ESTUDO-001. Confirmar que
   os valores atuais estão carregados. Alterar a Potência de 2000 para 2500.
   Acionar Salvar.
   Esperado: o sistema confirma a atualização; a consulta subsequente do
   mesmo ativo exibe Potência 2500 e todos os demais dados preservados.

4. CONSULTAR APÓS ATUALIZAÇÃO. Reabrir a consulta e verificar TUR-ESTUDO-001.
   Esperado: Potência 2500 é exibida; Número de Série, Modelo, Fornecedor e
   Status permanecem inalterados.

5. EXCLUIR. Usar variante sem associações a serviços impeditivas. Acionar
   Excluir; conferir que a caixa de confirmação apresenta o Número de Série
   TUR-ESTUDO-001; confirmar a exclusão.
   Esperado: a turbina é removida; a consulta não a apresenta mais; a
   exclusão não é apresentada como simples inativação. A comprovação de
   remoção permanente e os meios observáveis para confirmá-la dependem das
   pendências descritas abaixo.

6. CONSULTAR APÓS EXCLUSÃO. Buscar TUR-ESTUDO-001 na listagem.
   Esperado: o registro não é encontrado; nenhum dado residual é exibido.

[A] FLUXOS ALTERNATIVOS

1. Turbina com serviço associado. Preparar variante com ordem de serviço
   vinculada e solicitar exclusão.
   Esperado: recusa; motivo informado; turbina preservada. Ref.: CA-2.1.2.4.02.

2. Duplicidade de série. Tentar cadastrar uma segunda turbina com
   TUR-ESTUDO-001.
   Esperado: inclusão recusada; duplicidade informada. Ref.: CA-2.1.2.1.07.

3. Campo obrigatório vazio na inclusão. Tentar salvar com um dos cinco campos
   obrigatórios em branco.
   Esperado: salvamento recusado; campo vazio identificado. Ref.: CA-2.1.2.1.02.

[A-COM] CONCORRÊNCIA E INTERRUPÇÃO
Se outro usuário alterar o cadastro durante o fluxo, ou ocorrer perda de
resposta, registrar o ponto interrompido e a dúvida. Não escolher prevalência,
prazo ou recuperação que não esteja definida. Os resultados dessas variantes
permanecem pendentes de especificação.

REGRAS DE NEGÓCIO E ORÁCULO
- Os resultados dos passos derivam dos CAs relacionados, não da resposta atual
  do sistema.
- O cadastro em uma operação não concede autorização para as operações seguintes.
- Cancelamento e bloqueio não devem ser descritos como conclusão bem-sucedida.
- Ausência na listagem não prova remoção permanente.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Comparar entrada, consulta inicial, consulta após edição e resultado da exclusão.
- Em futura execução, anotar versão, data, massa, passo, esperado, observado e
  evidência.
- Nesta entrega: nenhum resultado observado; nenhum teste executado; sem
  homologação.

PENDÊNCIAS PARA STAKEHOLDERS
Forma de comprovar remoção definitiva versus inativação; equivalência de perfis
para exclusão; comportamento da exclusão quando há histórico de ordens de serviço;
concorrência e perda de resposta durante o salvamento.
"""
