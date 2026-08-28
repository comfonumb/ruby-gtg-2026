from pathlib import Path
import shutil

ROOT = Path('.')
COMMITTEE = ROOT / 'committee'
COMMITTEE.mkdir(exist_ok=True)

# Normalize newly uploaded committee photos that were placed in the repository root.
for name in ['Hema_S_Nair.jpg', 'Jose_Manual.jpg', 'Nimmy.jpg']:
    src = ROOT / name
    dst = COMMITTEE / name
    if src.exists() and src.stat().st_size > 10000 and not dst.exists():
        shutil.copy2(src, dst)

# Sindhu's previous upload was a tiny invalid placeholder. Accept it only when a real image is present.
for src_name in ['Sindhu_Nair_P. jpg', 'Sindhu_Nair_P.jpg']:
    src = ROOT / src_name
    dst = COMMITTEE / 'Sindhu_Nair_P.jpg'
    if src.exists() and src.stat().st_size > 10000:
        shutil.copy2(src, dst)
        break

index = ROOT / 'index.html'
s = index.read_text(encoding='utf-8')

cards = {
    'Hema S Nair': '<div class="person"><img class="portrait" src="committee/Hema_S_Nair.jpg" alt="Hema S Nair"><b>Hema S Nair</b></div>',
    'Jose Manual': '<div class="person"><img class="portrait" src="committee/Jose_Manual.jpg" alt="Jose Manual"><b>Jose Manual</b></div>',
    'Nimmy': '<div class="person"><img class="portrait" src="committee/Nimmy.jpg" alt="Nimmy"><b>Nimmy</b></div>',
    'Sindhu Nair P': '<div class="person"><img class="portrait" src="committee/Sindhu_Nair_P.jpg" alt="Sindhu Nair P"><b>Sindhu Nair P</b></div>',
}

def ensure_card(s, name, before_name):
    if f'alt="{name}"' in s:
        return s
    marker = f'<div class="person"><img class="portrait" src="committee/{before_name}.jpg" alt="{before_name}"><b>{before_name}</b></div>'
    return s.replace(marker, cards[name] + marker, 1)

# Maintain alphabetical order.
s = ensure_card(s, 'Hema S Nair', 'Jyothish')
s = ensure_card(s, 'Jose Manual', 'Jyothish')
s = ensure_card(s, 'Nimmy', 'Paul')
if (COMMITTEE / 'Sindhu_Nair_P.jpg').exists():
    s = ensure_card(s, 'Sindhu Nair P', 'Sofiya')

index.write_text(s, encoding='utf-8')
