# THE TUESDAY GLOBE — Tuesday 24 November 2026 in one image

A one-page newspaper front page that sums up the world news of
**Tuesday 24 November 2026** for the make.fun contest
`news-image-20261124`.

- **Lead:** NATO hardens its eastern border — Rutte and Merz pledge
  stronger external-border defence in Berlin after Russian missiles
  fell in Poland, a fresh Russian drone crosses Polish airspace
  overnight, and an AWACS heads east.
- **Second lead:** Jensen Huang returns to Nvidia eleven days after
  resigning, and Wall Street roars back (Nasdaq +6.5%).
- **Third lead:** Iran says three tankers struck naval mines in the
  Strait of Hormuz overnight, as sanctions widen and Qatar mediates.
- **The day in 36 briefs:** numbered one-paragraph stories across
  six continents — Berlin to Kyiv, Hormuz to Iowa, Cikande to
  Mexico City — plus a dotted world map whose red pins carry the
  brief numbers, and a sources footer.

## Layout of this repository

- `entry.png` — the finished page, 1024 x 1024, drawn Tuesday
  morning JST as an early edition.
- `main.py` — the entry program. It validates the page (PNG chunk
  walk with CRC checks, size and dimension limits) and ships it to
  `$MAKEFUN_OUTPUT_DIR` (default `/output`) atomically, verifying
  the shipped copy's SHA-256. Standard library only, deterministic.
- `SOURCES.md` — where each story on the page was reported.
- `LICENSE` — MIT.

Run it with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
