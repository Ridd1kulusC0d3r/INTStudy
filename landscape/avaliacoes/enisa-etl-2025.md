# Avaliação · ENISA Threat Landscape 2025 (v1.3)

[← Radar](../README.md) · [Rubrica](../RUBRICA.md)

| Campo | Valor |
|---|---|
| Relatório | [ENISA Threat Landscape 2025](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) · PDF v1.3, set/2026 |
| Data da avaliação | 2026-10-17 |
| Natureza | **Preliminar** — extração automatizada de trecho do PDF; seções a partir de 7.1.2 e anexos não foram vistos por completo |
| Nota | **17 / 24** — faixa "útil, conferir antes de citar números" |

## Critérios

| # | Nota | Evidência | Observação |
|---|---|---|---|
| D1 | 1 | Sumário executivo, p. 6: "aimed at both strategic and operational audiences" | Público declarado; finalidade e decisões apoiadas não formalizadas |
| D2 | 2 | Metodologia, p. 7: 01/07/2024 a 30/06/2025, corte em 30/06/2025 | Ver A3: a seção 7 (p. 36) cita "July 2024 and July 2025" |
| C1 | 2 | p. 7: fontes abertas + informação anonimizada de Estados-Membros + Cyber Partnership Programme; FIMI com amostra do EEAS | — |
| C2 | 2 | p. 7: 4.875 incidentes | — |
| P1 | 2 | Metodologia CTL (nota 1, p. 7); 18 setores NIS2 (p. 16); anexo de TTPs (p. 64) | ⚠️ Uso de ATT&CK não confirmado no trecho lido |
| P2 | 1 | p. 16: 28,5% dos incidentes sem setor identificado | Deduplicação não descrita no trecho |
| A1 | 1 | p. 7: "words of estimative probability", com matriz no anexo | ⚠️ Matriz não vista; nota pode subir para 2 |
| A2 | 2 | p. 7: visibilidade desigual (ransomware e DDoS imediatos; espionagem documentada com 6 meses a 4+ anos de atraso), viés de interesse do público, dados FIMI não generalizáveis | Ponto mais forte do relatório |
| A3 | 1 | Divergências: finanças 4,5% (p. 16) × 4,7% (p. 24); DDoS 76,7% (p. 8) × 81,4% (p. 16); janela jun × jul | ⚠️ Podem ser denominadores diferentes. Se o PDF não explicar, a nota cai para 0 |
| S1 | 1 | Seções 10.3 a 10.8 (p. 61–62): hardening, acesso e privilégios, rede, monitoramento, resiliência | ⚠️ Texto das recomendações não lido |
| S2 | 1 | Apêndices de TTPs, vulnerabilidades e léxico (seção 12, p. 64–86) | Sem dados legíveis por máquina no trecho |
| F1 | 1 | Seção 13 (Log History, p. 87); versões v1.2 e v1.3 publicadas | ⚠️ Conteúdo do log não visto |

## Números de destaque (para conferir no PDF antes de citar)

- Phishing ≈ 60% dos casos; exploração de vulnerabilidades 21,3% (p. 8) — confirmar no PDF a que conjunto o percentual se refere.
- Administração pública é o setor mais visado: 38,2% (p. 16).
- Ransomware: 81,1% das atividades de cibercrime (p. 28).
- 46 intrusion sets ativos contra a UE (p. 36).

## O que aprender com esta avaliação

1. **Limitações declaradas valem ouro:** a ENISA diz *por que* espionagem aparece menos — porque é descoberta tarde, não porque é rara. Esse é o raciocínio da Detecção pela Ausência.
2. **Cheque os denominadores:** "% dos casos" e "% dos incidentes" podem não ser a mesma coisa.
3. **Leia o log de versões:** um relatório que chega à v1.3 foi corrigido; saiba o quê antes de citar a v1.0.

## ▶ Próxima ação
Abrir o PDF nas p. 8, 16 e 24 e decidir se A3 fica em 1 ou cai para 0.
