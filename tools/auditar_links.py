#!/usr/bin/env python3
"""Checagem HTTP limitada; 200 não prova acesso integral ou qualidade."""
import concurrent.futures
import datetime
import json
import urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def check(url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'INTStudy-link-check/1.0'})
        with urllib.request.urlopen(req,timeout=12) as response:
            response.read(1024)
            return {'url':url,'http':response.status,'final':response.url,'tipo':response.headers.get('Content-Type',''),'resultado':'resposta_recebida'}
    except Exception as e:
        return {'url':url,'http':getattr(e,'code',None),'resultado':'nao_confirmado_neste_ambiente','erro':str(e)[:180]}

def main():
    data=json.loads((ROOT/'biblioteca/fontes.json').read_text())
    urls=sorted({f['url'] for f in data['fontes'] if f.get('url')})
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool: results=list(pool.map(check,urls))
    day=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (ROOT/'biblioteca/auditoria-links.json').write_text(json.dumps({'executado_em_utc':day,'metodo':'GET com leitura limitada a 1024 bytes, timeout 12s; não valida texto integral','resultados':results},ensure_ascii=False,indent=2)+'\n')
    lines=['# Verificação técnica de links','', '[← Biblioteca](README.md)','',f'Execução UTC: {day}','',
           '**Limite:** checagem de transporte, não auditoria de conteúdo. HTTP 200 pode ser uma página intermediária. HTTP 403/429, timeout ou erro de proxy não provam que a fonte deixou de existir. Datas editoriais não são inferidas desta checagem.','',
           '| URL | HTTP | Resultado / destino |','|---|---|---|']
    for x in results:
        detail=x.get('final',x.get('erro','')).replace('|',' / ').replace('\n',' ')
        lines.append(f"| <{x['url']}> | {x.get('http') or '—'} | {detail} |")
    (ROOT/'biblioteca/VERIFICACAO-LINKS.md').write_text('\n'.join(lines)+'\n')
    print(f"{len(results)} URLs; {sum(x['resultado']=='resposta_recebida' for x in results)} respostas recebidas; demais requerem revisão")
if __name__=='__main__':main()
