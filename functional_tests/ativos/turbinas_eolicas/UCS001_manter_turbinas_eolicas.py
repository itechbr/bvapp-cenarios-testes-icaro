'''
UCS001 — Manter turbinas eólicas

Objetivo: Permitir que o usuário possa cadastrar, consultar, atualizar e excluir turbinas eólicas no BVapp, integrando todo o ciclo de vida do ativo em um único cenário de CRUD com seus respectivos fluxos alternativos.

Requisitos:
- FEATURE-2.1.2.1: Inclusão de turbinas eólicas (CA-2.1.2.1.01 a CA-2.1.2.1.19)
- FEATURE-2.1.2.2: Consulta de turbinas eólicas (CA-2.1.2.2.01 a CA-2.1.2.2.13 e US #28740)
- FEATURE-2.1.2.3: Atualização de turbinas eólicas (CA-2.1.2.3.01 a CA-2.1.2.3.14 e US #29056)
- FEATURE-2.1.2.4: Exclusão de turbinas eólicas (CA-2.1.2.4.01 a CA-2.1.2.4.06)

Ator:
- Usuário autenticado com permissão de gestão de ativos.
'''

# 🟢 [FP] - FLUXO PRINCIPAL: INCLUIR TURBINA EÓLICA
# ---------------------------------------------------------------

# 1. O ator acessa o menu "Gestão de Ativos" -> "Turbinas Eólicas" e clica no botão "Nova Turbina Eólica".
#    O sistema exibe o formulário de cadastro de turbinas eólicas contendo os campos:
#    - Número de Série / Identificador (obrigatório)
#    - Potência Nominal em Watts (obrigatório)
#    - Inversor associado (obrigatório)
#    - Modelo (obrigatório)
#    - Fornecedor (obrigatório)
#    - Fabricante
#    - Usina / Parque Eólico (herdada do Inversor)
#    - Status (padrão: "Ativo")
#    - Seção de Datas e Garantias (compra, instalação e entrada em operação)

# 2. O ator preenche os campos do formulário com dados válidos:
#    - Número de Série: "TUR-EOL-001"
#    - Potência Nominal: "2000000" (2 MW)
#    - Inversor: seleciona "INV-001" (vinculado à Usina Serra do Mel)
#    - Modelo: seleciona "Vestas V150"
#    - Fornecedor: seleciona "Vestas do Brasil"
#    - Fabricante: seleciona "Vestas Wind Systems"
#    - Data de Compra: "10/01/2026"
#    - Garantia de Compra: "24" (meses)
#    - Data de Instalação: "15/02/2026"
#    - Garantia de Instalação: "12" (meses)
#    - Data de Entrada em Operação: "01/03/2026"
#    - Status: mantém o valor padrão "Ativo" [A4][A5][A6][A7][A8][A9]

# 3. O ator aciona a opção "Salvar". [A1][A2][A3]

# 4. O sistema valida os campos obrigatórios, confirma a inexistência de duplicidade do número de série,
#    verifica a compatibilidade da usina e valida a cronologia das datas e prazos de garantia [RN1].

# 5. O sistema grava o registro da nova turbina eólica no banco de dados e exibe a mensagem de sucesso:
#    "Turbina eólica cadastrada com sucesso".


# 🟠 [A1] - CONSULTAR TURBINA EÓLICA
# ---------------------------------------------------------------

# 6. O ator necessita localizar uma turbina eólica cadastrada e acessa a página "Listagem de Turbinas Eólicas".
# 7. O sistema exibe a listagem contendo os registros de turbinas eólicas com paginação de até 10 itens por página.
# 8. O ator informa o filtro de busca desejado (ex.: Número de Série "TUR-EOL-001" ou Modelo "Vestas V150") e clica em "Pesquisar".
# 9. O sistema filtra e apresenta na tabela o registro correspondente com os dados cadastrados.
# 10. O ator aciona a opção "Visualizar Detalhes" da turbina.
# 11. O sistema exibe a tela de detalhamento técnico confirmando todos os campos, garantias calculadas e vínculos com o inversor e a usina.


# 🟠 [A2] - ATUALIZAR / EDITAR TURBINA EÓLICA
# ---------------------------------------------------------------

# 12. O ator executa a consulta [A1] e localiza a turbina "TUR-EOL-001".
# 13. O ator clica na opção "Editar".
# 14. O sistema exibe o formulário de edição com os dados atuais da turbina preenchidos e o campo Número de Série protegido contra alteração.
# 15. O ator altera a Potência Nominal para "2500000" (2.5 MW) e o Status para "Em Manutenção" [A10].
# 16. O ator aciona a opção "Salvar".
# 17. O sistema valida os dados alterados [RN1], atualiza o registro e exibe a mensagem:
#     "Dados da turbina eólica atualizados com sucesso".
# 18. O ator retorna à consulta e verifica que os novos valores estão refletidos.


# 🟠 [A3] - EXCLUIR TURBINA EÓLICA
# ---------------------------------------------------------------

# 19. O ator executa a consulta [A1], localiza a turbina "TUR-EOL-001" (sem histórico de serviços ou ordens impeditivas vinculadas) e seleciona a opção "Excluir".
# 20. O sistema exibe uma janela modal de confirmação contendo o Número de Série "TUR-EOL-001" e a pergunta se deseja confirmar a exclusão.
# 21. O ator clica em "Confirmar Exclusão" [A12][A13].
# 22. O sistema remove o registro do ativo do banco de dados e exibe a mensagem de sucesso:
#     "Turbina eólica removida com sucesso".
# 23. O ator acessa a listagem e confirma que a turbina "TUR-EOL-001" não é mais exibida.


# 🟠 [A4] - TENTATIVA DE INCLUSÃO COM CAMPOS OBRIGATÓRIOS EM BRANCO
# ---------------------------------------------------------------

# 24. No passo 2, o ator deixa de preencher um ou mais campos obrigatórios (ex.: Número de Série ou Potência Nominal em branco).
# 25. O ator clica em "Salvar".
# 26. O sistema bloqueia a gravação, destaca os campos obrigatórios em vermelho e exibe a mensagem de validação correspondente.


# 🟠 [A5] - TENTATIVA DE INCLUSÃO COM NÚMERO DE SÉRIE DUPLICADO
# ---------------------------------------------------------------

# 27. No passo 2, o ator informa um Número de Série que já se encontra cadastrado no sistema para outro ativo.
# 28. O ator clica em "Salvar".
# 29. O sistema identifica a duplicidade da chave única e recusa a operação com mensagem:
#     "O Número de Série informado já está cadastrado para outro ativo".


# 🟠 [A6] - TENTATIVA DE INCLUSÃO COM VALOR DE POTÊNCIA NEGATIVO OU ZERADO
# ---------------------------------------------------------------

# 30. No passo 2, o ator preenche o campo de Potência Nominal com valor menor ou igual a zero (ex.: "-500").
# 31. O ator clica em "Salvar".
# 32. O sistema bloqueia o cadastro e informa que a potência deve ser um valor numérico estritamente positivo.


# 🟠 [A7] - TENTATIVA DE INCLUSÃO COM DATAS CRONOLOGICAMENTE INCONSISTENTES
# ---------------------------------------------------------------

# 33. No passo 2, o ator informa a Data de Instalação anterior à Data de Compra, ou Data de Entrada em Operação anterior à Instalação.
# 34. O ator clica em "Salvar".
# 35. O sistema recusa o salvamento informando que a sequência cronológica das datas deve respeitar: Compra <= Instalação <= Operação.


# 🟠 [A8] - TENTATIVA DE INCLUSÃO COM PAR DE GARANTIA INCOMPLETO
# ---------------------------------------------------------------

# 36. No passo 2, o ator preenche uma data (compra ou instalação) mas deixa o respectivo prazo de garantia em branco, ou informa garantia negativa.
# 37. O ator clica em "Salvar".
# 38. O sistema bloqueia a gravação informando a obrigatoriedade do preenchimento conjunto da data e de sua garantia com valor maior ou igual a zero.


# 🟠 [A9] - TENTATIVA DE CADASTRO COM INVERSOR INATIVO OU USINA INCOMPATÍVEL
# ---------------------------------------------------------------

# 39. No passo 2, o ator seleciona um Inversor cujo status esteja "Inativo" ou que pertença a uma Usina diferente da informada.
# 40. O ator clica em "Salvar".
# 41. O sistema bloqueia o vínculo informando que o inversor selecionado se encontra indisponível.


# 🟠 [A10] - ALTERAÇÃO RÁPIDA DE STATUS OPERACIONAL COM CONFIRMAÇÃO
# ---------------------------------------------------------------

# 42. Na listagem de turbinas, o ator aciona a alteração direta de status de uma turbina de "Ativo" para "Inativo".
# 43. O sistema abre diálogo de confirmação exibindo o número de série e o status solicitado.
# 44. O ator confirma a alteração.
# 45. O sistema atualiza o status para "Inativo" preservando todos os demais atributos cadastrais.


# 🟠 [A11] - CANCELAMENTO DA MUDANÇA DE STATUS OPERACIONAL
# ---------------------------------------------------------------

# 46. No passo 43, o ator clica em "Cancelar" na janela de confirmação de status.
# 47. O sistema fecha a janela sem modificar o status e mantém o estado original da turbina.


# 🟠 [A12] - CANCELAMENTO DA EXCLUSÃO
# ---------------------------------------------------------------

# 48. No passo 21, o ator clica em "Cancelar" na janela modal de confirmação de exclusão.
# 49. O sistema fecha a janela modal sem aplicar a remoção e mantém a turbina cadastrada e ativa.


# 🟠 [A13] - EXCLUSÃO BLOQUEADA POR HISTÓRICO OU ORDENS DE SERVIÇO ATIVAS
# ---------------------------------------------------------------

# 50. O ator tenta excluir uma turbina eólica que possui histórico de ordens de serviço ou registros de manutenção vinculados.
# 51. O sistema intercepta a exclusão física e impede a operação, informando que ativos com vínculos de serviço não podem ser excluídos definitivamente.


# 🟠 [A14] - TENTATIVA DE OPERAÇÃO POR USUÁRIO SEM PERMISSÃO
# ---------------------------------------------------------------

# 52. Um usuário sem permissão de administração tenta acionar os formulários de inclusão, edição ou exclusão.
# 53. O sistema bloqueia a ação e exibe mensagem de autorização insuficiente (HTTP 403 Forbidden).


# 🟣 [RN1] - REGRAS DE NEGÓCIO E INTEGRIDADE DO CRUD
# ---------------------------------------------------------------

# - Todos os campos estruturais (Número de Série, Potência, Inversor, Modelo, Fornecedor) são de preenchimento obrigatório.
# - O Número de Série é a chave única da turbina eólica no sistema e não pode ser duplicado sob nenhuma hipótese.
# - A Potência Nominal deve ser informada em Watts e ter valor numérico estritamente maior que zero.
# - A Usina da turbina é herdada diretamente do Inversor selecionado para manter a integridade topológica do parque.
# - A cronologia de datas deve respeitar obrigatoriamente: Data de Compra <= Data de Instalação <= Data de Entrada em Operação.
# - Informar uma data de compra ou instalação exige informar o respectivo prazo de garantia contratual em meses (regra do par de campos).
# - A inativação de uma turbina não equivale à sua exclusão; a turbina inativa continua acessível para consultas e relatórios.
# - Turbinas associadas a ordens de serviço ativas ou histórico de manutenção não podem sofrer exclusão física.
