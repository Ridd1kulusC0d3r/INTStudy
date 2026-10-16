# 18 · IA Aplicada à Inteligência ★★

> **Pergunta central:** como a IA amplia o analista sem substituí-lo — e como sistemas de IA viram alvo?

## Conceitos
- LLMs: forças, alucinação, IA como apoio e não como fonte.
- Extração de entidades (NER), resumo, tradução, classificação.
- RAG com evidências citáveis e revisão humana.
- Ameaças a sistemas de IA: OWASP Top 10 for LLM, MITRE ATLAS.
- Avaliação: precisão, viés, rastreabilidade.

## Trilha D → S
- [ ] **D** — Testar um LLM em uma tarefa de OSINT e registrar onde ele errou.
- [ ] **C** — NER (GLiNER ou similar) em textos de investigação.
- [ ] **C** — RAG simples com citação obrigatória da fonte.
- [ ] **B** — Ler o OWASP Top 10 for LLM e o MITRE ATLAS.
- [ ] **B** — Prompt injection e riscos de agentes, pelo lado defensivo.
- [ ] **A** — Avaliação com conjunto rotulado: medir acerto e falsos positivos.
- [ ] **S** — Palestra/artigo "Inteligência Ampliada em Ação".

## Fontes de referência
- OWASP Top 10 for LLM Applications.
- MITRE ATLAS.
- NIST AI RMF 1.0.

## Base legal
- LGPD, art. 20 — revisão de decisões automatizadas.
- PL 2338/2023 (marco legal da IA no Brasil) — verificar o status de tramitação.
- EU AI Act — referência internacional.

## Ponte com a psicologia
Viés de automação: confiar na máquina porque ela soa segura. A fluência do texto não é evidência.

## Meus repos
- `OSINT-Colab` *(laboratório)* · `LLmInjection` *(fonte)* · `OsintUAI` *(divulgação)*.

## ▶ Próxima ação (uma só)
Rodar um notebook do OSINT-Colab sobre um texto público e marcar cada entidade que o modelo inventou.
