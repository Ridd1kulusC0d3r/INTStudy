#!/usr/bin/env python3
"""Gera índices reprodutíveis a partir de fontes.json; não faz requisições de rede."""
import json
import sys
from pathlib import Path
from catalogo import DISCIPLINAS
ROOT = Path(__file__).resolve().parent.parent
LEVELS = {'D':0,'C':1,'B':2,'A':3,'S':4}
ACCESS = {'aberto':'Aberto','pago':'Comercial','restrito':'Restrito / não confirmado'}
def carregar():
    return json.loads((ROOT/'biblioteca/fontes.json').read_text())
def validar(d):
    errors=[]; ids=set()
    for f in d['fontes']:
        required={'id','titulo','autor','url','tipo','acesso','disciplinas','uso','nivel','status','nota'}
        if required-set(f):
            errors.append(f"Campos ausentes: {f.get('id')}");continue
        if f['id'] in ids: errors.append('ID duplicado: '+f['id'])
        ids.add(f['id'])
        for field,values in [('tipo',d['tipos']),('uso',d['usos']),('status',d['status']),('acesso',ACCESS),('nivel',LEVELS)]:
            if f[field] not in values: errors.append(f"{f['id']}: {field} inválido")
        if any(x not in DISCIPLINAS for x in f['disciplinas']): errors.append(f"{f['id']}: disciplina inválida")
        if f['status']!='nao_confirmado' and not str(f['url']).startswith('https://'): errors.append(f"{f['id']}: URL inválida")
        if f.get('ano') is not None and not isinstance(f['ano'],int): errors.append(f"{f['id']}: ano inválido")
    return errors

def ordenar(fs): return sorted(fs,key=lambda f:(LEVELS[f['nivel']],f['titulo'].casefold()))
def table(fs):
    lines=['| Material / instituição | Ano · formato | Nível / uso | Contexto e objetivo |','|---|---|---|---|']
    for f in ordenar(fs):
        year=f.get('ano') or 's/d'
        title=f"[{f['titulo']}]({f['url']})" if f.get('url') else f['titulo']
        state={'verificado':'Conferência anterior','conhecido':'Referência identificada','a_verificar':'A verificar','nao_confirmado':'Não confirmado'}[f['status']]
        note=f['nota']+f" **{state}.**"
        lines.append(f"| **{title}** — {f['autor']} | {year} · {f['tipo']} | {f['nivel']} / {f['uso']} | {note.replace('|',' / ')} |")
    return lines+['']

def saidas(d):
    fs=d['fontes']; openfs=[f for f in fs if f['acesso']=='aberto' and f['status']!='nao_confirmado']; archive=[f for f in fs if f not in openfs]
    L=['# Biblioteca aberta · escolha pela pergunta','', '[← Início](../README.md) · [Trilha CTI](../trilhas/CTI-DO-ZERO-AO-BRIEFING.md) · [Procedência](PROCEDENCIA.md) · [Auditoria de links](VERIFICACAO-LINKS.md)','',
       f"**{len(openfs)} referências classificadas como abertas · {len(archive)} registros comerciais, restritos ou não confirmados no [arquivo separado](REFERENCIAS-RESTRITAS.md).**",'',
       '> Índice gerado por `tools/biblioteca.py`. Edite `biblioteca/fontes.json`. Acesso é uma classificação editorial; bloqueios e resultados técnicos estão na auditoria. Nenhum link significa licença de redistribuição.', '',
       '**Como ler:** s/d = ano não confirmado ou recurso contínuo. D inicial · C fundamentos · B aplicação · A avançado · S contribuição. Histórico = anterior a 2022, apenas um filtro editorial; não significa inválido.', '',
       '| Preciso… | Percurso |','|---|---|','| Entender e produzir CTI | [Missões CTI](../trilhas/CTI-DO-ZERO-AO-BRIEFING.md) |','| Entender métodos MITRE | [MITRE em contexto](../trilhas/MITRE-EM-CONTEXTO.md) |','| Encontrar todas as referências deste chat | [Registro e inventário](../docs/CURADORIA-2026-10-16.md) |','',
       '## Navegar por disciplina','']
    for did,(name,folder,_) in DISCIPLINAS.items():
        n=sum(did in f['disciplinas'] for f in openfs)
        if n:L.append(f'- [{did} · {name}](../disciplinas/{folder}/BIBLIOTECA.md) — {n} referências abertas')
    L+=['','## Formação e consulta','']
    for label,pred in [('Publicações de 2022 em diante',lambda f:isinstance(f.get('ano'),int) and f['ano']>=2022),('Documentação contínua ou ano não confirmado',lambda f:not f.get('ano')),('Fundamentos históricos · anteriores a 2022',lambda f:isinstance(f.get('ano'),int) and f['ano']<2022)]:
        group=[f for f in openfs if pred(f)]
        L += [f'### {label}','']+table(group)
    out={ROOT/'biblioteca/README.md':'\n'.join(L)}
    A=['# Arquivo de referências comerciais, restritas e não confirmadas','', '[← Biblioteca aberta](README.md)','',
       'Preservamos o histórico da pesquisa sem apresentar estes materiais como requisitos gratuitos. Links de editoras confirmam a existência, não o acesso ao livro completo. Não hospedamos cópias de terceiros.','']
    for access in ['pago','restrito','aberto']:
        group=[f for f in archive if f['acesso']==access]
        if group:A+=['## '+ACCESS[access],'']+table(group)
    out[ROOT/'biblioteca/REFERENCIAS-RESTRITAS.md']='\n'.join(A)
    for did,(name,folder,_) in DISCIPLINAS.items():
        group=[f for f in openfs if did in f['disciplinas']]
        L=[f'# Biblioteca aberta · {name}','', '[← Disciplina](README.md) · [Catálogo completo](../../biblioteca/README.md) · [Trilhas](../../COMECE-AQUI.md)','',
           '> Gerado de `biblioteca/fontes.json`. Acesso e qualidade são dimensões diferentes; consulte a procedência e a auditoria no índice geral.','']
        for use in d['usos']:
            g=[f for f in group if f['uso']==use]
            if g:L+=['## '+use.capitalize(),'']+table(g)
        if not group:L+=['Ainda não há referências abertas catalogadas para esta disciplina. Consulte as fontes do README local.','']
        out[ROOT/'disciplinas'/folder/'BIBLIOTECA.md']='\n'.join(L)
    return out

def main():
    d=carregar(); errors=validar(d)
    if errors: print('\n'.join(errors));return 1
    outputs=saidas(d)
    if '--checar' in sys.argv:
        bad=[str(p.relative_to(ROOT)) for p,s in outputs.items() if not p.exists() or p.read_text()!=s]
        if bad:print('Índices desatualizados:\n'+'\n'.join(bad));return 1
        print('OK: schema e índices reprodutíveis');return 0
    for p,s in outputs.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
    print(f'OK: {len(d["fontes"])} registros, {len(outputs)} índices')
    return 0
if __name__=='__main__':sys.exit(main())
