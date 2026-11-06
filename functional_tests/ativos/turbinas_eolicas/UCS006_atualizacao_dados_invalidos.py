"""
UCS006 — Exportar ficha individual de turbina eólica

Autoria / responsável acadêmico: Ícaro Pontes
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Grupo de requisitos: Gestão de Turbinas Eólicas — EPIC 2.1.2.

OBJETIVO
Verificar que a exportação individual produz um PDF referente
exclusivamente ao cadastro escolhido, que o arquivo é identificável
pelo registro selecionado e que a indisponibilidade do registro é
informada corretamente. Cenário de relatório individual, distinto
da exportação coletiva do UCS005.

REQUISITOS RELACIONADOS
Feature: Exportação de turbinas eólicas.
Critérios identificados pelos títulos originais: Arquivo individual;
Registro individual indisponível; Entrega do arquivo.
Ref.: CA-2.1.2.2.04, CA-2.1.2.2.07.

ATOR
Usuário com permissão de visualização do registro individual.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado; massa sintética preparada.
- Turbina TUR-IND-A existente com dados cadastrais conhecidos.
- Turbina TUR-IND-B existente com dados diferentes de TUR-IND-A.
- Turbina TUR-IND-EXCLUIDA foi removida do sistema antes do fluxo.
- Nenhum cadastro é criado nem alterado neste cenário.

DADOS DE TESTE
Turbinas disponíveis: TUR-IND-A e TUR-IND-B (dados distintos entre si).
Turbina excluída: TUR-IND-EXCLUIDA.
Os dados são fictícios; não definem novos limites ou domínios.

[FP] FLUXO PRINCIPAL

1. Localizar TUR-IND-A na listagem e acessar seus detalhes.

2. Verificar que a opção de exportação individual disponível é PDF
   (não CSV). Acionar a exportação individual.
   Esperado: o download é iniciado; o resultado da obtenção é informado.

3. Verificar o arquivo PDF obtido:
   (a) O arquivo representa exclusivamente TUR-IND-A.
   (b) A identificação no arquivo permite reconhecer TUR-IND-A pelo
       Número de Série.
   (c) Nenhum dado de TUR-IND-B está presente no arquivo.
   Conteúdo completo do PDF permanece BLOQUEADO para aceite integral
   até resolução das pendências de contrato de saída.

4. Repetir o fluxo para TUR-IND-B. Confirmar que o arquivo representa
   TUR-IND-B e não TUR-IND-A.
   Esperado: o arquivo de TUR-IND-B não contém dados de TUR-IND-A.

[A] FLUXOS ALTERNATIVOS

1. Registro indisponível. Solicitar a exportação individual de
   TUR-IND-EXCLUIDA.
   Esperado: indisponibilidade informada; nenhum relatório de outro
   registro entregue.

2. Mesmo alvo ao exportar. Enquanto visualizando TUR-IND-A, acionar a
   exportação individual disponível na tela.
   Esperado: a solicitação se refere a TUR-IND-A, não a TUR-IND-B nem
   a nenhum outro registro.

REGRAS DE NEGÓCIO E ORÁCULO
- A exportação individual é sempre PDF; não presumir CSV individual.
- O arquivo não substitui a exportação da lista (coletiva).
- Registro indisponível não deve ser substituído por outro registro.
- Resultados derivam dos critérios identificados, não da implementação atual.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Nenhum arquivo gerado nem cenário executado nesta entrega.
- Em execução futura: registrar versão, data, massa, passo, esperado,
  observado e evidência.

PENDÊNCIAS PARA STAKEHOLDERS
Campos mínimos e conteúdo completo do PDF individual precisam de decisão.
Unidades de potência e garantias na ficha. Comportamento quando o registro
é excluído durante a preparação do arquivo.
"""
