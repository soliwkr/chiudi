from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
required = [
    root / "public/index.html",
    root / "public/desk.html",
    root / "public/assets/styles.css",
    root / "public/assets/site.js",
    root / "public/assets/desk.js",
    root / "wrangler.jsonc",
    root / "docs/PRODUCT.md",
    root / "docs/STATUS.md",
    root / "docs/NEXT.md",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    raise SystemExit(f"Missing required files: {', '.join(missing)}")

public_text = "\n".join(p.read_text(encoding="utf-8") for p in (root / "public").rglob("*.html"))
for forbidden in ["€490", "5% del fatturato", "OFFERTA PILOT", "MVP ·"]:
    if forbidden in public_text:
        raise SystemExit(f"Internal validation copy leaked into public HTML: {forbidden}")

for html in (root / "public").glob("*.html"):
    text = html.read_text(encoding="utf-8")
    if "<title>" not in text or "charset=" not in text:
        raise SystemExit(f"Basic HTML metadata missing in {html.name}")

csv_header = (root / "public/sample-leads.csv").read_text(encoding="utf-8").splitlines()[0]
expected = ["nome","lavoro","valore","data_preventivo","prossimo_followup","contatto","base_di_contatto","stato","note"]
if csv_header.split(";") != expected:
    raise SystemExit("sample-leads.csv header does not match documented schema")

json.loads((root / "wrangler.jsonc").read_text(encoding="utf-8"))
print("CHIUDI static checks: OK")
