# Landscape e tendências · ler, comparar, produzir

[← Início](../README.md) · [Biblioteca](../biblioteca/README.md) · [Trilha CTI](CTI-DO-ZERO-AO-BRIEFING.md)

> Um relatório de landscape responde *o que mudou no ambiente de ameaças e o que isso exige de quem defende*. Ler um só é opinião; comparar vários, com método, é inteligência.

## O método de referência

A [ENISA Cybersecurity Threat Landscape Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology) (2025, atualizada em setembro de 2026) define como produzir panoramas **horizontais** (todas as ameaças), **temáticos** (uma ameaça ou tecnologia) e **setoriais** (um setor), com processos, partes interessadas, ferramentas e elementos de conteúdo. O resultado aplicado é o [ENISA Threat Landscape 2025](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025).

Use a metodologia como gabarito para **avaliar** qualquer relatório e para **produzir** o seu.

## Onde estão os relatórios

| Camada | Para quê | Fontes |
|---|---|---|
| Governamental | Visão de Estado, menos viés comercial | ENISA ETL · CERT-EU TLR · NCSC Annual Review · ASD Cyber Threat Report · Europol IOCTA |
| Brasil e LATAM | Contexto local | NIC.br/CERT.br (relatório de atividades) · CTIR Gov · BID/OEA 2020 |
| Fornecedores | Telemetria ampla, com viés de produto | Verizon DBIR · Mandiant M-Trends · Microsoft MDDR · CrowdStrike GTR |
| Acervos | Achar e comparar relatórios | awesome-annual-security-reports · ORKL · Malpedia Library · APTnotes · CyberMonitor · APT_REPORT |
| Dados brutos | Medir em vez de citar | VCDB (VERIS) · ransomware.live · CERT-EU TLR em JSON |

Todos estão na [biblioteca](../biblioteca/README.md) com links, ano e classificação de acesso.

## Missões

| # | Ação | Entregável |
|---|---|---|
| 1 | Ler o sumário executivo do ENISA ETL 2025 e listar as ameaças principais. | Lista com a definição que o relatório usa para cada ameaça |
| 2 | Escolher **uma** ameaça (ex.: ransomware) e achar como DBIR, M-Trends e CERT-EU a medem. | Tabela "métrica × fonte × período × amostra" |
| 3 | Marcar o que é **medido**, o que é **estimado** e o que é **opinião** em cada fonte. | Mesma tabela com coluna de natureza da evidência |
| 4 | Contrastar com o Brasil: ransomware.live filtrado por país + relatório do CERT.br. | Parágrafo "o que se confirma e o que não se aplica aqui" |
| 5 | Usar a estrutura da metodologia ENISA para um landscape **temático BR** de uma página. | Rascunho com escopo, fontes, ameaças, tendências e limitações |
| 6 | Revisar com o [template de revisão](../templates/REVISAO.md). | Versão final com incerteza declarada |

## Armadilhas de leitura

- **Amostra ≠ universo:** cada fornecedor vê só os próprios clientes.
- **Períodos diferentes:** ano fiscal, ano civil e janela de incidentes não se comparam sem ajuste.
- **Definições móveis:** "ransomware" ou "ataque" mudam de sentido entre relatórios.
- **Número de manchete:** "bilhões de tentativas" mede volume de varredura, não impacto.
- **Viés de sobrevivência:** só entra o que foi detectado — a ausência também é dado.

## Drives e coleções privadas

Coleções compartilhadas em drives raramente são indexadas por buscadores e mudam sem aviso. Prefira acervos versionados (GitHub) ou bibliotecas com API (ORKL). Se usar um drive de terceiros, registre data, dono e hash dos arquivos no [template de evidências](../templates/EVIDENCIAS.md).

## ▶ Próxima ação (uma só)
Abrir o ENISA Threat Landscape 2025 e copiar, para o `DIARIO.md`, a lista de ameaças principais com a definição de cada uma.
