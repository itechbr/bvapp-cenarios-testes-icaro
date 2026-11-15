# Pendências de Especificação de Requisitos (Stakeholders)

Durante a especificação dos cenários de teste da Epic 2.1.2 (Gestão de Turbinas Eólicas), foram identificadas as seguintes lacunas e ambiguidades nos requisitos funcionais de origem. Conforme as boas práticas de engenharia de software, nenhum comportamento foi inventado; as etapas que dependem dessas definições permanecem registradas como dúvidas formais para os *stakeholders*:

## 1. Unidades de Medida e Cronologia de Datas (UCS001, UCS002)
- **Potência:** O CA de Inclusão exige a Potência Nominal como número inteiro em Watts (W), enquanto a regra de exportação cita kW e MW sem estabelecer uma taxa oficial de conversão e arredondamento decimal.
- **Formato Temporal:** A especificação menciona "Data de Entrada em Operação (anos)", aplicando uma métrica de duração a um campo de data cadastral (`DD/MM/AAAA`).
- **Garantia em Meses:** Informar data de compra/instalação torna obrigatório o preenchimento de garantia em meses, mas não delimita o cálculo exato para conversão em dias em anos bissextos.

## 2. Topologia de Inversores e Herança de Usina (UCS001)
- O CA-2.1.2.1.11 estipula que a Usina da turbina é herdada do Inversor selecionado. Permanece em aberto se a interface deve exibir a Usina desabilitada para edição ou se o campo deve ser totalmente omitido do formulário de cadastro.

## 3. Matriz de Autorização (UCS001, UCS002, UCS003)
- Os requisitos originais referenciam papéis de "Administrador", "Gerente" e "Operador" sem fornecer a matriz consolidada de controle de acesso (RBAC) para as rotas de edição de status e de exportação de dados patrimoniais.

## 4. Bloqueio de Exclusão vs. Soft Delete (UCS001)
- Os critérios CA-2.1.2.4.02 e CA-2.1.2.4.03 determinam o bloqueio de exclusão quando existirem ordens de serviço ou registros de manutenção associados. É necessário esclarecer com os stakeholders se haverá suporte a desativação lógica (*soft delete*) ou se apenas a recusa da exclusão física é adotada.

## 5. Contrato de Formatação dos Relatórios (UCS002, UCS003)
- **Layout do PDF Coletivo:** Ao contrário do formato CSV (que define exatamente 13 colunas), o PDF coletivo não possui relação de campos delimitada pela especificação oficial.
- **Tratamento de Consulta Vazia:** Definir se a exportação em tela com zero registros deve desabilitar os botões de ação ou apresentar diálogo explicativo ao usuário.
