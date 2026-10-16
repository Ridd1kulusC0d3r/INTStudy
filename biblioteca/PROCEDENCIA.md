# Procedência, acesso e limites

[← Biblioteca](README.md) · [Registro da incorporação](../docs/CURADORIA-2026-10-16.md)

## Origem

O acervo inicial reunia listas de recomendações anteriores, algumas produzidas com auxílio de IA. Em 16/10/2026 foi incorporada a pesquisa desta conversa: publicações MITRE, livros de CTI, filtro posterior por acesso público e guias de FIRST, ENISA, MISP, CREST, ECB e governo britânico. Duplicatas foram fundidas por obra/edição, preservando IDs já existentes.

## Dimensões separadas

| Campo | Significado | O que não significa |
|---|---|---|
| `status` | Grau de identificação bibliográfica herdado ou revisto | Leitura integral, endosso ou garantia de disponibilidade |
| `acesso` | Aberto, pago ou restrito/não confirmado | Licença para republicar |
| `ano` | Ano conhecido; `null` quando não confirmado | Data de atualização automática |
| `temporalidade` | Filtro editorial: recente, histórico ou sem ano confirmado | Qualidade científica |
| `origem` | Acervo anterior ou pesquisa desta conversa | Autor original da obra |
| Auditoria HTTP | Resposta obtida pelo ambiente na data registrada | Conteúdo completo, integridade ou permanência do link |

`conhecido` indica referência identificada; `verificado` preserva conferência registrada na curadoria anterior. Não elevamos toda a lista a “verificado” após uma resposta HTTP. `a_verificar` e `nao_confirmado` exigem investigação bibliográfica adicional. O status não deve ser confundido com uma recomendação de leitura.

## Correções editoriais

- **Crawford Thomas:** *The Art of Cyber Threat Intelligence* existe. Apress informa e-book em janeiro de 2026 e copyright 2025. A marca anterior “não encontrado” foi corrigida. Continua comercial e fora da trilha aberta.
- **Recorded Future:** a página do handbook oferece download, mas a tentativa de acesso ao PDF direto redirecionou ao site na pesquisa. Preservado como acesso restrito/não confirmado, sem promessa de download livre.
- **Systems Engineering Guide:** substituído o espelho por endereço MITRE. A instituição também oferece pedido à equipe de arquivos; esse formulário não equivale a acesso direto.
- **Ten Strategies:** registro histórico separado; o link confirma a sucessora, não o acesso integral à primeira edição. Priorizar *11 Strategies*.
- **TARA:** um registro para a coleção (white paper, descrição de método, workshop e workbook), em vez de contar cada anexo como livro.
- **Medical Device Response:** inclui o guia rápido como complemento; o playbook de modelagem é uma obra distinta.
- **STIX/TAXII históricos:** textos antigos MITRE não são a especificação atual da OASIS.
- **NIST SP 800-160:** autoria institucional NIST com coautores MITRE, não uma publicação exclusiva MITRE.
- **ENISA / Attack Flow / INFORM:** datas relatadas nas páginas consultadas; nenhum ano foi deduzido só do caminho de upload.
- **Materiais comerciais:** preservados apenas para rastreabilidade. Nenhum exercício requer compra, cadastro comercial ou assinatura.

## Direitos e reprodução

Esta biblioteca referencia as obras em seus sites oficiais. Não redistribui PDFs de terceiros. “Aberto” aqui significa acesso público esperado ao material ou sua documentação, e não necessariamente licença aberta. Respeite a licença específica antes de copiar, adaptar ou redistribuir.

## Limitação da pesquisa

O inventário não é um catálogo completo de todas as publicações da MITRE nem uma revisão sistemática de toda a literatura de CTI. Não foi realizada leitura integral de todas as obras. As descrições sintetizam páginas oficiais, sumários e trechos consultados; prioridades e exercícios são elaboração editorial local.
