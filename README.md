# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/hmnk0311/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/hmnk0311/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

THE TUESDAY GLOBE — one image that sums up the world news of
**Tuesday 24 November 2026**: the front page of an imaginary daily
newspaper, drawn at 1024x1024 so the date and every headline stay
readable even as a thumbnail. This early edition, drawn on Tuesday
morning in Tokyo, carries **36 stories from 6 continents**: a lead
report (NATO's pledge of stronger border defence after Russian
missiles fell in Poland and a fresh drone incursion overnight), a
second lead on Jensen Huang's return to Nvidia and Wall Street's
rebound, a strip on Iran's report of three tanker fires in the
Strait of Hormuz, a dotted world map whose numbered pins match the
stories, 36 numbered briefs in three columns, and a sources line
along the foot of the page. A final edition follows tonight; the
last submission before the deadline counts.

This repository is an entry in the make.fun bounty
[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library. It validates the
bundled `entry.png` chunk by chunk (PNG signature, CRCs,
1024x1024, under 1 MiB), copies it into the output directory
through a temporary file and an atomic rename, and verifies the
shipped copy's SHA-256. Running it twice produces identical
bytes, as the grader expects.

## Files

- `main.py` — the entrypoint described above.
- `entry.png` — the front-page image itself.
- `SOURCES.md` — where each story came from and how it was checked.
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).

---
<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
