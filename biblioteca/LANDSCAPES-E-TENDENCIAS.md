# Observatório de leituras · landscapes e tendências

[← Biblioteca](README.md) · [Início](../README.md) · [Missões CTI](../trilhas/CTI-DO-ZERO-AO-BRIEFING.md) · **[Radar de Landscape](../landscape/README.md)**

> Curadoria de 16/10/2026. Acervos e índices públicos consultados na pesquisa; não houve validação individual de todos os PDFs. Acesso gratuito não implica licença para redistribuir. Este repositório cataloga links e não replica documentos de terceiros.

## Comece pela pergunta

| Objetivo | Prioridade |
|---|---|
| Comparar tendências anuais | Awesome Annual Security Reports + ENISA + CERT-EU |
| Investigar uma campanha | APTnotes + CyberMonitor + APT_REPORT |
| Relacionar aliases de atores | APT Groups and Operations; confirmar nas fontes |
| Construir corpus e análises | VCDB + APTnotes Markdown + CTI Crawler |

## Landscapes e tendências

| Recurso | Uso e limites |
|---|---|
| [Awesome Annual Security Reports](https://github.com/jacobdjwilson/awesome-annual-security-reports) | Relatórios anuais por ano e tema, PDFs e conversões Markdown. Inclui materiais de 2026. Confira estatísticas no PDF original; conversões usam IA. |
| [Threat Intel Reports — março de 2026](https://github.com/da5ch0/2026_03-threat-intel-reports) | Seleção de relatórios de terceiros referente a março de 2026; não pressupõe atualização contínua nem completude. |

## Campanhas e APTs

| Recurso | Uso e limites |
|---|---|
| [APTnotes — índice e documentos no Box](https://github.com/aptnotes/data) | Índice CSV/JSON com título, fonte, data, ano, hash e links Box. Página pública conferida; cada objeto Box não foi testado individualmente. |
| [APT & Cybercriminal Campaign Collections](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections) | Coleção cronológica de campanhas. Também contém amostras: para estudo documental, use relatórios. Não representa amostra estatística de todas as ameaças. |
| [APT_REPORT](https://github.com/blackorbird/APT_REPORT) | Relatórios, indicadores e materiais por grupo/operação; inclui amostras. Útil para pesquisa histórica e aprofundamento por ator. |

## Dados e automação

| Recurso | Uso e limites |
|---|---|
| [APTnotes em Markdown](https://github.com/alexander-hanel/APTnotes-md) | Conversões para busca, indexação e RAG; projeto orientado a processamento por LLMs. Para leitura e citação, consulte documentos originais. |
| [VERIS Community Database — VCDB](https://github.com/vz-risk/VCDB) | Incidentes divulgados publicamente em formato estruturado. Há vieses de seleção documentados; não equivale à base completa do DBIR. |
| [CTI Crawler](https://github.com/peng-gao-lab/cti-crawler) | Coleta e dataset de CTI com procedência. Deduplicar entre fontes e URLs antes de contar evidências. |

## Nuvem e índices de atores

| Recurso | Uso e limites |
|---|---|
| [APT Groups and Operations — Google Sheets](https://docs.google.com/spreadsheets/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/edit) | Leitura pública confirmada. Aliases, grupos, operações e fontes. Mapeamentos podem estar incorretos ou desatualizados; índice para pesquisa, não prova de atribuição. |

## Fontes institucionais

| Recurso | Uso e limites |
|---|---|
| [ENISA — catálogo Threat Landscape](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape) | Panoramas gerais, temáticos e setoriais. Usar com a metodologia ENISA já catalogada. |
| [CERT-EU — Threat Intelligence 2026](https://cert.europa.eu/publications/threat-intelligence/2026) | Publicações de inteligência e panoramas. Distinguir o ano da publicação do período analisado. |

## Acesso pendente

| Recurso | Uso e limites |
|---|---|
| [TTP Attribution — dataset anunciado no Google Drive](https://drive.google.com/drive/folders/1spjdXx_rCO6I1b4g_5X2C6ksJwlFN6Gu) | Pasta anunciada em https://github.com/KylaG/ttp_attribution com dataset de CTI, embeddings e resultados. Ferramenta de pesquisa não conseguiu abrir a pasta; acesso e conteúdo não confirmados. |

## Método: transformar a coleção em inteligência

Use a [ENISA Cybersecurity Threat Landscape Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology) para delimitar escopo e documentar a pesquisa. O roteiro abaixo é uma proposta de estudo do INTStudy, não uma reprodução normativa da ENISA.

1. Defina destinatário, decisão, setor, região e período de observação.
2. Registre título, autor, URL original, data de publicação, início/fim da observação, método, amostra e limitações.
3. Distinga telemetria, incidentes públicos e pesquisas de opinião; compare somente medidas compatíveis.
4. Deduplicate por documento/campanha: espelhos e forks não são evidências independentes.
5. Confira números e citações nos originais; conversões em Markdown podem conter erros.
6. Entregue três tendências sustentadas, uma hipótese alternativa e lacunas de coleta no [template de briefing](../templates/BRIEFING.md).

## Limites da busca em nuvem

A planilha Google foi acessada publicamente. O APTnotes fornece links Box, mas cada arquivo não foi testado. Não foi confirmada uma pasta Google Drive equivalente ao acervo anual. O dataset TTP Attribution permanece fora da seleção aberta até validação.
