# Procedência e verificação

## Origem
Esta biblioteca consolidou, em 2026-10-16, quatro listas de recomendações de CTI geradas com assistentes de IA, com foco em publicações da MITRE, materiais abertos, livros de 2025–2026 e ferramentas operacionais. Uma quinta lista era cópia idêntica de outra e foi descartada. Itens repetidos entre as listas foram fundidos num único registro.

## Método de verificação
Listas geradas por IA podem conter livros, autores ou links inexistentes. Cada item recebeu um status:

| Status | Critério |
|---|---|
| ✅ verificado | Existência confirmada por busca em 2026-10-16 (ISBN, página da editora ou PDF oficial) |
| 📘 conhecido | Referência consolidada na área (MITRE, OTRF, MISP, CISA); link original não reconferido |
| ⚠️ a verificar | Não foi possível conferir — validar antes de citar |
| ❌ não confirmado | Não encontrado; mantido só como registro, nunca citado |

## Correções feitas
- **Cyber Brief (CB25-10):** a lista apontava para um espelho em `azurewebsites.net`. A fonte oficial é o **CERT-EU** (`cert.europa.eu/publications/threat-intelligence`).
- **STIX e TAXII (MITRE):** as páginas são históricas (versões 1.x). Para uso atual, a referência é o STIX/TAXII 2.1 da OASIS.
- **MITRE Systems Engineering Guide:** o link era uma cópia em site de terceiro; anotado para preferir o download em mitre.org.
- **Cyber Denial, Deception and Counter Deception:** livro da Springer, não um PDF gratuito da MITRE.

## Não confirmados
- *The Art of Cyber Threat Intelligence: A Comprehensive Understanding* (Crawford Thomas, Springer).
- *Cybersecurity Knowledge Graphs in Action* (John Doty).
- *Master MITRE ATT&CK* (sem autor).

## Para manter
Ao adicionar uma fonte em `fontes.json`, comece com `a_verificar` e só promova para `verificado` depois de abrir o link ou achar o ISBN.
