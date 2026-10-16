# 04 · Forense Digital e Resposta a Incidentes (DFIR) ★★

> **Pergunta central:** o que aconteceu, quando, em qual sistema — e a evidência resiste a contestação?

## Conceitos
- Ordem de volatilidade (RFC 3227); aquisição, preservação, análise, relatório.
- Cadeia de custódia: reconhecimento, isolamento, fixação, coleta, acondicionamento, transporte, recebimento, processamento, armazenamento e descarte (CPP, art. 158-B).
- Ciclo de resposta: preparação → detecção/análise → contenção/erradicação/recuperação → lições aprendidas.

## Trilha D → S
- [ ] **D** — Ler os arts. 158-A a 158-F do CPP e a RFC 3227.
- [ ] **D** — Ciclo de resposta a incidentes (NIST SP 800-61).
- [ ] **C** — Aquisição de disco e memória com verificação por hash.
- [ ] **C** — Artefatos Windows: registro, prefetch, event logs, Amcache/ShimCache.
- [ ] **B** — Linha do tempo com plaso/log2timeline; análise com Autopsy.
- [ ] **B** — Memória com Volatility 3.
- [ ] **A** — Investigação de ransomware: entrada, movimentação lateral, exfiltração.
- [ ] **S** — Laudo/relatório pericial completo de um caso de laboratório.

## Fontes de referência
📚 Biblioteca curada desta disciplina, com status de verificação: [BIBLIOTECA.md](BIBLIOTECA.md)

- SANS DFIR — posters e cheat sheets.
- NIST SP 800-61 e SP 800-86.
- Brian Carrier — *File System Forensic Analysis*.
- ABNT NBR ISO/IEC 27037 — identificação, coleta, aquisição e preservação de evidência digital.
- Cursos AFD: *Incident Response* (concluído), *Ransomware Attack Investigation* (em andamento).

## Base legal
- CPP, arts. 158-A a 158-F — cadeia de custódia (Lei 13.964/2019, Pacote Anticrime).
- Marco Civil, arts. 13 e 15 — guarda de registros de conexão e de aplicação.
- LGPD, art. 48 — comunicação de incidente à ANPD e ao titular.
- Resolução CD/ANPD nº 15/2024 — regulamento de comunicação de incidente.

## Ponte com a psicologia
Pressão do incidente gera fechamento prematuro: a primeira explicação plausível vira "a" explicação. A linha do tempo é o antídoto — os fatos em ordem antes da história.

## Meus repos
- `investigador-cyber-90-dias` *(trilha)* · `ToolsGuide` *(trilha)*.

## ▶ Próxima ação (uma só)
Fazer a imagem de um pendrive de teste e registrar o hash antes e depois, num formulário de custódia.
