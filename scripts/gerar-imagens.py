from pathlib import Path
import json, subprocess
b=Path(__file__).resolve().parent.parent
for i,scene in enumerate(json.loads((b/'context/cenas.json').read_text())):
 p=b/'assets/img'/('trilha.webp' if i==0 else f'aula-{i}.webp')
 if p.exists(): continue
 subprocess.run(['python3','/home/nmaldaner/.claude/skills/formato-curso-v6/scripts/gerar-cena.py',str(p),scene,'--gerador','flux','--seed',str(410+i)],check=True)
