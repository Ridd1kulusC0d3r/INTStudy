#!/usr/bin/env python3
"""
biblioteca.py — gera a biblioteca a partir de biblioteca/fontes.json (Python stdlib).

Saídas:
    biblioteca/README.md                  índice geral (por status, uso e disciplina)
    disciplinas/<pasta>/BIBLIOTECA.md     recorte por disciplina

Uso:
    python3 tools/biblioteca.py           # regenera tudo
    python3 tools/biblioteca.py --checar  # valida (CI): JSON coerente e arquivos em dia
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalogo import DISCIPLINAS  # noqa: E402  (mesma fonte de verdade das disciplinas)

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "biblioteca" / "fontes.json"
INDICE = RAIZ / "biblioteca" / "README.md"

SELO = {"verificado": "✅", "conhecido": "📘", "a_verificar": "⚠️", "nao_confirmado": "❌"}
ACESSO = {"aberto": "🆓", "pago": "💲"}
ORDEM_NIVEL = {"D": 0, "C": 1, "B": 2, "A": 3, "S": 4}


def carregar():
    with open(DADOS, encoding="utf-8") as f:
        return json.load(f)


def titulo_md(f):
    t = f"**{f['titulo']}**"
    return f"[{t}]({f['url']})" if f.get("url") else t


def linha(f, com_disc=True):
    cols = [
        SELO[f["status"]],
        titulo_md(f),
        f["autor"],
        f["tipo"],
        ACESSO[f["acesso"]],
        f["nivel"],
        f["uso"],
    ]
    if com_disc:
        cols.append(", ".join(DISCIPLINAS[d][0] for d in f["disciplinas"]))
    cols.append(f["nota"])
    return "| " + " | ".join(str(c) for c in cols) + " |"


def cabecalho(com_disc=True):
    nomes = ["", "Título", "Autor", "Tipo", "Acesso", "Nível", "Uso"]
    if com_disc:
        nomes.append("Disciplinas")
    nomes.append("Nota")
    return ["| " + " | ".join(nomes) + " |", "|" + "---|" * len(nomes)]


def legenda(dados):
    itens = [f"{SELO[k]} {v}" for k, v in dados["status"].items()]
    return ["**Legenda:** " + " · ".join(itens) + " · 🆓 aberto · 💲 pago", ""]


def ordenar(fontes):
    peso_status = {"verificado": 0, "conhecido": 1, "a_verificar": 2, "nao_confirmado": 3}
    return sorted(fontes, key=lambda f: (peso_status[f["status"]], ORDEM_NIVEL[f["nivel"]], f["titulo"].lower()))


def render_indice(dados):
    fontes = ordenar(dados["fontes"])
    validas = [f for f in fontes if f["status"] != "nao_confirmado"]
    descartes = [f for f in fontes if f["status"] == "nao_confirmado"]
    L = [
        "# Biblioteca",
        "",
        "> Gerado por `tools/biblioteca.py` a partir de `biblioteca/fontes.json`. Edite o JSON, não este arquivo.",
        f"> Atualizado em {dados['atualizado']} · {len(validas)} fontes utilizáveis · {len(descartes)} descartadas.",
        "",
        "Fluxo de uso operacional: [FLUXO-OPERACIONAL.md](FLUXO-OPERACIONAL.md) · Origem e verificação: [PROCEDENCIA.md](PROCEDENCIA.md)",
        "",
    ] + legenda(dados)

    for uso, desc in dados["usos"].items():
        grupo = [f for f in validas if f["uso"] == uso]
        if not grupo:
            continue
        L += [f"## {uso.capitalize()} — {desc}", ""] + cabecalho() + [linha(f) for f in grupo] + [""]

    L += ["## Por disciplina", ""]
    for did, (nome, pasta, peso) in DISCIPLINAS.items():
        n = sum(1 for f in validas if did in f["disciplinas"])
        if n:
            L.append(f"- [{did} · {nome}](../disciplinas/{pasta}/BIBLIOTECA.md) — {n} fonte(s)")
    L.append("")

    if descartes:
        L += ["## ❌ Não confirmadas — não citar", "",
              "Mantidas aqui para registro: vieram das listas de origem, mas não foram encontradas.", ""]
        L += cabecalho() + [linha(f) for f in descartes] + [""]
    return "\n".join(L)


def render_disciplina(dados, did):
    nome, pasta, peso = DISCIPLINAS[did]
    grupo = [f for f in ordenar(dados["fontes"]) if did in f["disciplinas"] and f["status"] != "nao_confirmado"]
    if not grupo:
        return None
    L = [
        f"# Biblioteca — {did} · {nome}",
        "",
        "> Recorte gerado de [`biblioteca/fontes.json`](../../biblioteca/fontes.json). "
        "Índice geral: [biblioteca/](../../biblioteca/README.md).",
        "",
    ] + legenda(dados)
    for uso, desc in dados["usos"].items():
        sub = [f for f in grupo if f["uso"] == uso]
        if sub:
            L += [f"## {uso.capitalize()}", ""] + cabecalho(False) + [linha(f, False) for f in sub] + [""]
    return "\n".join(L)


def validar(dados):
    erros, ids = [], set()
    for f in dados["fontes"]:
        if f["id"] in ids:
            erros.append(f"id duplicado: {f['id']}")
        ids.add(f["id"])
        if f["status"] not in dados["status"]:
            erros.append(f"{f['id']}: status inválido")
        if f["tipo"] not in dados["tipos"]:
            erros.append(f"{f['id']}: tipo inválido")
        if f["uso"] not in dados["usos"]:
            erros.append(f"{f['id']}: uso inválido")
        if f["nivel"] not in ORDEM_NIVEL:
            erros.append(f"{f['id']}: nível inválido")
        if f["acesso"] not in ACESSO:
            erros.append(f"{f['id']}: acesso inválido")
        for d in f["disciplinas"]:
            if d not in DISCIPLINAS:
                erros.append(f"{f['id']}: disciplina inexistente '{d}'")
        if f["status"] != "nao_confirmado" and not f.get("url"):
            erros.append(f"{f['id']}: fonte utilizável sem url")
    return erros


def saidas(dados):
    arquivos = {INDICE: render_indice(dados)}
    for did, (_, pasta, _) in DISCIPLINAS.items():
        destino = RAIZ / "disciplinas" / pasta / "BIBLIOTECA.md"
        texto = render_disciplina(dados, did)
        arquivos[destino] = texto  # None = o arquivo não deve existir
    return arquivos


def main():
    dados = carregar()
    erros = validar(dados)
    for e in erros:
        print("ERRO:", e)
    if erros:
        return 1
    arquivos = saidas(dados)
    if sys.argv[1:2] == ["--checar"]:
        falhas = []
        for p, texto in arquivos.items():
            atual = p.read_text(encoding="utf-8") if p.exists() else None
            if atual != texto:
                falhas.append(str(p.relative_to(RAIZ)))
        if falhas:
            print("ERRO: biblioteca desatualizada — rode: python3 tools/biblioteca.py")
            for f in falhas:
                print("  -", f)
            return 1
        print("ok: biblioteca válida e em dia")
        return 0
    n = 0
    for p, texto in arquivos.items():
        if texto is None:
            if p.exists():
                p.unlink()
            continue
        p.write_text(texto, encoding="utf-8")
        n += 1
    print(f"ok: {len(dados['fontes'])} fontes → {n} arquivos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
