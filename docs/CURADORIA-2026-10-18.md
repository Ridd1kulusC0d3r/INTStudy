# Curadoria CTI · recursos indicados em 18/10/2026

[← Biblioteca](../biblioteca/README.md) · [Acervos e landscapes](../biblioteca/LANDSCAPES-E-TENDENCIAS.md)

## Decisões de inclusão

Foram lidos os quatro READMEs, os módulos main.py e threat_detector.py do dashboard e uma amostra de relatório do arquivo independente. A página de tópicos também foi consultada. Inclusão significa utilidade para estudo, não endosso de todas as afirmações nem validação operacional. Os links apontam aos projetos originais; não foram copiados relatórios ou dados de terceiros.

| Recurso | Classificação e limites |
|---|---|
| [Cyber Threat Intelligence — introdução em português](https://github.com/danieldonda/Cyber-Threat-Intelligence) | Introdução a CTI, geopolítica, atores estatais, hunting, IoCs/IoAs, LOLBins e TTPs. Material de apoio; distinções proativo/reativo são simplificações didáticas. Links externos podem exigir conta. |
| [Cyber Threat Intelligence Report — arquivo independente](https://github.com/gameworkerkim/CYBER-THREAT-INTELLIGENCE-REPORT) | Análises independentes baseadas em OSINT sobre APTs, supply chain, vulnerabilidades, IA/LLM e Web3. Índice e amostra consultados; fatos não auditados integralmente. Há inconsistência no uso de TLP:GREEN para publicação pública; consultar a nota de curadoria e FIRST antes de reutilizar. |
| [deepdarkCTI — diretório de fontes](https://github.com/fastfire/deepdarkCTI) | Diretório público de fontes deep/dark web, Telegram, Discord, ransomware, fóruns e métodos. O índice aberto não garante acesso público, estabilidade ou confiabilidade dos destinos; não é feed validado nem coleção de landscapes. |
| [Threat Detection Dashboard — laboratório com dados sintéticos](https://github.com/Vaskar71/Cybersecurity-Threat-Detection-and-Response-Dashboard) | Laboratório Python/PyQt5 com Isolation Forest. main.py e threat_detector.py inspecionados: treino e pontos simulados, sem captura de rede nesses módulos. Não validado em execução nem indicado como monitor de produção; anomalia sintética não demonstra ameaça real. |
| [GitHub Topics — cyber-threat-intelligence](https://github.com/topics/cyber-threat-intelligence) | Página dinâmica de descoberta por tópico, não catálogo revisado nem ranking de qualidade. Verificar escopo, código, licença e evidências de cada projeto antes de incorporar. |

## Leitura crítica e exercícios

- **Daniel Donda:** comece pelos conceitos em português e produza uma hipótese de hunting com evidência necessária e critério de refutação. Trate IoCs/IoAs no contexto; os rótulos proativo/reativo não bastam para avaliar uma investigação.
- **Arquivo Dennis Kim:** use a estrutura de relatório como exercício de análise. Escolha três afirmações, localize fontes primárias e registre confirmado / inferido / não corroborado. Não converta confiança declarada pelo autor em confiança própria sem verificação.
- **deepdarkCTI:** selecione categorias e produza um plano de coleta com procedência, atualização e acesso. O exercício pode ser feito somente com o índice público; não requer entrar em grupos ou mercados.
- **Dashboard:** explique como a geração de dados condiciona o resultado do detector. O código marca anomalias com protocolo 2 enquanto dados normais usam 0/1; esse atalho sintético limita a validade externa. Não foram instaladas dependências nem executado o projeto.
- **GitHub Topics:** selecione três projetos e compare finalidade, exemplos reproduzíveis, licença e manutenção. Estrelas e presença no tópico não demonstram qualidade.

## Evidência da avaliação

- [README Daniel Donda](https://github.com/danieldonda/Cyber-Threat-Intelligence/blob/main/README.md).
- [README do arquivo independente](https://github.com/gameworkerkim/CYBER-THREAT-INTELLIGENCE-REPORT/blob/main/README.md) e [amostra Scattered Spider](https://github.com/gameworkerkim/CYBER-THREAT-INTELLIGENCE-REPORT/blob/main/CTI-2026-0704-SCATTEREDSPIDER_EN.md). Amostra consultada quanto à estrutura; alegações não revalidadas como fatos nesta curadoria.
- [README deepdarkCTI](https://github.com/fastfire/deepdarkCTI/blob/main/README.md).
- [main.py](https://github.com/Vaskar71/Cybersecurity-Threat-Detection-and-Response-Dashboard/blob/main/main.py) e [threat_detector.py](https://github.com/Vaskar71/Cybersecurity-Threat-Detection-and-Response-Dashboard/blob/main/threat_detector.py).
- [FIRST — Traffic Light Protocol](https://www.first.org/tlp/): TLP:GREEN permite compartilhamento na comunidade, mas não em canais publicamente acessíveis. A apresentação de GREEN no arquivo independente é inconsistente com esse limite. Mantemos o link, sem republicar relatórios.

## Referência incidental não incorporada

O vídeo https://www.youtube.com/watch?v=YfD2ekCScdk apareceu como citação na mensagem, sem título ou explicação de pertinência. Não foi consumido nem classificado como material validado; permanece registrado aqui para rastreabilidade.
