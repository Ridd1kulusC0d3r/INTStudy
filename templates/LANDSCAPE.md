# Landscape de ameaças · modelo BR

> Estrutura adaptada das seis fases da [ENISA CTL Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology), com relevância medida para o Brasil. Antes de publicar, pontue o próprio texto pela [rubrica](../landscape/RUBRICA.md): a meta é ≥ 20/24.

**Título:**  
**Tipo:** ☐ horizontal (todas as ameaças) ☐ setorial (setor: ____) ☐ temático (tema: ____)  
**Versão / data de publicação:**  
**Marcação TLP:** ☐ CLEAR ☐ GREEN ☐ AMBER  
**Autoria e revisão:**

---

## 1 · Direção

| Item | Preenchimento |
|---|---|
| Finalidade | Que decisão este landscape apoia? |
| Público | ☐ estratégico (direção, conselho) ☐ tático (arquitetura, detecção, hunting) ☐ operacional (resposta, SOC) |
| Requisitos de inteligência | 3 a 5 perguntas — use o [modelo de PIR](PIR.md) |
| Período de observação | de __/__/____ a __/__/____ · corte em __/__/____ |
| Fora do escopo | O que deliberadamente não será tratado |

## 2 · Plano de coleta

| Fonte | Tipo | Confiabilidade (A–F) | Cobertura e viés | Frequência |
|---|---|---|---|---|
| Ex.: notificações CERT.br | estatística nacional | B | só incidentes notificados | anual |
| Ex.: ransomware.live filtrado por BR | sites de vazamento | C | só vítimas expostas publicamente | contínua |
| Ex.: relatório de fornecedor | telemetria | C | base de clientes do fornecedor | anual |

Fontes no [radar](../landscape/README.md). Registre cada evidência na [matriz de evidências](EVIDENCIAS.md).

## 3 · Processamento

- **Taxonomia de ameaças:** ☐ taxonomia ENISA ☐ outra: ____
- **Comportamento:** MITRE ATT&CK (técnica + ID)
- **Contexto estratégico:** PESTEL
- **Setores:** ☐ PNSIC (Decreto 9.573/2018) ☐ 18 setores NIS2 (para comparar com a ENISA)
- **Deduplicação:** como espelhos, republicações e incidentes repetidos foram tratados
- **Dados ausentes:** % de registros sem setor, ator ou vetor

## 4 · Análise e produção

### Sumário executivo
Três a cinco julgamentos, cada um com nível de confiança.

### Panorama por ameaça
Repita o bloco para cada ameaça principal:

| Campo | Conteúdo |
|---|---|
| Ameaça | |
| O que mudou no período | |
| Evidência (n, fontes) | |
| Atores e motivação | estatal · cibercrime · hacktivismo |
| Técnicas ATT&CK | |
| Setores BR afetados | |
| **Relevância BR** | ☐ ALTA ☐ MÉDIA ☐ BAIXA — critério: efeito possível sobre serviços essenciais e sobre a confiança em serviços digitais no Brasil |
| Confiança | escala estimativa + Admiralty das fontes-chave |
| Hipótese alternativa | |

### Tendências
Só tendências sustentadas por **duas ou mais fontes independentes** e por **medidas compatíveis**.

### Comparação com o panorama internacional
O que se confirma no Brasil, o que diverge e por quê. Base: ENISA ETL, CERT-EU, DBIR, M-Trends.

### Limitações e vieses
Cobertura, atraso de descoberta (espionagem aparece tarde), viés de reporte, idioma das fontes.

## 5 · Disseminação

- **Recomendações estratégicas** (direção):
- **Recomendações operacionais** (SOC, detecção, resposta):
- **Anexos:** ☐ TTPs ☐ vulnerabilidades exploradas (CVE + KEV) ☐ léxico ☐ dados em CSV/JSON

## 6 · Feedback e versões

| Versão | Data | Mudança | Natureza (editorial ou substantiva) |
|---|---|---|---|
| 1.0 | | Publicação | — |

Canal de feedback:  
Data prevista da próxima edição:
