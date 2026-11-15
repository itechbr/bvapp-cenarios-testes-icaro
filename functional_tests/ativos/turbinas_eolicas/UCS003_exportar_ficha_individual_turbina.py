'''
UCS003 — Exportar ficha técnica individual de turbina eólica

Objetivo: Permitir a exportação da ficha técnica individual e completa de uma turbina eólica selecionada para um documento em formato PDF, consolidando parâmetros técnicos de engenharia, datas contratuais, prazos de garantia e vínculos patrimoniais específicos do ativo.

Requisitos:
- FEATURE: Exportação de turbinas eólicas (Arquivo individual; Registro individual indisponível; Entrega do arquivo; Autorização)
- FEATURE-2.1.2.2: Consulta de turbinas eólicas (US #28740 - Detalhamento da turbina eólica)

Ator:
- Usuário autenticado com permissão de visualização detalhada de ativos.
'''

# 🟢 [FP] - FLUXO PRINCIPAL: EXPORTAÇÃO DE FICHA TÉCNICA INDIVIDUAL EM PDF
# ---------------------------------------------------------------

# 1. O ator acessa a listagem de turbinas eólicas e clica sobre o registro da turbina "TUR-EOL-001".
#    O sistema carrega a tela de detalhamento técnico do ativo.

# 2. O ator confere a exibição dos dados técnicos completos da turbina: potência nominal, rotor, torre, fabricante, fornecedor, garantias e usina associada.

# 3. O ator clica no botão "Exportar Ficha Técnica (PDF)". [A1][A2][A3]

# 4. O sistema processa o documento diagramado contendo exclusivamente as informações da turbina "TUR-EOL-001", com o respectivo Número de Série em destaque no cabeçalho [RN1].

# 5. O sistema inicia automaticamente o download do arquivo nomeado no padrão `ficha_tecnica_TUR-EOL-001.pdf` e mantém o usuário na tela de detalhes.


# 🟠 [A1] - EXPORTAÇÃO DE FICHA TÉCNICA COM SEÇÕES COMPLEMENTARES
# ---------------------------------------------------------------

# 6. No passo 1, o ator seleciona uma turbina eólica que possui histórico de manutenção, ordens de serviço e cooperados vinculados.
# 7. O ator clica em "Exportar Ficha Técnica (PDF)".
# 8. O sistema inclui na ficha as seções complementares de histórico operacional e cooperativa, sem mesclar dados de nenhum outro equipamento.


# 🟠 [A2] - TENTATIVA DE EXPORTAÇÃO DE ATIVO INEXISTENTE OU RECÉM-EXCLUÍDO
# ---------------------------------------------------------------

# 9. O ator tenta acessar a exportação da ficha técnica informando diretamente na URL um identificador de turbina que foi previamente excluído ou que não existe na base.
# 10. O sistema verifica a inexistência do ativo, bloqueia a geração do PDF e exibe a mensagem de erro:
#     "O ativo solicitado não foi encontrado ou está indisponível para exportação".


# 🟠 [A3] - TENTATIVA DE EXPORTAÇÃO INDIVIDUAL POR USUÁRIO SEM PERMISSÃO
# ---------------------------------------------------------------

# 11. Um usuário com permissão restrita tenta acessar a rota de exportação individual de um ativo protegido.
# 12. O sistema bloqueia a extração e apresenta notificação de acesso negado (HTTP 403 Forbidden).


# 🟣 [RN1] - REGRAS DE NEGÓCIO DA FICHA TÉCNICA INDIVIDUAL
# ---------------------------------------------------------------

# - A exportação individual de ativos é realizada obrigatoriamente no formato PDF diagramado.
# - A ficha técnica deve representar com estrita exclusividade a turbina selecionada, sendo vedada a inclusão de dados residuais de outros ativos.
# - O documento deve apresentar em destaque: Número de Série, Usina, Inversor associado, Potência Nominal e datas de compra, instalação e operação com os respectivos prazos de garantia.
# - Identificadores inexistentes ou desativados permanentemente não devem produzir documentos vazios.
