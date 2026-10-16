#!/usr/bin/env python3
"""Valida destinos locais em Markdown e imagens; ignora URLs externas e âncoras."""
import re
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
errors=[]; count=0
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:continue
    text=p.read_text()
    targets=re.findall(r'\]\(([^)]+)\)',text)+re.findall(r'(?:src|href)="([^"]+)"',text)
    for target in targets:
        if re.match(r'^[a-z]+:',target) or target.startswith('#'):continue
        target=target.split('#')[0].split('?')[0]
        if not target:continue
        count+=1
        if not (p.parent/target).exists():errors.append(f'{p.relative_to(ROOT)} → {target}')
print('\n'.join(errors) if errors else f'OK: {count} destinos locais existentes')
sys.exit(bool(errors))
