# 🎙️ Roteiro de Apresentação (Pitch de 5 Minutos)

**Aluno:** Ícaro Pontes  
**Módulo:** Gestão de Ativos - Turbinas Eólicas  
**Data:** 06/11/2026  

---

### [0:00 - 1:00] Introdução e Estrutura do Mini Projeto
"Boa tarde a todos e ao professor. Apresento o mini projeto de especificação de cenários de teste para o módulo de **Gestão de Turbinas Eólicas** do BVapp.

A organização do meu repositório no GitHub segue estritamente a arquitetura acordada pelo nosso grupo, inspirada no padrão de testes funcionais do Django/Python. Dentro de `functional_tests/ativos/turbinas_eolicas/`, elaborei **10 cenários de teste** mapeados diretamente sobre as especificações da Epic 2.1.2."

---

### [1:00 - 3:00] Destaque: Cenário Integrador UCS001 (CRUD Completo)
"O coração da minha entrega é o cenário **UCS001 — Manter Turbinas Eólicas**. Para atender com rigor aos critérios da avaliação, este teste engloba as quatro operações fundamentais do CRUD em uma única cadeia integradora:

1. **Inclusão (Create):** Cadastramos a turbina `TB-EOL-001` no *Parque Eólico Serra do Mel* com potência de 4200 kW e rotor de 150 metros.
2. **Consulta (Read):** Filtramos pelo código `TB-EOL-001` no grid e acessamos a tela de detalhes para garantir que a persistência foi idêntica aos dados inseridos.
3. **Atualização (Update):** Editamos a potência para 4500 kW e o status para *Em Manutenção*, validando a alteração no banco.
4. **Exclusão (Delete):** Acionamos a remoção, confirmamos na janela modal e fazemos a busca final para atestar o estado vazio."

---

### [3:00 - 4:15] Estratégia dos Cenários Complementares (UCS002 a UCS010)
"Além do CRUD feliz, estruturei os outros 9 cenários em três pilares estratégicos de testes de software:

* **Validação de Limites Numéricos (UCS002):** Testei uma turbina *offshore* de 15 MW e rotor de 236 metros para garantir que o banco de dados não sofra perda de precisão ou arredondamento.
* **Testes de Exceção e Fronteira (UCS003 a UCS007):** Mapeei o comportamento do sistema ao tentar cadastrar dados negativos, consultar ou excluir IDs inexistentes (retornando HTTP 404 tratado ao invés de erro 500) e navegar em uma base zerada.
* **Funcionalidade de Exportação (UCS008 a UCS010):** Validei a geração de relatórios em CSV/PDF, garantindo que o relatório herde os filtros ativos no grid e que a exportação seja bloqueada em telas sem registros."

---

### [4:15 - 5:00] Rastreabilidade, Dúvidas e Encerramento
"Toda a suíte possui rastreabilidade mapeada em `docs/matriz-rastreabilidade.md`. Também registrei em `docs/pendencias.md` duas dúvidas de requisitos para alinhamento com os *stakeholders*: a definição entre exclusão física ou *soft delete* para ativos antigos e o limite de registros em relatórios.

O repositório está organizado, documentado e pronto para reuso em futuras etapas de automação. Muito obrigado!"