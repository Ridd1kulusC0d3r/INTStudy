# CTI · Da pergunta ao briefing

[← Início](../README.md) · [Biblioteca](../biblioteca/README.md) · [Templates](../templates/README.md)

**Cenário:** você apoia uma organização fictícia brasileira e precisa recomendar onde aprofundar a coleta sobre ameaças. Nenhuma missão requer conta paga, dados pessoais reais ou infraestrutura de ataque.

| Missão | Leitura principal | Trabalho | Critério de conclusão |
|---|---|---|---|
| **01 / Orientar · D** | [FIRST Curriculum](https://www.first.org/global/sigs/cti/curriculum/) | Escrever um PIR e três questões subsidiárias. | Há destinatário, decisão, prazo e escopo explícitos. |
| **02 / Coletar · C** | [ENISA Methodology](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology) | Selecionar três fontes públicas e montar a matriz de evidências. | Cada afirmação possui URL, trecho/localização, data de consulta e limitação. |
| **03 / Analisar · C** | [FIRST Reporting](https://www.first.org/global/sigs/cti/curriculum/cti-reporting) | Formular duas hipóteses concorrentes e avaliar confiança. | Probabilidade e confiança são distintas; existe evidência que poderia refutar a conclusão. |
| **04 / Modelar · B** | [CISA ATT&CK Mapping](https://www.cisa.gov/news-events/news/best-practices-mitre-attckr-mapping) | Mapear até cinco comportamentos de um relatório público. | Cada técnica tem justificativa e evidência; comportamentos ambíguos podem ficar sem mapeamento. |
| **05 / Produzir · B** | [TIBER-EU TTIR](https://www.ecb.europa.eu/pub/pdf/annex/ecb.tiber_targeted_threat_intelligence_report_guidance_2025.en.pdf) | Escrever briefing de uma página e cenário contextualizado. | A recomendação responde ao PIR e distingue observação, inferência e cenário hipotético. |
| **06 / Revisar · A** | [MISP Best Practices](https://www.misp-project.org/best-practices-in-threat-intelligence.html) | Aplicar a rubrica e solicitar revisão quando houver colega disponível. | Corrigir ao menos uma fragilidade ou justificar, com evidência, por que nenhuma foi identificada. |

## Critério S · contribuir

Publique um produto reproduzível com bibliografia, método, escopo, data e limitações. Uma contribuição ao ATT&CK exige critérios próprios e aceite da equipe responsável; esta trilha não promete reconhecimento externo.

## Entregáveis

- `PIR.md`: uma pergunta vinculada a uma decisão.
- `EVIDENCIAS.md`: fontes e julgamentos rastreáveis.
- `BRIEFING.md`: conclusão, confiança, impacto e próxima ação.
- `REVISAO.md`: revisão de qualidade com pendências.

## Evite os três atalhos

1. Contar links como evidências independentes: várias páginas podem repetir a mesma fonte.
2. Atribuir ator só por técnica ou ferramenta: comportamentos podem ser compartilhados.
3. Converter frequência publicada em prevalência real: o conjunto observado sofre vieses de coleta e publicação.

**Autoavaliação:** consigo explicar por que minha recomendação mudaria se uma fonte-chave estivesse errada?
