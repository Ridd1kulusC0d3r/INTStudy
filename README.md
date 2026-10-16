# INTStudy — Ponto de Estudos de Inteligência

> Hub de estudos de **todas as disciplinas de inteligência**, com foco máximo em **OSINT**, **Cyber Threat Intelligence** e **Análise de Malware e Engenharia Reversa**, sustentado por **Engenharia de Dados** e **Arquitetura de Sistemas**.
> Mantido por **Deivison Lourenço** ([@Ridd1kulusC0d3r](https://github.com/Ridd1kulusC0d3r)) — pesquisador em OSINT/CTI, psicólogo e defensor da "Camada 8".

---

## Como funciona

Cada disciplina tem uma pasta em [`disciplinas/`](disciplinas/) com sempre as mesmas seções:

| Seção | Para quê |
|---|---|
| **Pergunta central** | O que essa INT responde |
| **Conceitos** | O mínimo para entender o campo |
| **Trilha D → S** | Checklist de progressão (ranks do OSINT no Jutsu) |
| **Fontes de referência** | Livros, frameworks, bases públicas |
| **Base legal** | Leis e normas brasileiras que delimitam a prática |
| **Ponte com a psicologia** | Onde o fator humano entra |
| **Meus repos** | Quais repositórios meus servem de fonte, ferramenta, método ou laboratório |
| **▶ Próxima ação** | **Uma** coisa para fazer agora |

O [`CATALOGO-REPOS.md`](CATALOGO-REPOS.md) classifica todos os meus repositórios por **papel** e por **disciplina**. Ele é gerado a partir de [`repos.json`](repos.json) por [`tools/catalogo.py`](tools/catalogo.py) (Python stdlib) e validado a cada push pelo GitHub Actions.

---

## Mapa das disciplinas

Pesos: ★★★ foco máximo · ★★ pilar de suporte · ★ cobertura completa.

### Base
| # | Disciplina | Peso |
|---|---|---|
| 00 | [Fundamentos de Inteligência](disciplinas/00-fundamentos/) | ★★ |

### Foco máximo
| # | Disciplina | Peso |
|---|---|---|
| 01 | [OSINT](disciplinas/01-osint/) | ★★★ |
| 02 | [Cyber Threat Intelligence](disciplinas/02-cti/) | ★★★ |
| 03 | [Análise de Malware e Engenharia Reversa](disciplinas/03-malware-engenharia-reversa/) | ★★★ |

### Técnica e análise
| # | Disciplina | Peso |
|---|---|---|
| 04 | [Forense Digital e Resposta a Incidentes (DFIR)](disciplinas/04-dfir/) | ★★ |
| 05 | [SOCMINT](disciplinas/05-socmint/) | ★★ |
| 06 | [HUMINT](disciplinas/06-humint/) | ★ |
| 07 | [Psicologia Investigativa (Camada 8)](disciplinas/07-psicologia-investigativa/) | ★★ |

### Coleta especializada
| # | Disciplina | Peso |
|---|---|---|
| 08 | [GEOINT / IMINT](disciplinas/08-geoint-imint/) | ★ |
| 09 | [SIGINT](disciplinas/09-sigint/) | ★ |
| 10 | [MASINT](disciplinas/10-masint/) | ★ |
| 11 | [TECHINT](disciplinas/11-techint/) | ★ |
| 12 | [CYBINT](disciplinas/12-cybint/) | ★★ |
| 13 | [FININT](disciplinas/13-finint/) | ★ |
| 14 | [Contrainteligência](disciplinas/14-contrainteligencia/) | ★ |
| 15 | [Outras INTs](disciplinas/15-outras-ints/) — MEDINT, NUCINT, ACINT, competitiva, CRIMINT/ISP | ★ |

### Pilares de engenharia
| # | Disciplina | Peso |
|---|---|---|
| 16 | [Engenharia de Dados](disciplinas/16-engenharia-de-dados/) | ★★ |
| 17 | [Arquitetura de Sistemas](disciplinas/17-arquitetura-de-sistemas/) | ★★ |
| 18 | [IA Aplicada à Inteligência](disciplinas/18-ia-aplicada/) | ★★ |

```
                       00 FUNDAMENTOS  ·  07 PSICOLOGIA (ponte com todas)
                                        │
  COLETA       01 OSINT · 05 SOCMINT · 06 HUMINT · 08 GEOINT · 09 SIGINT · 10 MASINT
                                        │
  DOMÍNIO      02 CTI ◄── 03 MALWARE/RE ◄── 04 DFIR      12 CYBINT · 11 TECHINT
                                        │                13 FININT · 14 CI · 15 OUTRAS
  ENGENHARIA   16 DADOS ── 17 ARQUITETURA ── 18 IA
```

---

## Ritmo (uma ação por vez)

- **Diário (25 min):** a "Próxima ação" de 01, 02 ou 03, alternando.
- **Semanal:** um item de 04–07 + um de 16–18.
- **Mensal:** uma disciplina ★ (08–15).
- **Sempre:** registrar no [`DIARIO.md`](DIARIO.md).

Comece por [`COMECE-AQUI.md`](COMECE-AQUI.md).

---

## Princípios

- **Evidência antes de conclusão:** fonte, data, hash e grau de confiança em tudo.
- **Ética e legalidade:** coleta passiva, LGPD, Marco Civil, CPP 158-A a 158-F, Berkeley Protocol.
- **Malware só no viés analítico e defensivo,** em laboratório isolado.
- **Simplicidade:** Python stdlib primeiro; shell e Go quando fizer sentido.
- **Somar, nunca substituir:** cada estudo adiciona a camada Brasil às referências originais, citando os autores.

---

## Licença

Conteúdo autoral sob CC BY 4.0 (sugestão — ajuste se preferir). Materiais de terceiros citados pertencem a seus autores.
