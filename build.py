"""
Builds the Class Wall website into the _site/ folder.

You don't need to run this yourself. GitHub runs it automatically:
  - on every pull request (to check your card), and
  - every time something is merged into main (to update the live site).

If you're curious, you can run it locally with:  python build.py
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
MEMBERS = ROOT / "members"
OUT = ROOT / "_site"


def clean_card(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)                    # drop comments
    html = re.sub(r"<link[^>]*>", "", html, flags=re.I)                    # drop preview stylesheet
    html = re.sub(r"<script.*?</script>", "", html, flags=re.S | re.I)     # no scripts on the wall
    html = re.sub(r"\son\w+\s*=\s*(\"[^\"]*\"|'[^']*')", "", html, flags=re.I)
    return html.strip()


def main() -> int:
    problems = []
    cards = []

    for path in sorted(MEMBERS.glob("*"), key=lambda p: p.name.lower()):
        if path.name.startswith("_") or path.name.startswith("."):
            continue  # skip the template and hidden files
        if path.suffix != ".html":
            problems.append(f"{path.name}: card files must end in .html")
            continue
        card = clean_card(path)
        if 'class="card"' not in card:
            problems.append(f'{path.name}: could not find <article class="card"> — did you copy the template?')
            continue
        if "Juan Dela Cruz" in card:
            problems.append(f"{path.name}: still has the template name 'Juan Dela Cruz' — put your own name!")
            continue
        cards.append(card)

    if problems:
        print("Some cards need fixing:\n")
        for p in problems:
            print("  -", p)
        return 1

    page = (ROOT / "index.html").read_text(encoding="utf-8")
    body = "\n\n".join(cards) if cards else (
        '<div class="empty">No cards yet. Be the first one on the wall!</div>'
    )
    page = page.replace("<!-- CARDS -->", body).replace("<!-- COUNT -->", str(len(cards)))

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / "index.html").write_text(page, encoding="utf-8")
    shutil.copy(ROOT / "style.css", OUT / "style.css")

    print(f"Built the wall with {len(cards)} card(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
