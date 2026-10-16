# 12 · CYBINT — Inteligência de Infraestrutura Cibernética ★★

[← INTStudy](../../README.md) · [Mapa](../../docs/MAPA-DISCIPLINAS.md) · [Biblioteca aberta](BIBLIOTECA.md) · [Mesa de trabalho](../../templates/README.md)

> **Pergunta central:** quais ativos e infraestruturas existem no ciberespaço, como se conectam e o que expõem?

## Conceitos
- Superfície de ataque externa (ASM): domínios, subdomínios, IPs, serviços.
- DNS passivo, transparência de certificados (CT logs), RDAP.
- Roteamento: ASN, prefixos, BGP.
- Fingerprinting: JARM, favicon hash, cabeçalhos; correlação com CVEs.

## Trilha D → S
- [ ] **D** — Revisar TCP/IP, DNS, HTTP e TLS.
- [ ] **C** — Enumerar subdomínios por CT logs (crt.sh) e RDAP.
- [ ] **C** — DNS passivo e histórico de resolução.
- [ ] **B** — ASN, prefixos e BGP (bgp.he.net, RIPEstat).
- [ ] **B** — Shodan e Censys em escopo autorizado; correlação com NVD e CISA KEV.
- [ ] **A** — Clusterização de infraestrutura adversária (JARM, padrões de registro).
- [ ] **A** — ASM contínuo: inventário, mudança, alerta.
- [ ] **S** — Integração VÉRTICE + FAROL alimentando CTI (02).

## Fontes de referência
📚 Biblioteca curada desta disciplina, com status de verificação: [BIBLIOTECA.md](BIBLIOTECA.md)

- crt.sh; RDAP (IANA); RIPEstat; Hurricane Electric BGP Toolkit.
- Shodan e Censys (documentação).
- NVD, CISA KEV, FIRST EPSS.
- Registro.br.

## Base legal
- Código Penal, art. 154-A — coleta passiva sim; varredura ativa só com autorização.
- Marco Civil da Internet.
- Termos de uso das fontes e do Registro.br.

## Ponte com a psicologia
Infraestrutura adversária revela hábitos: provedores preferidos, padrões de nome, horários de registro — erros de OPSEC são comportamentais.

## Meus repos
- `VeRTICE` *(ferramenta)* · `farol` 🔒 *(ferramenta)* · `Cyber-Threat-Context-Modeling` *(método)* · `ToolsGuide` *(trilha)*.

## ▶ Próxima ação (uma só)
Consultar no crt.sh um domínio da sua própria organização (com autorização) e contar os subdomínios únicos.
