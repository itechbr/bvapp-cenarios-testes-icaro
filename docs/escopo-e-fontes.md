# 📌 Escopo e Fontes de Informação

**Autor:** Ícaro Pontes  
**Módulo:** Gestão de Ativos - Turbinas Eólicas  
**Projeto:** BVapp  

---

## 1. Origem dos Requisitos
Os cenários de teste documentados neste repositório foram elaborados utilizando como única fonte da verdade os requisitos funcionais oficiais da **Epic 2.1.2 — Gestão de Turbinas Eólicas**, abrangendo os artefatos de Especificação de Casos de Uso (CA), User Stories (US) e Rastreabilidade das seguintes *Features*:

*   **FEATURE-2.1.2.1:** Inclusão de turbinas eólicas
*   **FEATURE-2.1.2.2:** Consulta de turbinas eólicas
*   **FEATURE-2.1.2.3:** Atualização de turbinas eólicas
*   **FEATURE-2.1.2.4:** Exclusão de turbinas eólicas
*   **FEATURE:** Exportação de turbinas eólicas

---

## 2. Escopo Coberto
Os 10 cenários desenvolvidos cobrem:
1. **CRUD Completo e Integrado (UCS001):** Ciclo de vida completo do ativo (Inclusão, Consulta, Atualização e Exclusão) executado em um único fluxo integrador.
2. **Variação de Limites (UCS002):** Cadastro e manipulação de turbinas com capacidades máximas e grandes dimensões físicas.
3. **Validações e Tratamento de Erros (UCS003, UCS004, UCS005, UCS006, UCS007):** Rejeição de valores numéricos negativos, buscas/exclusões de IDs inexistentes, navegação em base vazia e proteção contra códigos duplicados.
4. **Exportação de Relatórios (UCS008, UCS009, UCS010):** Geração de relatórios em CSV/PDF/XLSX, herança de filtros ativos na tela e bloqueio de exportação de listas vazias.