# 01 · OSINT — Inteligência de Fontes Abertas ★★★

> **Pergunta central:** o que informação publicamente acessível, coletada legalmente e com custódia, revela sobre o objeto da investigação?

## Conceitos
- Fonte aberta ≠ informação sem dono: público não significa livre de regras.
- Coleta passiva × ativa; pivô por identificador; verificação; proveniência.
- Cadeia de custódia digital: hash, timestamp, registro de coleta, reprodutibilidade.
- Fontes brasileiras: dados abertos de CNPJ, Diários Oficiais, tribunais, Portal da Transparência.

## Trilha D → S
- [ ] **D** — Estação de trabalho: navegador dedicado, perfil limpo, pasta de evidências por caso.
- [ ] **D** — Operadores de busca e arquivamento (Wayback Machine, archive.today).
- [ ] **C** — Pivôs: username, e-mail, telefone, domínio, imagem.
- [ ] **C** — Infraestrutura: WHOIS/RDAP, DNS, crt.sh.
- [ ] **C** — Fontes BR: CNPJ, Diários Oficiais, Jusbrasil, Portal da Transparência.
- [ ] **B** — Verificação de mídia: busca reversa, metadados, cronolocalização.
- [ ] **B** — Custódia: SHA-256, timestamps e relatório de coleta reproduzível.
- [ ] **A** — Automação em Python stdlib + shell com saída JSONL.
- [ ] **A** — Análise de vínculos em grafo com níveis de confiança.
- [ ] **S** — Detecção pela Ausência e OSINT comportamental (T.O.C.A.I.A.).

## Fontes de referência
- Bellingcat — *Online Investigations Toolkit*.
- ONU/Berkeley — *Berkeley Protocol on Digital Open Source Investigations*.
- Michael Bazzell — *OSINT Techniques*.
- OSINT Framework (osintframework.com).
- cipher387 — *Python for OSINT* e *Linux for OSINT* (21 dias).
- osintbrazuca/osint-brazuca.
- Wendt & Barreto (orgs.) — *Tratado de OSINT*.

## Base legal
- LGPD (Lei 13.709/2018) — finalidade, necessidade, bases legais.
- Marco Civil da Internet (Lei 12.965/2014).
- Lei de Acesso à Informação (Lei 12.527/2011).
- Código Penal, art. 154-A (Lei 12.737/2012) — invasão de dispositivo: o limite da coleta.
- CPP, arts. 158-A a 158-F — cadeia de custódia (Lei 13.964/2019).
- Termos de uso das plataformas.

## Ponte com a psicologia
A coleta é guiada pela hipótese do analista; o risco é colher só o que confirma. O registro de buscas *sem resultado* é a defesa — e a matéria-prima da Detecção pela Ausência.

## Meus repos
| Papel | Repo |
|---|---|
| Método | `tocaia-osint`, `osintchecklist` |
| Ferramenta | `FIO`, `Mineiro-OSINT-Extractor`, `toolsR` (GARIMPO), `VINCULA`, `OsintbrFLOW`, `VeRTICE`, `farol` 🔒 |
| Fonte | `OSINTList` 🔒, `OSINT` |
| Trilha | `python-para-osint-21-dias`, `linux-para-osint-21-dias`, `ToolsGuide` |
| Laboratório | `TOCAIALinux`, `OSINT-Colab`, `mineirohml` |

## ▶ Próxima ação (uma só)
Escolher um caso de estudo público e registrar a coleta de um único pivô (username) com hash SHA-256 de cada evidência.
