#!/usr/bin/env python3
"""
landscape.py — gera o Radar de Landscape a partir dos blocos `landscape` de biblioteca/fontes.json.

Saídas (reprodutíveis, sem rede):
    landscape/README.md   radar com painel, matriz, séries, calendário de vigilância e lacunas
    landscape/radar.csv   mesma base em planilha

O calendário usa `radar_referencia` de fontes.json (não a data de hoje), para o CI
continuar reprodutível. Para ver a situação na data atual sem gravar nada:
    python3 tools/landscape.py --hoje

Uso:
    python3 tools/landscape.py            # regenera
    python3 tools/landscape.py --checar   # valida e confere se os arquivos estão em dia
"""
import csv
import io
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTES = ROOT / "biblioteca" / "fontes.json"
OUT_MD = ROOT / "landscape" / "README.md"
OUT_CSV = ROOT / "landscape" / "radar.csv"

VOC = {
    "publicador_tipo": {"governo": "Governo", "multilateral": "Multilateral", "terceiro-setor": "Terceiro setor",
                        "fornecedor": "Fornecedor", "academia": "Academia", "comunidade": "Comunidade"},
    "regiao": {"global": "Global", "europa": "Europa", "brasil": "Brasil", "latam": "América Latina",
               "eua": "EUA", "reino-unido": "Reino Unido", "canada": "Canadá", "australia": "Austrália",
               "franca": "França", "alemanha": "Alemanha", "singapura": "Singapura"},
    "escopo": {"horizontal": "Horizontal", "setorial": "Setorial", "tematico": "Temático",
               "metodo": "Método", "acervo": "Acervo", "dataset": "Dataset"},
    "evidencia": {"incidentes_publicos": "incidentes públicos", "incidentes_reportados": "incidentes reportados ao órgão",
                  "resposta_incidentes": "resposta a incidentes", "telemetria": "telemetria do fornecedor",
                  "pesquisa_opiniao": "pesquisa de opinião", "avaliacao_maturidade": "avaliação de maturidade",
                  "misto": "misto", "curadoria": "curadoria", "metodo": "método"},
    "periodicidade": {"mensal": "mensal", "trimestral": "trimestral", "semestral": "semestral", "anual": "anual",
                      "bienal": "bienal", "continua": "contínua", "pontual": "pontual"},
    "relevancia_br": {"alta": "●●●", "media": "●●○", "baixa": "●○○"},
}
LEGIVEL_MAQUINA = {"json", "csv", "md", "api"}
PASSO = {"anual": 1, "bienal": 2}
MESES = ["", "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


def carregar():
    return json.loads(FONTES.read_text(encoding="utf-8"))


def series(d):
    return [f for f in d["fontes"] if "landscape" in f]


def validar(d):
    erros = []
    if "radar_referencia" not in d:
        erros.append("fontes.json sem radar_referencia")
    for f in series(d):
        m, i = f["landscape"], f["id"]
        for campo, voc in VOC.items():
            if m.get(campo) not in voc:
                erros.append(f"{i}: {campo} inválido ({m.get(campo)!r})")
        if not isinstance(m.get("formatos"), list) or not m["formatos"]:
            erros.append(f"{i}: formatos ausentes")
        mes = m.get("mes_tipico")
        if mes is not None and not (isinstance(mes, int) and 1 <= mes <= 12):
            erros.append(f"{i}: mes_tipico inválido")
        if m.get("substituida_por") and m["substituida_por"] not in {x["id"] for x in d["fontes"]}:
            erros.append(f"{i}: substituida_por aponta para id inexistente")
        if m.get("ano_edicao") is not None and not isinstance(m["ano_edicao"], int):
            erros.append(f"{i}: ano_edicao inválido")
        av = m.get("avaliacao")
        if av:
            if not (isinstance(av.get("nota"), int) and 0 <= av["nota"] <= av.get("maximo", 24)):
                erros.append(f"{i}: nota de avaliação inválida")
            if not (ROOT / av.get("arquivo", "")).exists():
                erros.append(f"{i}: arquivo de avaliação inexistente")
    return erros


def proxima(m, ref):
    """Retorna (ano, mes, devida) da próxima edição esperada, ou None."""
    passo = PASSO.get(m["periodicidade"])
    if m.get("substituida_por"):
        return None
    if not passo or not m.get("mes_tipico") or not m.get("ano_edicao"):
        return None
    ano, mes = m["ano_edicao"] + passo, m["mes_tipico"]
    return ano, mes, (ref.year, ref.month) >= (ano, mes)


def link(f):
    return f"[{f['titulo']}]({f['url']})"


def celula_rubrica(m):
    av = m.get("avaliacao")
    if not av:
        return "—"
    return f"[{av['nota']}/{av.get('maximo', 24)}](../{av['arquivo']})"


def tabela(fs):
    L = ["| Série | Publicador · região | Base de evidência | Periodicidade · edição | Formatos | BR | Rubrica |",
         "|---|---|---|---|---|---|---|"]
    ordem_br = ["alta", "media", "baixa"]
    for f in sorted(fs, key=lambda f: (ordem_br.index(f["landscape"]["relevancia_br"]), f["titulo"].casefold())):
        m = f["landscape"]
        acesso = "" if f["acesso"] == "aberto" else " 🔒"
        if m.get("substituida_por"):
            acesso += " ↳ *edição anterior*"
        ed = m.get("ultima_edicao") or "—"
        L.append(f"| {link(f)}{acesso}<br><sub>{m['tema']}</sub> | {f['autor']} · {VOC['regiao'][m['regiao']]} "
                 f"| {VOC['evidencia'][m['evidencia']]} | {VOC['periodicidade'][m['periodicidade']]} · {ed} "
                 f"| {', '.join(m['formatos'])} | {VOC['relevancia_br'][m['relevancia_br']]} | {celula_rubrica(m)} |")
    return L + [""]


def contagem(fs, campo):
    c = Counter(f["landscape"][campo] for f in fs)
    return " · ".join(f"{VOC[campo][k]} **{n}**" for k, n in c.most_common())


def render_md(d):
    fs = series(d)
    ref = date.fromisoformat(d["radar_referencia"])
    relatorios = [f for f in fs if f["landscape"]["escopo"] in ("horizontal", "setorial", "tematico", "metodo")]
    maquina = sum(1 for f in fs if LEGIVEL_MAQUINA & set(f["landscape"]["formatos"]))
    avaliadas = [f for f in fs if f["landscape"].get("avaliacao")]
    L = [
        "# Radar de Landscape · séries comparáveis de panorama e tendência",
        "",
        "[← Início](../README.md) · [Trilha](../trilhas/LANDSCAPE-E-TENDENCIAS.md) · [Rubrica ENISA](RUBRICA.md) · "
        "[Template do nosso landscape](../templates/LANDSCAPE.md) · [Planilha](radar.csv) · "
        "[Observatório de acervos](../biblioteca/LANDSCAPES-E-TENDENCIAS.md)",
        "",
        "> Gerado por `tools/landscape.py` a partir dos blocos `landscape` de `biblioteca/fontes.json`. "
        f"Data de referência do calendário: **{ref.isoformat()}**. Para a situação de hoje: `python3 tools/landscape.py --hoje`.",
        "",
        "## O que este radar faz que uma lista não faz",
        "",
        "| Uma *awesome list* diz… | O radar diz também… |",
        "|---|---|",
        "| que o relatório existe | **quem publica** (governo, fornecedor, academia) e com que **base de evidência** |",
        "| o ano | a **periodicidade**, o mês típico e **quando a próxima edição é esperada** |",
        "| o link | os **formatos** — e se há dados legíveis por máquina para medir, não só citar |",
        "| o tema | a **relevância para o Brasil** e onde estão as **lacunas** de cobertura |",
        "| — | uma **nota de qualidade metodológica** pela [rubrica ENISA](RUBRICA.md), com avaliação documentada |",
        "",
        "## Painel",
        "",
        f"- **{len(fs)} séries** · {len(relatorios)} relatórios/métodos · "
        f"{len(fs) - len(relatorios)} acervos e datasets · **{maquina}** com formato legível por máquina "
        f"(JSON, CSV, Markdown ou API) · **{len(avaliadas)}** avaliada(s) pela rubrica.",
        f"- **Publicador:** {contagem(fs, 'publicador_tipo')}",
        f"- **Base de evidência:** {contagem(fs, 'evidencia')}",
        f"- **Relevância BR:** {contagem(fs, 'relevancia_br').replace('●●●', 'alta').replace('●●○', 'média').replace('●○○', 'baixa')}",
        "",
        "### Matriz região × publicador",
        "",
    ]
    regs = [r for r in VOC["regiao"] if any(f["landscape"]["regiao"] == r for f in fs)]
    pubs = [p for p in VOC["publicador_tipo"] if any(f["landscape"]["publicador_tipo"] == p for f in fs)]
    L.append("| Região | " + " | ".join(VOC["publicador_tipo"][p] for p in pubs) + " |")
    L.append("|---|" + "---|" * len(pubs))
    for r in regs:
        cel = []
        for p in pubs:
            n = sum(1 for f in fs if f["landscape"]["regiao"] == r and f["landscape"]["publicador_tipo"] == p)
            cel.append(str(n) if n else "·")
        L.append(f"| {VOC['regiao'][r]} | " + " | ".join(cel) + " |")
    L.append("")

    blocos = [
        ("Relatórios horizontais · todas as ameaças", "horizontal"),
        ("Relatórios setoriais", "setorial"),
        ("Relatórios temáticos", "tematico"),
        ("Métodos", "metodo"),
        ("Acervos de relatórios", "acervo"),
        ("Datasets e rastreadores · medir em vez de citar", "dataset"),
    ]
    for titulo, esc in blocos:
        grupo = [f for f in fs if f["landscape"]["escopo"] == esc]
        if grupo:
            L += [f"## {titulo}", ""] + tabela(grupo)
    L.append("BR: ●●● dados ou foco no Brasil/LATAM · ●●○ comparação útil · ●○○ contexto externo. 🔒 = cadastro ou acesso restrito.")
    L.append("")

    L += ["## Calendário de vigilância", "",
          f"Próxima edição esperada de séries periódicas, calculada a partir da edição catalogada e do mês típico de publicação. "
          f"Referência: {ref.isoformat()}.", "",
          "| Série | Edição catalogada | Próxima esperada | Situação |", "|---|---|---|---|"]
    linhas = []
    for f in fs:
        nx = proxima(f["landscape"], ref)
        if nx:
            ano, mes, devida = nx
            sit = "⚠️ conferir se já saiu e atualizar o registro" if devida else "aguardar"
            linhas.append(((not devida, ano, mes), f"| {link(f)} | {f['landscape']['ultima_edicao']} | {MESES[mes]}/{ano} | {sit} |"))
    L += [x for _, x in sorted(linhas)] + [""]

    L += ["## Lacunas de cobertura", ""]
    gov_h = {f["landscape"]["regiao"] for f in fs if f["landscape"]["publicador_tipo"] == "governo"
             and f["landscape"]["escopo"] == "horizontal"}
    if "brasil" not in gov_h:
        L.append("- **Brasil:** nenhuma série governamental *horizontal e anual* equivalente ao ETL da ENISA neste radar. "
                 "Existem peças setoriais (BCB), estatísticas de notificação (NIC.br/CERT.br) e alertas (CTIR Gov). "
                 "**Oportunidade:** produzir um landscape BR com o [template](../templates/LANDSCAPE.md).")
    latam_dados = [f for f in fs if f["landscape"]["regiao"] in ("brasil", "latam") and LEGIVEL_MAQUINA & set(f["landscape"]["formatos"])]
    if not latam_dados:
        L.append("- **Dados abertos BR/LATAM:** nenhuma série regional com formato legível por máquina. Para medir tendências "
                 "locais, filtrar bases globais por país (ransomware.live, EuRepoC, CISSM) e declarar o viés de cobertura.")
    sem_aval = len(relatorios) - sum(1 for f in relatorios if f["landscape"].get("avaliacao"))
    L.append(f"- **Qualidade:** {sem_aval} relatórios ainda sem avaliação pela rubrica. Uma por semana fecha o radar em poucos meses.")
    L.append("")

    if avaliadas:
        L += ["## Avaliações pela rubrica ENISA", "", "| Série | Nota | Natureza | Data |", "|---|---|---|---|"]
        for f in avaliadas:
            av = f["landscape"]["avaliacao"]
            L.append(f"| {link(f)} | [{av['nota']}/{av.get('maximo', 24)}](../{av['arquivo']}) | {av.get('natureza', '')} | {av['data']} |")
        L.append("")

    L += ["## Como ampliar", "",
          "1. Acrescente a fonte em `biblioteca/fontes.json` com o bloco `landscape` (vocabulário em `tools/landscape.py`).",
          "2. Preencha `ano_edicao` e `mes_tipico` só com evidência da data de publicação.",
          "3. Rode `python3 tools/biblioteca.py && python3 tools/landscape.py` e faça o commit.",
          "4. Para avaliar: copie a [rubrica](RUBRICA.md) para `landscape/avaliacoes/<id>.md` e registre `avaliacao` no bloco.",
          ""]
    return "\n".join(L)


def render_csv(d):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    cols = ["publicador_tipo", "regiao", "escopo", "tema", "evidencia", "periodicidade", "ultima_edicao",
            "ano_edicao", "mes_tipico", "relevancia_br"]
    w.writerow(["id", "titulo", "autor", "url", "acesso", "status"] + cols + ["formatos", "idioma", "rubrica"])
    for f in sorted(series(d), key=lambda f: f["id"]):
        m = f["landscape"]
        av = m.get("avaliacao")
        w.writerow([f["id"], f["titulo"], f["autor"], f["url"], f["acesso"], f["status"]]
                   + ["" if m.get(c) is None else m[c] for c in cols]
                   + [";".join(m["formatos"]), ";".join(m.get("idioma", [])),
                      f"{av['nota']}/{av.get('maximo', 24)}" if av else ""])
    return buf.getvalue()


def main():
    d = carregar()
    erros = validar(d)
    for e in erros:
        print("ERRO:", e)
    if erros:
        return 1
    if sys.argv[1:2] == ["--hoje"]:
        hoje = date.today()
        print(f"Situação em {hoje.isoformat()}:")
        for f in series(d):
            nx = proxima(f["landscape"], hoje)
            if nx and nx[2]:
                print(f"  ⚠️  {f['titulo']} — edição {MESES[nx[1]]}/{nx[0]} provavelmente publicada")
        return 0
    saidas = {OUT_MD: render_md(d), OUT_CSV: render_csv(d)}
    if sys.argv[1:2] == ["--checar"]:
        falhas = [p for p, t in saidas.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        for p in falhas:
            print("ERRO: desatualizado —", p.relative_to(ROOT), "(rode: python3 tools/landscape.py)")
        if not falhas:
            print(f"OK: radar com {len(series(d))} séries em dia")
        return bool(falhas)
    OUT_MD.parent.mkdir(exist_ok=True)
    for p, t in saidas.items():
        p.write_text(t, encoding="utf-8")
    print(f"OK: {len(series(d))} séries → landscape/README.md + radar.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
