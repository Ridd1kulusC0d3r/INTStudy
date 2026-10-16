# Comece aqui

Uma ação por vez. Marque `[x]` quando concluir.

## Passo 1 — Base (semana 1)
- [ ] Fazer a **Próxima ação** de [00 · Fundamentos](disciplinas/00-fundamentos/).

## Passo 2 — Foco máximo (semanas 2–8, alternando dias)
- [ ] Próxima ação de [01 · OSINT](disciplinas/01-osint/).
- [ ] Próxima ação de [02 · CTI](disciplinas/02-cti/).
- [ ] Próxima ação de [03 · Malware/RE](disciplinas/03-malware-engenharia-reversa/) (montar o lab isolado).

## Passo 3 — Suporte (semanal)
- [ ] [07 · Psicologia](disciplinas/07-psicologia-investigativa/) — Key Assumptions Check numa investigação antiga.
- [ ] [16 · Dados](disciplinas/16-engenharia-de-dados/) — JSONL do GARIMPO no `sqlite3`.
- [ ] [17 · Arquitetura](disciplinas/17-arquitetura-de-sistemas/) — ADR-001 do VÉRTICE.

## Passo 4 — Amplitude (uma por mês)
- [ ] 04 DFIR → 05 SOCMINT → 12 CYBINT → 13 FININT → 08 GEOINT → 06 HUMINT → 09 SIGINT → 10 MASINT → 11 TECHINT → 14 CI → 15 Outras.

## Manter o catálogo
```bash
python3 tools/catalogo.py                        # regenera CATALOGO-REPOS.md
python3 tools/catalogo.py --checar               # valida (o mesmo que o GitHub Actions roda)
python3 tools/catalogo.py --verificar Ridd1kulusC0d3r   # lista repos públicos que faltam no repos.json
```
Ao criar um repo novo: adicione uma linha em `repos.json`, rode o primeiro comando e faça o commit.
