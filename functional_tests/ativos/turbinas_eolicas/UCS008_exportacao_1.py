"""
UCS008 — Consultar turbinas eólicas com filtros combinados e paginação

Autoria / responsável acadêmico: Ícaro Pontes
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Grupo de requisitos: Gestão de Turbinas Eólicas — EPIC 2.1.2.

OBJETIVO
Verificar os filtros de consulta disponíveis, sua combinação, a paginação
da listagem e os limites de período e potência. Cenário de consulta pura,
sem exportação nem operações CRUD.

REQUISITOS RELACIONADOS
Feature 2.1.2.2 — Consulta de turbinas eólicas.
CAs exercitados: CA-2.1.2.2.02, CA-2.1.2.2.03, CA-2.1.2.2.05,
CA-2.1.2.2.06, CA-2.1.2.2.08, CA-2.1.2.2.09, CA-2.1.2.2.11,
CA-2.1.2.2.12.

ATOR
Usuário autenticado com permissão de consulta.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado; massa sintética preparada.
- 15 turbinas cadastradas, distribuídas em diferentes Modelos, Status e Usinas:
    * 5 turbinas: Modelo Estudo A, Status Ativo, Usina Estudo A.
    * 4 turbinas: Modelo Estudo B, Status Ativo, Usina Estudo B.
    * 6 turbinas: Status Inativo, Modelos e Usinas variados.
- Turbinas com datas de instalação: 3 antes de 01/01/2026, 5 em janeiro 2026,
  5 em fevereiro 2026, 2 depois de 01/03/2026.
- Duas turbinas com Potência 2000 W; demais com outras potências.
- Turbinas TUR-HIST-A e TUR-HIST-B possuem ordens de serviço distintas.
- Mais de 10 turbinas no resultado para validar paginação.

DADOS DE TESTE
Filtros individuais: Modelo = Modelo Estudo A; Status = Ativo;
Usina = Usina Estudo A; Potência = 2000; Período de instalação:
01/01/2026 a 28/02/2026 (limites inclusivos).
Os dados são fictícios; não definem novos limites ou domínios.

[FP] FLUXO PRINCIPAL

1. Acessar a listagem sem filtros. Verificar que a página inicial exibe
   até 10 registros, o total de itens, a página atual e o tamanho da página.
   Esperado: até 10 registros na página 1; total de itens reflete o conjunto
   completo; tamanho de página = 10. Ref.: CA-2.1.2.2.02, CA-2.1.2.2.08.

2. Verificar as colunas da tabela. Confirmar que a listagem exibe:
   Número de Série, Potência, Modelo / Fabricante, Usina, Data de Instalação,
   Data de Entrada em Operação e Status.
   Esperado: todas as colunas descritas presentes. Ref.: CA-2.1.2.2.09.

3. Navegar para a segunda página. Verificar que os registros mudam,
   mantendo o total de itens e a identificação da página atual.
   Esperado: novos registros; total e tamanho inalterados.
   Ref.: CA-2.1.2.2.06.

4. Aplicar filtro único: Modelo = Modelo Estudo A. Verificar que apenas
   turbinas com Modelo Estudo A são listadas.

5. Adicionar Status = Ativo ao filtro anterior. Verificar que apenas
   turbinas com Modelo Estudo A e Status Ativo são listadas.

6. Adicionar Usina = Usina Estudo A. Verificar que apenas as turbinas
   que atendem aos três filtros simultaneamente aparecem.
   Esperado: somente turbinas Modelo Estudo A AND Ativo AND Usina Estudo A.
   Ref.: CA-2.1.2.2.03, CA-2.1.2.2.05.

7. Remover todos os filtros. Verificar que a listagem retorna ao conjunto
   completo.

8. Aplicar filtro de período de instalação: de 01/01/2026 a 28/02/2026.
   Verificar que turbinas instaladas antes de 01/01/2026 e depois de
   28/02/2026 não aparecem, mas as instaladas exatamente em 01/01/2026
   e 28/02/2026 aparecem (limites inclusivos).
   Esperado: datas dos limites incluídas no resultado.
   Ref.: CA-2.1.2.2.11.

9. Aplicar filtro Potência = 2000. Verificar que somente as turbinas com
   Potência exatamente 2000 W são exibidas.
   Esperado: filtro de potência procura valor exato; potências 1999 e 2001
   não compõem o resultado. Ref.: CA-2.1.2.2.11.

10. Selecionar TUR-HIST-A na listagem e abrir seus detalhes. Acessar a
    aba de Histórico de Ordens de Serviço.
    Esperado: apenas ordens vinculadas a TUR-HIST-A são apresentadas;
    ordens de TUR-HIST-B não aparecem. Ref.: CA-2.1.2.2.12.

[A] FLUXOS ALTERNATIVOS

1. Campo de filtro vazio não restringe. Preencher somente o filtro Modelo
   e deixar Status em branco. Verificar que apenas o Modelo é aplicado.
   Esperado: filtros em branco não eliminam registros por ausência de valor.
   Ref.: CA-2.1.2.2.05.

REGRAS DE NEGÓCIO E ORÁCULO
- Paginação inicial: 10 registros por página.
- Limites de período são inclusivos.
- Filtro de Potência: valor exato.
- Histórico vinculado ao ativo selecionado; não agrega ordens de outros.
- Resultados derivam dos CAs, não da implementação atual.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Nenhum resultado observado nesta entrega; nenhum teste executado.
- Em execução futura: registrar versão, data, massa, passo, esperado,
  observado e evidência.

PENDÊNCIAS PARA STAKEHOLDERS
Semântica dos filtros de Operadora de Energia e Data de Compra (divergências
registradas nos CAs). Comportamento da paginação quando o último item da
página é excluído por outro usuário durante a consulta. Tempo máximo de espera
sem erro.
"""
