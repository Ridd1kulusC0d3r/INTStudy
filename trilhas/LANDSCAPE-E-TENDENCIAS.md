# Landscape e tendências · ler, comparar, produzir

[← Início](../README.md) · [Biblioteca](../biblioteca/README.md) · [Trilha CTI](CTI-DO-ZERO-AO-BRIEFING.md)

> Um relatório de landscape responde *o que mudou no ambiente de ameaças e o que isso exige de quem defende*. Ler um só é opinião; comparar vários, com método, é inteligência.

## O método de referência

A [ENISA Cybersecurity Threat Landscape Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology) (2025, atualizada em setembro de 2026) define como produzir panoramas **horizontais** (todas as ameaças), **temáticos** (uma ameaça ou tecnologia) e **setoriais** (um setor), com processos, partes interessadas, ferramentas e elementos de conteúdo. O resultado aplicado é o [ENISA Threat Landscape 2025](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025).

Use a metodologia como gabarito para **avaliar** qualquer relatório e para **produzir** o seu.

**Ferramentas desta trilha:** [Radar de Landscape](../landscape/README.md) (séries comparáveis, calendário e lacunas) · [Rubrica ENISA](../landscape/RUBRICA.md) · [Exemplo avaliado](../landscape/avaliacoes/enisa-etl-2025.md) · [Template do landscape BR](../templates/LANDSCAPE.md) · [Acervos, planilha e Drive](../biblioteca/LANDSCAPES-E-TENDENCIAS.md).

## Onde estão os relatórios

| Camada | Para quê | Fontes |
|---|---|---|
| Governos | Visão de Estado, menos viés comercial | ENISA ETL 2026 · CERT-EU TLR · NCSC · ASD · CCCS (Canadá) · ANSSI · BSI · CSA Singapura · ODNI · Europol IOCTA |
| Setoriais | Um setor em profundidade | ENISA Finance (com ECB) · ENISA Health · BCB — Relatório de Estabilidade Financeira |
| Brasil e LATAM | Contexto local | NIC.br/CERT.br · CTIR Gov · BCB · BID/OEA 2020 e 2025 · ESET Security Report LATAM · Recorded Future LATAM (pt) |
| Fornecedores | Telemetria ampla, com viés de produto | DBIR · M-Trends · MDDR · CrowdStrike · X-Force · Red Canary · FortiGuard · ESET · Google Forecast · Sophos |
| Acervos | Achar e comparar relatórios | awesome-annual-security-reports · ORKL · Malpedia · APTnotes · CyberMonitor · APT_REPORT |
| Dados | Medir em vez de citar | EuRepoC · CFR Cyber Operations Tracker · CISSM · Hackmageddon · VCDB · ransomware.live · CERT-EU em JSON |

Todos estão no [radar](../landscape/README.md) com publicador, base de evidência, periodicidade, formatos e relevância BR, e na [biblioteca](../biblioteca/README.md).

## Missões

| # | Ação | Entregável |
|---|---|---|
| 1 | Ler o sumário executivo do ENISA ETL 2026 e listar as ameaças principais. Comparar com o 2025: o período mudou de jul–jun para o ano civil. | Lista de ameaças com definições + nota sobre a sobreposição jan–jun/2025 |
| 2 | Escolher **uma** ameaça (ex.: ransomware) e achar como DBIR, M-Trends e CERT-EU a medem. | Tabela "métrica × fonte × período × amostra" |
| 3 | Marcar o que é **medido**, o que é **estimado** e o que é **opinião** em cada fonte. Avaliar uma delas pela [rubrica](../landscape/RUBRICA.md). | Tabela com natureza da evidência + uma avaliação em `landscape/avaliacoes/` |
| 4 | Contrastar com o Brasil: ransomware.live filtrado por país + relatório do CERT.br. | Parágrafo "o que se confirma e o que não se aplica aqui" |
| 5 | Preencher o [template do landscape BR](../templates/LANDSCAPE.md) para **um tema** (ex.: ransomware no Brasil). | Rascunho com direção, plano de coleta, ameaças, relevância BR e limitações |
| 6 | Revisar com o [template de revisão](../templates/REVISAO.md) e pontuar o próprio texto pela rubrica. | Versão final com nota ≥ 20/24 |

## Armadilhas de leitura

- **Amostra ≠ universo:** cada fornecedor vê só os próprios clientes.
- **Períodos diferentes:** ano fiscal, ano civil e janela de incidentes não se comparam sem ajuste. Exemplo real: o ETL 2025 cobre jul/2024–jun/2025 e o ETL 2026 cobre o ano civil de 2025.
- **Definições móveis:** "ransomware" ou "ataque" mudam de sentido entre relatórios.
- **Número de manchete:** "bilhões de tentativas" mede volume de varredura, não impacto.
- **Viés de sobrevivência:** só entra o que foi detectado — a ausência também é dado.

## Drives e coleções privadas

Coleções compartilhadas em drives raramente são indexadas por buscadores e mudam sem aviso. Prefira acervos versionados (GitHub) ou bibliotecas com API (ORKL). Se usar um drive de terceiros, registre data, dono e hash dos arquivos no [template de evidências](../templates/EVIDENCIAS.md).

## ▶ Próxima ação (uma só)
Abrir o ENISA Threat Landscape 2026 e copiar, para o `DIARIO.md`, a lista de ameaças principais com a definição de cada uma.
