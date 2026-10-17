# Radar de Landscape · séries comparáveis de panorama e tendência

[← Início](../README.md) · [Trilha](../trilhas/LANDSCAPE-E-TENDENCIAS.md) · [Rubrica ENISA](RUBRICA.md) · [Template do nosso landscape](../templates/LANDSCAPE.md) · [Planilha](radar.csv) · [Observatório de acervos](../biblioteca/LANDSCAPES-E-TENDENCIAS.md)

> Gerado por `tools/landscape.py` a partir dos blocos `landscape` de `biblioteca/fontes.json`. Data de referência do calendário: **2026-10-17**. Para a situação de hoje: `python3 tools/landscape.py --hoje`.

## O que este radar faz que uma lista não faz

| Uma *awesome list* diz… | O radar diz também… |
|---|---|
| que o relatório existe | **quem publica** (governo, fornecedor, academia) e com que **base de evidência** |
| o ano | a **periodicidade**, o mês típico e **quando a próxima edição é esperada** |
| o link | os **formatos** — e se há dados legíveis por máquina para medir, não só citar |
| o tema | a **relevância para o Brasil** e onde estão as **lacunas** de cobertura |
| — | uma **nota de qualidade metodológica** pela [rubrica ENISA](RUBRICA.md), com avaliação documentada |

## Painel

- **52 séries** · 31 relatórios/métodos · 21 acervos e datasets · **11** com formato legível por máquina (JSON, CSV, Markdown ou API) · **1** avaliada(s) pela rubrica.
- **Publicador:** Governo **19** · Fornecedor **13** · Comunidade **11** · Academia **6** · Multilateral **2** · Terceiro setor **1**
- **Base de evidência:** curadoria **16** · incidentes públicos **10** · misto **7** · incidentes reportados ao órgão **6** · telemetria do fornecedor **6** · resposta a incidentes **2** · avaliação de maturidade **2** · pesquisa de opinião **2** · método **1**
- **Relevância BR:** média **29** · baixa **13** · alta **10**

### Matriz região × publicador

| Região | Governo | Multilateral | Terceiro setor | Fornecedor | Academia | Comunidade |
|---|---|---|---|---|---|---|
| Global | · | · | · | 10 | 6 | 11 |
| Europa | 10 | · | · | · | · | · |
| Brasil | 2 | · | 1 | · | · | · |
| América Latina | · | 2 | · | 2 | · | · |
| EUA | 1 | · | · | 1 | · | · |
| Reino Unido | 1 | · | · | · | · | · |
| Canadá | 1 | · | · | · | · | · |
| Austrália | 1 | · | · | · | · | · |
| França | 1 | · | · | · | · | · |
| Alemanha | 1 | · | · | · | · | · |
| Singapura | 1 | · | · | · | · | · |

## Relatórios horizontais · todas as ameaças

| Série | Publicador · região | Base de evidência | Periodicidade · edição | Formatos | BR | Rubrica |
|---|---|---|---|---|---|---|
| [ESET Security Report 2025 — Latinoamérica](https://www.welivesecurity.com/es/informes/eset-security-report-2025-ciberseguridad-empresas-latinoamerica/)<br><sub>empresas da América Latina</sub> | ESET · América Latina | pesquisa de opinião | anual · 2025 | pdf, html | ●●● | — |
| [Relatório de Atividades 2024 (inclui CERT.br)](https://nic.br/media/docs/publicacoes/9/20250424215104/relatorio-de-atividades-2024.pdf)<br><sub>notificações de incidentes ao CERT.br</sub> | NIC.br / CERT.br · Brasil | incidentes reportados ao órgão | anual · 2024 | pdf | ●●● | — |
| [CrowdStrike 2026 Global Threat Report](https://www.crowdstrike.com/en-au/resources/infographics/crowdstrike-2026-global-threat-report-highlights/) 🔒<br><sub>adversários e velocidade de intrusão</sub> | CrowdStrike · Global | telemetria do fornecedor | anual · 2026 | pdf, html | ●●○ | — |
| [Cyber Brief (mensal) — ex.: CB25-10, setembro de 2025](https://cert.europa.eu/publications/threat-intelligence/2025)<br><sub>síntese de fontes abertas</sub> | CERT-EU · Europa | curadoria | mensal · — | pdf, html, json, md | ●●○ | — |
| [Data Breach Investigations Report (DBIR) 2026](https://www.verizon.com/business/resources/reports/dbir/)<br><sub>violações de dados (esquema VERIS)</sub> | Verizon · Global | misto | anual · 2026 | pdf | ●●○ | — |
| [ENISA Threat Landscape 2025 (v1.3)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) ↳ *edição anterior*<br><sub>todas as ameaças · 18 setores NIS2</sub> | ENISA · Europa | incidentes públicos | anual · 2025 · v1.3 set/2026 | pdf | ●●○ | [17/24](../landscape/avaliacoes/enisa-etl-2025.md) |
| [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026)<br><sub>todas as ameaças · ano civil 2025</sub> | ENISA · Europa | incidentes públicos | anual · 2026 (set/2026) · cobre 2025 | pdf | ●●○ | — |
| [ESET Threat Report (semestral)](https://www.eset.com/int/business/threat-report/)<br><sub>telemetria de detecções</sub> | ESET Research · Global | telemetria do fornecedor | semestral · H1 2026 | pdf, html | ●●○ | — |
| [Global Threat Landscape Report 2026](https://www.bankinfosecurity.com/whitepapers/2026-global-threat-landscape-report-w-16451) 🔒<br><sub>telemetria global de ameaças</sub> | Fortinet FortiGuard Labs · Global | telemetria do fornecedor | anual · 2026 (abr/2026) | pdf | ●●○ | — |
| [M-Trends 2026](https://cloud.google.com/security/resources/m-trends)<br><sub>métricas de resposta a incidentes</sub> | Mandiant / Google Cloud · Global | resposta a incidentes | anual · 2026 | pdf | ●●○ | — |
| [Microsoft Digital Defense Report 2025](https://www.microsoft.com/en-us/corporate-responsibility/cybersecurity/microsoft-digital-defense-report-2025/)<br><sub>atores estatais e cibercrime</sub> | Microsoft · Global | telemetria do fornecedor | anual · 2025 | pdf, html | ●●○ | — |
| [Threat Landscape Report 2025](https://cert.europa.eu/publications/threat-intelligence/tlr2025/)<br><sub>instituições e órgãos da UE</sub> | CERT-EU · Europa | resposta a incidentes | anual · 2025 | pdf, html, json, md | ●●○ | — |
| [X-Force Threat Intelligence Index 2026](https://www.ibm.com/think/premium/threat-intelligence-report-about)<br><sub>vetores iniciais e impacto por setor e região (inclui LATAM)</sub> | IBM X-Force · Global | misto | anual · 2026 | pdf | ●●○ | — |
| [Annual Threat Assessment of the U.S. Intelligence Community 2026](https://www.dni.gov/index.php/ncsc-how-we-work/ncsc-know-the-risk-raise-your-shield/ncsc-awareness-materials/cyber-training-series/11382-newsroom/press-releases/press-releases-2026/4142-pr-03-26)<br><sub>ameaças à segurança nacional (inclui cibernético)</sub> | ODNI (EUA) · EUA | misto | anual · 2026 (mar/2026) | pdf | ●○○ | — |
| [ASD Annual Cyber Threat Report 2024–25](https://www.asd.gov.au/news/2025-10-14-australian-signals-directorate-releases-annual-cyber-threat-report-2024-25)<br><sub>ameaças à Austrália</sub> | Australian Signals Directorate (ACSC) · Austrália | incidentes reportados ao órgão | anual · 2024–25 | pdf, html | ●○○ | — |
| [Die Lage der IT-Sicherheit in Deutschland 2025](https://www.bsi.bund.de/DE/Service-Navi/Publikationen/Lagebericht/lagebericht_node.html)<br><sub>situação da segurança de TI na Alemanha</sub> | BSI (Alemanha) · Alemanha | misto | anual · 2025 | pdf | ●○○ | — |
| [National Cyber Threat Assessment 2025-2026](https://cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026)<br><sub>ameaças ao Canadá</sub> | Canadian Centre for Cyber Security · Canadá | misto | bienal · 2025–2026 (out/2024) | html, pdf | ●○○ | — |
| [NCSC Annual Review 2025](https://www.ncsc.gov.uk/collection/ncsc-annual-review-2025)<br><sub>incidentes nacionalmente significativos</sub> | NCSC (Reino Unido) · Reino Unido | incidentes reportados ao órgão | anual · 2025 | html, pdf | ●○○ | — |
| [Panorama de la cybermenace 2025](https://cyber.gouv.fr/nous-connaitre/publications/panoramas-de-la-cybermenace/panorama-de-la-cybermenace-2025/)<br><sub>ameaças à França</sub> | ANSSI (França) · França | incidentes reportados ao órgão | anual · 2025 (mar/2026) | pdf, html | ●○○ | — |
| [Singapore Cyber Landscape 2025/2026](https://isomer-user-content.by.gov.sg/36/e3a2bc10-c70a-4b06-bf46-4847e1d8b358/Singapore%20Cyber%20Landscape%202025_2026.pdf)<br><sub>ameaças a Singapura</sub> | Cyber Security Agency of Singapore · Singapura | incidentes reportados ao órgão | anual · 2025/2026 (jul/2026) | pdf | ●○○ | — |

## Relatórios setoriais

| Série | Publicador · região | Base de evidência | Periodicidade · edição | Formatos | BR | Rubrica |
|---|---|---|---|---|---|---|
| [ENISA Threat Landscape: Finance Sector](https://www.enisa.europa.eu/publications/enisa-threat-landscape-finance-sector)<br><sub>setor financeiro</sub> | ENISA / ECB · Europa | incidentes públicos | pontual · 2024 (fev/2025) | pdf | ●●● | — |
| [Relatório de Estabilidade Financeira (REF)](https://www.bcb.gov.br/publicacoes/ref)<br><sub>sistema financeiro (risco cibernético é uma seção)</sub> | Banco Central do Brasil · Brasil | incidentes reportados ao órgão | semestral · nov/2025 | pdf, html | ●●● | — |
| [ENISA Threat Landscape: Health Sector](https://www.enisa.europa.eu/publications/health-threat-landscape)<br><sub>saúde</sub> | ENISA · Europa | incidentes públicos | pontual · 2023 | pdf | ●●○ | — |

## Relatórios temáticos

| Série | Publicador · região | Base de evidência | Periodicidade · edição | Formatos | BR | Rubrica |
|---|---|---|---|---|---|---|
| [Panorama do cibercrime na América Latina e Caribe](https://www.recordedfuture.com/research/latin-america-and-the-caribbean-cybercrime-landscape-pt)<br><sub>cibercrime na região</sub> | Recorded Future (Insikt Group) · América Latina | telemetria do fornecedor | pontual · — | html, pdf | ●●● | — |
| [Relatório de Cibersegurança 2020: riscos, avanços e o caminho a seguir na América Latina e Caribe](https://publications.iadb.org/pt/relatorio-de-ciberseguranca-2020-riscos-avancos-e-o-caminho-seguir-na-america-latina-e-caribe)<br><sub>maturidade de capacidades (CMM)</sub> | BID / OEA · América Latina | avaliação de maturidade | pontual · 2020 | pdf | ●●● | — |
| [Relatório de cibersegurança 2025: vulnerabilidade e desafios de maturidade para reduzir lacunas na América Latina e no Caribe](https://publications.iadb.org/en/2025-cybersecurity-report-vulnerability-and-maturity-challenges-bridging-gaps-latin-america-and)<br><sub>maturidade de capacidades (CMM) · 30 países</sub> | BID / OEA · América Latina | avaliação de maturidade | pontual · 2025 | pdf | ●●● | — |
| [Cybersecurity Forecast 2026](https://cloud.google.com/security/resources/cybersecurity-forecast)<br><sub>previsões para o ano seguinte</sub> | Google Cloud Security · Global | misto | anual · 2026 (nov/2025) | pdf, html | ●●○ | — |
| [Internet Organised Crime Threat Assessment (IOCTA) 2025](https://eucrim.eu/news/iocta-2025/)<br><sub>crime organizado online</sub> | Europol · Europa | misto | anual · 2025 · há edição 2026 | pdf | ●●○ | — |
| [Threat Detection Report 2026 — metodologia](https://redcanary.com/threat-detection-report/methodology/)<br><sub>técnicas ATT&CK mais detectadas</sub> | Red Canary · Global | telemetria do fornecedor | anual · 2026 | html, pdf | ●●○ | — |
| [The State of Ransomware in the US 2025](https://assets.sophos.com/X24WTUEQ/at/k7f88k4hqrgw9fqkknvctrp/sophos-state-of-ransomware-in-us-2025.pdf)<br><sub>ransomware (pesquisa com vítimas)</sub> | Sophos · EUA | pesquisa de opinião | anual · 2025 | pdf | ●○○ | — |

## Métodos

| Série | Publicador · região | Base de evidência | Periodicidade · edição | Formatos | BR | Rubrica |
|---|---|---|---|---|---|---|
| [ENISA Cybersecurity Threat Landscape Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology)<br><sub>metodologia CTL (ETL, setorial, temático)</sub> | ENISA · Europa | método | pontual · 2025 · atualizada set/2026 | pdf, html | ●●● | — |

## Acervos de relatórios

| Série | Publicador · região | Base de evidência | Periodicidade · edição | Formatos | BR | Rubrica |
|---|---|---|---|---|---|---|
| [CTIR Gov — alertas e centrais de conteúdo](https://www.gov.br/ctir/pt-br)<br><sub>alertas e recomendações à APF</sub> | CTIR Gov / GSI-PR · Brasil | curadoria | contínua · — | html, pdf | ●●● | — |
| [APTnotes](https://github.com/kbandla/APTnotes)<br><sub>relatórios de APT por ano</sub> | kbandla / comunidade (GitHub) · Global | curadoria | contínua · — | pdf | ●●○ | — |
| [APTnotes em Markdown](https://github.com/alexander-hanel/APTnotes-md)<br><sub>relatórios de APT convertidos</sub> | alexander-hanel · Global | curadoria | pontual · — | md | ●●○ | — |
| [APTnotes — índice e documentos no Box](https://github.com/aptnotes/data)<br><sub>índice de relatórios de APT</sub> | APTnotes · Global | curadoria | contínua · — | csv, json | ●●○ | — |
| [awesome-annual-security-reports](https://github.com/jacobdjwilson/awesome-annual-security-reports)<br><sub>relatórios anuais por ano e tema</sub> | jacobdjwilson (GitHub) · Global | curadoria | contínua · — | md, pdf | ●●○ | — |
| [CERT-EU — Threat Intelligence 2026](https://cert.europa.eu/publications/threat-intelligence/2026)<br><sub>publicações de inteligência do ano</sub> | CERT-EU · Europa | curadoria | contínua · — | html, json, md | ●●○ | — |
| [ENISA — catálogo Threat Landscape](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape)<br><sub>ETL, setoriais e temáticos</sub> | ENISA · Europa | curadoria | contínua · — | html | ●●○ | — |
| [Malpedia — Library](https://malpedia.caad.fkie.fraunhofer.de/library)<br><sub>bibliografia por família e ator</sub> | Fraunhofer FKIE · Global | curadoria | contínua · — | html | ●●○ | — |
| [ORKL — biblioteca de relatórios de CTI](https://orkl.eu/)<br><sub>biblioteca pesquisável de CTI</sub> | ORKL · Global | curadoria | contínua · — | html, api | ●●○ | — |
| [APT & Cybercriminal Campaign Collections](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections)<br><sub>campanhas por ano</sub> | CyberMonitor (GitHub) · Global | curadoria | contínua · — | pdf | ●○○ | — |
| [APT_REPORT](https://github.com/blackorbird/APT_REPORT)<br><sub>relatórios e IOCs por ator</sub> | blackorbird (GitHub) · Global | curadoria | contínua · — | pdf | ●○○ | — |
| [Threat Intel Reports — março de 2026](https://github.com/da5ch0/2026_03-threat-intel-reports)<br><sub>seleção de março de 2026</sub> | da5ch0 · Global | curadoria | pontual · mar/2026 | pdf | ●○○ | — |

## Datasets e rastreadores · medir em vez de citar

| Série | Publicador · região | Base de evidência | Periodicidade · edição | Formatos | BR | Rubrica |
|---|---|---|---|---|---|---|
| [ransomware.live](https://www.ransomware.live/about)<br><sub>vítimas de ransomware por grupo, setor e país</sub> | Julien Mousqueton · Global | incidentes públicos | contínua · — | html | ●●● | — |
| [CISSM Cyber Events Database](https://cissm.umd.edu/cissm-cyber-events-database)<br><sub>eventos públicos codificados</sub> | University of Maryland (CISSM) · Global | incidentes públicos | contínua · — | html, csv | ●●○ | — |
| [CTI Crawler](https://github.com/peng-gao-lab/cti-crawler)<br><sub>corpus de CTI com procedência</sub> | peng-gao-lab · Global | curadoria | pontual · — | json | ●●○ | — |
| [Cyber Operations Tracker](https://www.cfr.org/cyber-operations)<br><sub>operações patrocinadas por Estados</sub> | Council on Foreign Relations · Global | incidentes públicos | contínua · — | html | ●●○ | — |
| [European Repository of Cyber Incidents (EuRepoC)](https://www.swp-berlin.org/en/swp/about-us/organization/swp-projects/european-repository-on-cyber-incidents-eurepoc/)<br><sub>incidentes politicamente relevantes</sub> | EuRepoC (consórcio acadêmico, com SWP Berlin) · Global | incidentes públicos | contínua · — | html, csv | ●●○ | — |
| [HACKMAGEDDON — timelines e estatísticas](https://www.hackmageddon.com/)<br><sub>ataques divulgados publicamente</sub> | Paolo Passeri · Global | incidentes públicos | mensal · — | html | ●●○ | — |
| [VERIS Community Database (VCDB)](https://github.com/vz-risk/VCDB)<br><sub>incidentes públicos em VERIS</sub> | Verizon (vz-risk) · Global | incidentes públicos | contínua · — | json | ●●○ | — |
| [APT Groups and Operations — Google Sheets](https://docs.google.com/spreadsheets/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/edit)<br><sub>aliases de grupos e operações</sub> | Florian Roth e colaboradores · Global | curadoria | contínua · — | planilha | ●○○ | — |
| [TTP Attribution — dataset anunciado no Google Drive](https://drive.google.com/drive/folders/1spjdXx_rCO6I1b4g_5X2C6ksJwlFN6Gu) 🔒<br><sub>dataset de atribuição por TTP</sub> | KylaG · Global | curadoria | pontual · — | drive | ●○○ | — |

BR: ●●● dados ou foco no Brasil/LATAM · ●●○ comparação útil · ●○○ contexto externo. 🔒 = cadastro ou acesso restrito.

## Calendário de vigilância

Próxima edição esperada de séries periódicas, calculada a partir da edição catalogada e do mês típico de publicação. Referência: 2026-10-17.

| Série | Edição catalogada | Próxima esperada | Situação |
|---|---|---|---|
| [ASD Annual Cyber Threat Report 2024–25](https://www.asd.gov.au/news/2025-10-14-australian-signals-directorate-releases-annual-cyber-threat-report-2024-25) | 2024–25 | out/2026 | ⚠️ conferir se já saiu e atualizar o registro |
| [National Cyber Threat Assessment 2025-2026](https://cyber.gc.ca/en/guidance/national-cyber-threat-assessment-2025-2026) | 2025–2026 (out/2024) | out/2026 | ⚠️ conferir se já saiu e atualizar o registro |
| [Cybersecurity Forecast 2026](https://cloud.google.com/security/resources/cybersecurity-forecast) | 2026 (nov/2025) | nov/2026 | aguardar |
| [CrowdStrike 2026 Global Threat Report](https://www.crowdstrike.com/en-au/resources/infographics/crowdstrike-2026-global-threat-report-highlights/) | 2026 | fev/2027 | aguardar |
| [Annual Threat Assessment of the U.S. Intelligence Community 2026](https://www.dni.gov/index.php/ncsc-how-we-work/ncsc-know-the-risk-raise-your-shield/ncsc-awareness-materials/cyber-training-series/11382-newsroom/press-releases/press-releases-2026/4142-pr-03-26) | 2026 (mar/2026) | mar/2027 | aguardar |
| [Panorama de la cybermenace 2025](https://cyber.gouv.fr/nous-connaitre/publications/panoramas-de-la-cybermenace/panorama-de-la-cybermenace-2025/) | 2025 (mar/2026) | mar/2027 | aguardar |
| [Global Threat Landscape Report 2026](https://www.bankinfosecurity.com/whitepapers/2026-global-threat-landscape-report-w-16451) | 2026 (abr/2026) | abr/2027 | aguardar |
| [Data Breach Investigations Report (DBIR) 2026](https://www.verizon.com/business/resources/reports/dbir/) | 2026 | mai/2027 | aguardar |
| [Singapore Cyber Landscape 2025/2026](https://isomer-user-content.by.gov.sg/36/e3a2bc10-c70a-4b06-bf46-4847e1d8b358/Singapore%20Cyber%20Landscape%202025_2026.pdf) | 2025/2026 (jul/2026) | jul/2027 | aguardar |
| [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026) | 2026 (set/2026) · cobre 2025 | set/2027 | aguardar |

## Lacunas de cobertura

- **Brasil:** nenhuma série governamental *horizontal e anual* equivalente ao ETL da ENISA neste radar. Existem peças setoriais (BCB), estatísticas de notificação (NIC.br/CERT.br) e alertas (CTIR Gov). **Oportunidade:** produzir um landscape BR com o [template](../templates/LANDSCAPE.md).
- **Dados abertos BR/LATAM:** nenhuma série regional com formato legível por máquina. Para medir tendências locais, filtrar bases globais por país (ransomware.live, EuRepoC, CISSM) e declarar o viés de cobertura.
- **Qualidade:** 30 relatórios ainda sem avaliação pela rubrica. Uma por semana fecha o radar em poucos meses.

## Avaliações pela rubrica ENISA

| Série | Nota | Natureza | Data |
|---|---|---|---|
| [ENISA Threat Landscape 2025 (v1.3)](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) | [17/24](../landscape/avaliacoes/enisa-etl-2025.md) | preliminar | 2026-10-17 |

## Como ampliar

1. Acrescente a fonte em `biblioteca/fontes.json` com o bloco `landscape` (vocabulário em `tools/landscape.py`).
2. Preencha `ano_edicao` e `mes_tipico` só com evidência da data de publicação.
3. Rode `python3 tools/biblioteca.py && python3 tools/landscape.py` e faça o commit.
4. Para avaliar: copie a [rubrica](RUBRICA.md) para `landscape/avaliacoes/<id>.md` e registre `avaliacao` no bloco.
