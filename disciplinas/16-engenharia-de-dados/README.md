# 16 · Engenharia de Dados ★★

[← INTStudy](../../README.md) · [Mapa](../../docs/MAPA-DISCIPLINAS.md) · [Biblioteca aberta](BIBLIOTECA.md) · [Mesa de trabalho](../../templates/README.md)

> **Pergunta central:** como coletas de muitas fontes viram dados confiáveis, consultáveis e auditáveis — e alimentam detecção?

## Conceitos
- Formatos: CSV, JSON, JSONL, Parquet.
- Pipelines ETL/ELT, idempotência, reprocessamento.
- Esquemas de segurança: STIX 2.1, OCSF, Elastic ECS.
- Proveniência e linhagem: fonte, data, hash em cada registro.
- Grafos e resolução de entidades.
- Ciência de dados para detecção: baseline, anomalia, avaliação (precisão/recall).

## Trilha D → S
- [ ] **D** — SQL com `sqlite3` (stdlib).
- [ ] **D** — Converter saída JSONL de uma ferramenta sua em tabela.
- [ ] **C** — Modelagem: entidades, relações, chaves.
- [ ] **C** — DuckDB consultando Parquet/JSONL direto do disco.
- [ ] **B** — Mapear um log real para OCSF ou ECS.
- [ ] **B** — Proveniência: coluna de origem + hash + timestamp em todo registro.
- [ ] **A** — Grafo de vínculos (NetworkX) e consultas de caminho.
- [ ] **A** — Resolução de entidades e deduplicação.
- [ ] **A** — Detecção estatística simples (baseline × desvio) com avaliação de falsos positivos.
- [ ] **S** — Data lake de inteligência para o ecossistema DEIVOSINT.

## Fontes de referência
📚 Biblioteca curada desta disciplina, com status de verificação: [BIBLIOTECA.md](BIBLIOTECA.md)

- Reis & Housley — *Fundamentals of Data Engineering*.
- Martin Kleppmann — *Designing Data-Intensive Applications*.
- Documentação SQLite e DuckDB; OCSF Schema; Elastic Common Schema.

## Base legal
- LGPD, art. 6º — finalidade, necessidade (minimização), segurança.
- LGPD, art. 37 — registro das operações de tratamento.

## Ponte com a psicologia
Esquema é uma teoria: decidir o que vira coluna decide o que o analista consegue perguntar depois. Dado ausente no esquema vira ausência invisível.

## Meus repos
- `toolsR` (GARIMPO), `FIO`, `VINCULA`, `VeRTICE`, `OsintbrFLOW` *(ferramentas que produzem dados)*.
- `python-para-osint-21-dias` *(trilha)* · `ThePensieveProject` *(fonte)*.

## ▶ Próxima ação (uma só)
Carregar um JSONL de saída do GARIMPO num banco `sqlite3` e fazer uma consulta de contagem por tipo de entidade.
