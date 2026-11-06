"""
UCS007 — Tratar autorização e falha na exportação de turbinas eólicas

Autoria / responsável acadêmico: Ícaro Pontes
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Grupo de requisitos: Gestão de Turbinas Eólicas — EPIC 2.1.2.

OBJETIVO
Verificar que a exportação sem autorização é recusada, que falha na
obtenção do arquivo é informada sem entregar conteúdo de erro como
relatório, e que o controle de exportação fica indisponível durante
a preparação do arquivo. Cenário de relatório; não contém CRUD.

REQUISITOS RELACIONADOS
Feature: Exportação de turbinas eólicas.
Critérios identificados pelos títulos originais: Autorização;
Falha na obtenção do arquivo; Exportação em andamento.

ATOR PRINCIPAL
Usuário sem autorização de consulta (fluxo de autorização).
Usuário com autorização de consulta (fluxos de falha e andamento).

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado.
- Usuário sem permissão de consulta disponível para o passo 1.
- Usuário com permissão de consulta disponível para os passos 2 e 3.
- Turbina TUR-AUTH-A existente e visível para usuário autorizado.
- Nenhum cadastro é criado nem alterado neste cenário.

[FP] FLUXO PRINCIPAL

1. AUTORIZAÇÃO COLETIVA. Usar o usuário sem permissão de consulta da
   listagem e solicitar a exportação coletiva.
   Esperado: exportação recusada; nenhum relatório entregue.

2. AUTORIZAÇÃO INDIVIDUAL. Usar o usuário sem permissão de visualização
   do registro e solicitar a exportação individual de TUR-AUTH-A.
   Esperado: exportação recusada; nenhum relatório entregue.

3. FALHA NA OBTENÇÃO. Usar o usuário autorizado. Solicitar exportação
   coletiva em condição que provoca falha no servidor (simulada ou
   condição preparada em ambiente de teste).
   Esperado: a falha é informada ao usuário; nenhum conteúdo de erro
   é entregue como se fosse um relatório concluído.

4. EXPORTAÇÃO EM ANDAMENTO. Usar o usuário autorizado. Iniciar a
   exportação coletiva e, enquanto o arquivo está sendo preparado,
   tentar acionar o mesmo controle de exportação novamente.
   Esperado: o controle que iniciou a exportação fica indisponível
   durante a preparação; o usuário recebe indicação de que o arquivo
   está sendo preparado; a segunda tentativa pelo mesmo controle não
   é aceita.

[A] FLUXOS ALTERNATIVOS

1. Autorização coletiva diferente da individual. Usuário com permissão
   para exportar lista, mas sem permissão de visualização individual,
   tenta exportar ficha individual.
   Esperado: exportação individual recusada; exportação coletiva não
   é afetada pela ausência de permissão individual.

REGRAS DE NEGÓCIO E ORÁCULO
- Autorização de consulta (listagem) é necessária para exportação coletiva.
- Autorização de visualização do registro é necessária para exportação individual.
- Falha não é relatório concluído.
- Controle indisponível durante preparação impede duplo acionamento pelo
  mesmo controle; não impede outras ações do usuário na tela.
- Resultados derivam dos critérios identificados, não da implementação atual.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Nenhum arquivo gerado nem cenário executado nesta entrega.
- Em execução futura: registrar versão, data, massa, passo, esperado,
  observado e evidência.

PENDÊNCIAS PARA STAKEHOLDERS
Tempo máximo de preparação antes de considerar falha por timeout.
Recuperação após perda de resposta. Comportamento do controle após
conclusão bem-sucedida (volta a ficar disponível?).
"""
