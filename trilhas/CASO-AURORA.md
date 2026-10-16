# Caso Aurora · O domínio que parecia uma campanha

[← Trilha CTI](CTI-DO-ZERO-AO-BRIEFING.md) · [Templates](../templates/README.md)

> **Laboratório integralmente fictício.** Não pesquisar os personagens, não contatar pessoas e não consultar domínios reais. Os nomes e registros abaixo são dados de exercício, não evidências de uma campanha real.

Você é analista de uma cooperativa fictícia. A equipe pergunta: **devemos priorizar uma investigação sobre possível impersonação da marca ou tratar o alerta como ruído?** Há 45 minutos para recomendar a próxima coleta, não para atribuir autoria.

## Dossiê fornecido

| ID | Observação sintética | Limitação |
|---|---|---|
| E01 | Um alerta interno menciona `suporte-aurora.example` e um pedido de atualização cadastral. | O alerta não contém a mensagem original. |
| E02 | Dois blogs reproduzem o mesmo parágrafo sobre uma campanha financeira genérica. | Ambos dependem de uma única fonte; não são confirmações independentes. |
| E03 | A equipe informa que seu fornecedor envia campanhas de atualização cadastral. | Não foi fornecida a lista de domínios autorizados. |
| E04 | O assunto relatado contém urgência e prazo de 24 horas. | Esse padrão também pode ocorrer em comunicações legítimas. |
| E05 | Não há URL completa, cabeçalhos, amostra da página ou registro de acesso. | Não é possível afirmar execução, comprometimento ou técnica específica. |

## Sua investigação documental

1. Escreva um PIR com destinatário, prazo e decisão.
2. Compare **H1: impersonação maliciosa** e **H2: comunicação legítima ou alerta incorreto**.
3. Para cada observação, marque: favorece H1, favorece H2, neutra ou insuficiente.
4. Escolha duas coletas internas de maior valor informacional e justifique a ordem.
5. Escreva um briefing de até 200 palavras. Declare confiança e limitações.
6. Diga se existe evidência suficiente para mapear ATT&CK. É aceitável não mapear.

<details>
<summary><strong>Abra depois de concluir: roteiro de revisão</strong></summary>

A hipótese maliciosa é plausível, mas não está confirmada. E01 é relato indireto; E02 não corrobora o caso e não oferece duas fontes independentes; E04 não determina intenção. A mensagem original, obtida com tratamento apropriado dos dados, e a confirmação dos domínios autorizados do fornecedor discriminam melhor H1/H2 do que pesquisar um ator famoso.

Um produto defensável recomenda preservar o alerta, obter os artefatos faltantes e confirmar a legitimidade com o responsável interno. Não afirma comprometimento nem atribui ator. Probabilidade e confiança precisam de justificativa, não de um percentual inventado. Não há aqui descrição técnica suficiente para um mapeamento ATT&CK específico sustentado.

</details>
