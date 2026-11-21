// the-poster-for-a-place-that-i-2-20261121-0539 — "Solmara"
// A travel poster for a place that does not exist: Solmara, a bright
// coastal town where whitewashed houses with terracotta roofs cascade
// down a hillside to a turquoise bay — a white lighthouse on a rocky
// point, colorful fishing boats on calm water, pink bougainvillea and
// cypress trees in warm Mediterranean light. The promise is a stay by
// the sea: sun, salt air, and the light coming home. The name is set in
// large white serif across the clear blue sky, with the tagline
// "WHERE THE LIGHT COMES HOME" over the sea below. The scene is an
// original AI-generated painting (scene.png, made for this entry);
// the type is set by render.py and rendered to entry.png.
//
// Output contract: this program copies entry.png to the output directory,
// byte for byte. The poster itself is the entry artifact — the program
// never re-renders it, never fetches anything, and never writes a single
// different byte. Every run therefore produces the exact file the
// competition harness expects: out/entry.png identical to entry.png,
// so the submitted poster and the program's output can never drift apart.
// The file name lives in one constant (ENTRY_FILE) so the source and the
// destination always name the same file.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const ENTRY_FILE = "entry.png";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, ENTRY_FILE), join(outDir, ENTRY_FILE));
