# Contribuir para o INTStudy

[← Início](README.md)

1. Consulte `biblioteca/fontes.json` para evitar duplicatas de título ou edição.
2. Prefira página institucional e texto completo público. Registre autor/instituição, ano (ou `null`), tipo, acesso, disciplina e objetivo.
3. Acesso gratuito não é licença aberta. Não envie PDFs de terceiros sem verificar autorização.
4. Use `a_verificar` para existência/metadados incertos. Um HTTP 200 não basta para marcar conteúdo integral como acessível.
5. Mantenha livros pagos e links restritos no arquivo secundário; não os use como requisito de exercícios.
6. Explique por que uma fonte é central ou complementar e se é histórica. Não transforme data de upload em data de publicação.
7. Regere os índices e execute as verificações abaixo.

```bash
python3 tools/catalogo.py --checar
python3 tools/biblioteca.py
python3 tools/biblioteca.py --checar
python3 tools/verificar_interno.py
```

`tools/auditar_links.py` faz uma checagem de transporte com timeout e gera um registro; não contorna bloqueios e não prova leitura integral. Revise seus resultados antes de alterar o acesso de uma fonte.

Em contribuições textuais, cite as fontes e evite alegações de ranking, eficácia ou atualização sem evidência. Preserve a abrangência das 19 disciplinas.
