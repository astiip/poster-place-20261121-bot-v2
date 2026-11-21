# Solmara — The Poster for a Place That Isn't There

[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/astiip/poster-place-20261121-bot-v2/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/astiip/poster-place-20261121-bot-v2/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

A travel poster for a place that does not exist: **Solmara**, a bright
coastal town where whitewashed houses with terracotta roofs cascade down
a hillside to a turquoise bay. A white lighthouse stands on a rocky
point, colorful fishing boats float on calm water, and pink
bougainvillea spills between the houses — the promise is a stay by the
sea: sun, salt air, and the light coming home. Solmara is a bright
coastal town where the whole day is arranged around the light: white
walls to catch the morning sun, and a lighthouse that brings it home
at dusk.

The name is set in large white serif across the clear blue sky, with the
tagline "WHERE THE LIGHT COMES HOME" over the sea below.

## Files

- `main.ts` — the entry program (Node 22). Copies `entry.png` to the
  output directory, byte for byte. No network. Deterministic: the same
  poster, byte for byte, on every run.
- `entry.png` — the poster, 1024×1024, a real PNG under 1 MiB.
- `scene.png` — the original AI-generated painting of the coastal town
  (made for this entry, no text in it).
- `render.py` — composes the poster: the scene cropped square with the
  name, tagline and gold rule set in DejaVu Serif / DejaVu Sans, and
  writes `entry.png` with its size and sha256.

## Run

`node main.ts` writes `out/entry.png`, byte-identical to `entry.png`.
