#!/usr/bin/env python3
"""
catalogo.py — gera CATALOGO-REPOS.md a partir de repos.json (Python stdlib).

Uso:
    python3 tools/catalogo.py                       # regenera o catálogo
    python3 tools/catalogo.py --checar              # valida (CI): JSON, pastas e catálogo em dia
    python3 tools/catalogo.py --verificar <usuario> # lista repos públicos fora do repos.json

A verificação usa a API pública do GitHub (sem token, 60 req/h).
"""
import json
import sys
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "repos.json"
SAIDA = RAIZ / "CATALOGO-REPOS.md"
PASTA_DISC = RAIZ / "disciplinas"

# id -> (nome curto, pasta, peso)
DISCIPLINAS = {
    "00": ("Fundamentos", "00-fundamentos", "★★"),
    "01": ("OSINT", "01-osint", "★★★"),
    "02": ("CTI", "02-cti", "★★★"),
    "03": ("Malware/RE", "03-malware-engenharia-reversa", "★★★"),
    "04": ("DFIR", "04-dfir", "★★"),
    "05": ("SOCMINT", "05-socmint", "★★"),
    "06": ("HUMINT", "06-humint", "★"),
    "07": ("Psicologia", "07-psicologia-investigativa", "★★"),
    "08": ("GEOINT/IMINT", "08-geoint-imint", "★"),
    "09": ("SIGINT", "09-sigint", "★"),
    "10": ("MASINT", "10-masint", "★"),
    "11": ("TECHINT", "11-techint", "★"),
    "12": ("CYBINT", "12-cybint", "★★"),
    "13": ("FININT", "13-finint", "★"),
    "14": ("Contrainteligência", "14-contrainteligencia", "★"),
    "15": ("Outras INTs", "15-outras-ints", "★"),
    "16": ("Dados", "16-engenharia-de-dados", "★★"),
    "17": ("Arquitetura", "17-arquitetura-de-sistemas", "★★"),
    "18": ("IA", "18-ia-aplicada", "★★"),
}


def carregar():
    with open(DADOS, encoding="utf-8") as f:
        return json.load(f)


def link(dados, r):
    dono = r.get("dono", dados["owner"])
    rotulo = r["nome"] if dono == dados["owner"] else f"{dono}/{r['nome']}"
    return f"[{rotulo}](https://github.com/{dono}/{r['nome']})"


def renderizar(dados):
    repos = sorted(dados["repos"], key=lambda r: (r["papel"], r["nome"].lower()))
    L = [
        "# Catálogo dos meus repositórios",
        "",
        "> Gerado por `tools/catalogo.py` a partir de `repos.json`. Edite o JSON, não este arquivo.",
        f"> Atualizado em {dados['atualizado']} · {len(repos)} repositórios · 🌐 público · 🔒 privado",
        "",
        "## Por papel",
        "",
    ]
    for papel, desc in dados["papeis"].items():
        grupo = [r for r in repos if r["papel"] == papel]
        if not grupo:
            continue
        L += [f"### {papel.capitalize()} — {desc}", "",
              "| Repo | Disciplinas | Visib. | Descrição |", "|---|---|---|---|"]
        for r in grupo:
            discs = ", ".join(DISCIPLINAS[d][0] for d in r["disciplinas"]) or "—"
            vis = "🔒" if r["visibilidade"] == "privado" else "🌐"
            L.append(f"| {link(dados, r)} | {discs} | {vis} | {r['descricao']} |")
        L.append("")

    L += ["## Por disciplina", "", "| Disciplina | Peso | Repos |", "|---|---|---|"]
    for did, (nome, pasta, peso) in DISCIPLINAS.items():
        grupo = [r for r in repos if did in r["disciplinas"]]
        itens = " · ".join(f"{link(dados, r)} *({r['papel']})*" for r in grupo) or "_lacuna_"
        L.append(f"| [{did} · {nome}](disciplinas/{pasta}/) | {peso} | {itens} |")
    L.append("")

    lacunas = [f"{did} {n}" for did, (n, _, _) in DISCIPLINAS.items()
               if not any(did in r["disciplinas"] for r in repos)]
    if lacunas:
        L += ["## Lacunas — disciplinas sem repo próprio", "", "- " + "\n- ".join(lacunas), ""]
    return "\n".join(L)


def validar(dados):
    erros = []
    nomes = set()
    for r in dados["repos"]:
        chave = (r.get("dono", dados["owner"]), r["nome"].lower())
        if chave in nomes:
            erros.append(f"repo duplicado: {r['nome']}")
        nomes.add(chave)
        if r["papel"] not in dados["papeis"]:
            erros.append(f"{r['nome']}: papel desconhecido '{r['papel']}'")
        for d in r["disciplinas"]:
            if d not in DISCIPLINAS:
                erros.append(f"{r['nome']}: disciplina inexistente '{d}'")
    for did, (_, pasta, _) in DISCIPLINAS.items():
        if not (PASTA_DISC / pasta / "README.md").exists():
            erros.append(f"falta disciplinas/{pasta}/README.md")
    return erros


def verificar(dados, usuario):
    conhecidos = {r["nome"].lower() for r in dados["repos"] if r.get("dono", dados["owner"]) == usuario}
    novos, pagina = [], 1
    while True:
        url = f"https://api.github.com/users/{usuario}/repos?per_page=100&page={pagina}"
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                                   "User-Agent": "INTStudy-catalogo"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            lote = json.load(resp)
        if not lote:
            break
        novos += [(r["name"], r.get("fork"), r.get("description") or "")
                  for r in lote if r["name"].lower() not in conhecidos]
        pagina += 1
    if not novos:
        print("Todos os repos públicos já estão em repos.json.")
        return
    print(f"{len(novos)} repo(s) fora do repos.json:")
    for nome, fork, desc in novos:
        print(f"  - {nome}{' (fork)' if fork else ''}: {desc}")


def main():
    dados = carregar()
    args = sys.argv[1:]
    if args[:1] == ["--verificar"] and len(args) == 2:
        verificar(dados, args[1])
        return 0
    erros = validar(dados)
    for e in erros:
        print("ERRO:", e)
    if erros:
        return 1
    texto = renderizar(dados)
    if args[:1] == ["--checar"]:
        atual = SAIDA.read_text(encoding="utf-8") if SAIDA.exists() else ""
        if atual != texto:
            print("ERRO: CATALOGO-REPOS.md desatualizado — rode: python3 tools/catalogo.py")
            return 1
        print("ok: catálogo e estrutura válidos")
        return 0
    SAIDA.write_text(texto, encoding="utf-8")
    print(f"ok: {SAIDA.name} com {len(dados['repos'])} repos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
