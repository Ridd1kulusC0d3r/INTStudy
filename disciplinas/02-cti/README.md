# 02 · Cyber Threat Intelligence ★★★

> **Pergunta central:** quem pode nos atacar, como e por quê — e o que devemos detectar ou priorizar agora?

## Conceitos
- Níveis: estratégico (risco, tendência), operacional (campanhas), tático (TTPs), técnico (IOCs).
- IOC × TTP; Pirâmide da Dor (David Bianco).
- Modelos: MITRE ATT&CK, Diamond Model, Cyber Kill Chain, Unified Kill Chain.
- Padrões: STIX 2.1, TAXII, TLP 2.0; plataformas MISP e OpenCTI.
- CTI → detecção: hipótese, regra (Sigma/YARA), validação, feedback.

## Trilha D → S
- [ ] **D** — Navegar no ATT&CK Enterprise; distinguir tática, técnica e procedimento.
- [ ] **D** — Classificar 10 indicadores na Pirâmide da Dor.
- [ ] **C** — Aplicar Diamond Model e Kill Chain a um relatório público.
- [ ] **C** — Enriquecer IOCs com fontes abertas e atribuir confiança.
- [ ] **B** — Modelar um incidente em STIX 2.1 e importar no MISP ou OpenCTI.
- [ ] **B** — Escrever PIRs para um MSSP e para setores BR (financeiro, governo).
- [ ] **A** — Rastrear campanha: pivôs de infraestrutura, clusters, atribuição com controles (ACH).
- [ ] **A** — Transformar um TTP em regra Sigma testada.
- [ ] **A** — Modelagem de ameaças orientada por inteligência (TIEM/AXIS).
- [ ] **S** — Contribuir com o MITRE ATT&CK; relatório de campanha BR/LATAM publicado.

## Fontes de referência
📚 Biblioteca curada desta disciplina, com status de verificação: [BIBLIOTECA.md](BIBLIOTECA.md)

- MITRE ATT&CK, D3FEND e ATLAS.
- Roberts & Brown — *Intelligence-Driven Incident Response*.
- FIRST — CTI SIG Curriculum; FIRST TLP 2.0.
- OASIS — STIX 2.1 / TAXII 2.1.
- Documentação MISP e OpenCTI.
- CERT.br, CTIR Gov.

## Base legal
- Decreto 11.856/2023 — Política Nacional de Cibersegurança (PNCiber).
- Código Penal, art. 154-A (Lei 12.737/2012).
- LGPD — compartilhamento de indicadores que contenham dados pessoais (IPs, e-mails).
- Contratos/NDAs e TLP como regra de difusão.

## Ponte com a psicologia
Atribuição é o terreno mais fértil para viés: ancoragem no primeiro ator suspeito, espelhamento ("eles pensam como nós") e falsas bandeiras feitas para explorar exatamente isso.

## Meus repos
| Papel | Repo |
|---|---|
| Método | `Cyber-Threat-Context-Modeling` (TCE/TIEM+AXIS), `tocaia-osint` |
| Fonte | `apt4all`, `LLmInjection`, `ThePensieveProject` |
| Ferramenta | `tropeiro-intel` |
| Trilha | `investigador-cyber-90-dias` |
| Contribuição | `MrCl0wnLab/FraudNeuron` |

## ▶ Próxima ação (uma só)
Pegar um relatório público recente sobre um ator com atuação no Brasil e mapear 5 técnicas no ATT&CK Navigator.
