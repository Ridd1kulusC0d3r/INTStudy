# 17 · Arquitetura de Sistemas ★★

> **Pergunta central:** como organizar ferramentas e plataformas de inteligência para que cresçam sem virar caos?

## Conceitos
- Arquitetura hexagonal (portas e adaptadores): núcleo de domínio isolado das fontes e saídas.
- Modelo C4: contexto, contêiner, componente, código.
- ADR (Architecture Decision Record) e arc42.
- Atributos de qualidade: auditabilidade, segurança, desempenho, manutenibilidade.
- Modelagem de ameaças da própria arquitetura (STRIDE).
- Contratos entre módulos (JSONL, esquemas versionados).

## Trilha D → S
- [ ] **D** — Desenhar o diagrama C4 nível 1 de uma ferramenta sua.
- [ ] **D** — Linux e shell: processos, pipes, permissões, systemd.
- [ ] **C** — Escrever o primeiro ADR.
- [ ] **C** — Refatorar um coletor para arquitetura hexagonal (fonte = adaptador).
- [ ] **B** — Go para CLIs concorrentes; empacotamento e distribuição.
- [ ] **B** — STRIDE aplicado à sua ferramenta.
- [ ] **A** — Plugins e contratos versionados entre módulos.
- [ ] **S** — Arquitetura de referência DEIVOSINT (VÉRTICE, FAROL, GARIMPO, FIO, PRISMA).

## Fontes de referência
📚 Biblioteca curada desta disciplina, com status de verificação: [BIBLIOTECA.md](BIBLIOTECA.md)

- Richards & Ford — *Fundamentos da Arquitetura de Software*.
- Alistair Cockburn — *Hexagonal Architecture* (artigo original).
- Simon Brown — c4model.com; arc42.org.
- Adam Shostack — *Threat Modeling: Designing for Security*.
- The Twelve-Factor App.

## Base legal
- LGPD, art. 46 — segurança e privacidade desde a concepção.
- Decreto 11.856/2023 (PNCiber) — referência de segurança.

## Ponte com a psicologia
Lei de Conway: o sistema reflete a comunicação de quem o constrói. E arquitetura boa reduz carga cognitiva — essencial para quem mantém sozinho muitas ferramentas.

## Meus repos
- `TOCAIALinux` *(laboratório)* · `linux-para-osint-21-dias` *(trilha)* · `Cyber-Threat-Context-Modeling` *(método)* · `OsintbrFLOW` *(ferramenta)*.

## ▶ Próxima ação (uma só)
Escrever o ADR-001 do VÉRTICE: "por que o FAROL é um módulo separado e se comunica por JSONL".
