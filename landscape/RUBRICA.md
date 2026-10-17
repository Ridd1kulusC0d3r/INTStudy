# Rubrica de qualidade metodológica · baseada na ENISA CTL

[← Radar](README.md) · [Template do nosso landscape](../templates/LANDSCAPE.md) · [Exemplo avaliado](avaliacoes/enisa-etl-2025.md)

> Uma régua para comparar relatórios de landscape **pelo método**, não pela fama do publicador. Os critérios seguem as seis fases da [ENISA Cybersecurity Threat Landscape Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology) (direção, coleta, processamento, análise e produção, disseminação, feedback). A rubrica é elaboração do INTStudy, não um instrumento oficial da ENISA.

## Pontuação

Cada critério vale **0, 1 ou 2**. Total: **0–24**.

| Fase ENISA | # | Critério | 0 | 1 | 2 |
|---|---|---|---|---|---|
| Direção | D1 | Finalidade e público | ausentes | público citado sem escopo | finalidade, público e decisões apoiadas declarados |
| Direção | D2 | Período de observação | ausente | só o ano | datas de início, fim e corte |
| Coleta | C1 | Fontes identificadas | não informa | tipos genéricos | tipos de fonte e parceiros nomeados |
| Coleta | C2 | Amostra quantificada | sem números | números parciais | n de incidentes, organizações ou eventos |
| Processamento | P1 | Taxonomia declarada | nenhuma | implícita | explícita (taxonomia ENISA, ATT&CK, setores NIS2 etc.) |
| Processamento | P2 | Consolidação e dados ausentes | não trata | menciona | deduplicação e % de campos desconhecidos informados |
| Análise | A1 | Confiança e incerteza | afirmações sem qualificação | linguagem vaga | escala estimativa ou Admiralty aplicada |
| Análise | A2 | Limitações e vieses | nenhum | genéricos | específicos (cobertura, atraso, viés de reporte) |
| Análise | A3 | Consistência interna | contradições sem explicação | divergências menores ou explicáveis | números coerentes entre seções |
| Disseminação | S1 | Recomendações | ausentes | genéricas | acionáveis e por público |
| Disseminação | S2 | Formatos reutilizáveis | só PDF corrido | anexos (TTPs, léxico) | dados legíveis por máquina (JSON, CSV, STIX) |
| Feedback | F1 | Versões e correções | nenhuma | versões sem registro do que mudou | histórico com natureza e data das mudanças |

## Leitura da nota

| Faixa | Como usar o relatório |
|---|---|
| 20–24 | Base para tendências e comparação entre anos |
| 14–19 | Útil, mas confira os critérios com nota 0 ou 1 antes de citar números |
| 8–13 | Contexto e hipóteses; não sustente uma tendência só com ele |
| 0–7 | Material de divulgação; procure a fonte primária |

## Sinais de alerta (independem da nota)

- Número de manchete sem denominador ("bilhões de ataques").
- Comparação entre anos com mudança de método não declarada.
- Pesquisa de opinião apresentada como medição.
- Atribuição a Estado sem nível de confiança.
- Mesmo dado com valores diferentes em seções distintas.

## Como registrar uma avaliação

1. Copie [`avaliacoes/enisa-etl-2025.md`](avaliacoes/enisa-etl-2025.md) para `avaliacoes/<id>.md`.
2. Para cada critério, anote **nota + evidência (página ou seção)**. Sem evidência, nota 0.
3. Marque com ⚠️ o que veio de leitura parcial ou extração automatizada.
4. No bloco `landscape` da fonte em `biblioteca/fontes.json`, registre `avaliacao: {nota, maximo, arquivo, data, natureza}`.
5. Rode `python3 tools/landscape.py`.
