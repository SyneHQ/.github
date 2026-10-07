# GitHub profile artwork

The banners use SyneHQ's approved S02 / Pinched S identity. The frozen masks preserve the actual symbol and wordmark. Do not retype the wordmark or redraw the dot geometry.

| Color | Value |
| --- | --- |
| Wine | `#26191D` |
| Ivory | `#FFF7F4` |
| Blush | `#FFB8B0` |
| Coral | `#FF6666` |

The wordmark's full ink height is 78% of the symbol's height. The gap is 26% of the symbol's height. Both are centered by their full ink bounds, including descenders. Keep at least a quarter-symbol of clear space around a lockup.

The pixel pattern is composited at 75% opacity on wine at the bottom right. On the wide banner, its rightmost 300 pixels fall outside the canvas to keep the text clear. Its native 1514 × 295 pixel grid is cropped, never stretched or resampled. Headline type is Newsreader; supporting text is Manrope. The unmodified fonts are bundled with their SIL Open Font Licenses.

## Rebuild

Use Python 3 and Pillow:

```sh
python3 -m venv .venv
.venv/bin/pip install Pillow==12.3.0
.venv/bin/python scripts/render_brand.py
```

Outputs in `profile/assets/`:

- `synehq-banner.png` — 1800 × 720 desktop banner.
- `synehq-banner-mobile.png` — 960 × 960 compact banner.
- `synehq-logo-wine.png`, `synehq-logo-ivory.png` — transparent logo lockups.

Review the generated artwork at its actual GitHub display size, on a narrow screen, and on light and dark backgrounds. The sources here are brand assets, not a grant to impersonate SyneHQ. Font licensing is separate and recorded in `fonts/*-OFL.txt`.

## Editorial sources

The profile was reviewed against these public sources on October 8, 2026:

- [SyneHQ workspace](https://synehq.com/) and [product pages](https://synehq.com/products/): positioning, Kole, Quantum Lab, sharing, and the current self-hosting boundary.
- [Kelvo README](https://github.com/SyneHQ/kelvo-go), [notebook index](https://github.com/SyneHQ/kelvo-go/blob/cargo/notebooks/README.md), and [contribution guide](https://github.com/SyneHQ/kelvo-go/blob/cargo/CONTRIBUTING.md): capabilities, preview status, examples, and ways to contribute.
- [Lumen](https://github.com/SyneHQ/lumen), [Rabbit](https://github.com/SyneHQ/rabbit.go), and [Kole MCP](https://github.com/SyneHQ/kole-mcp): individual project descriptions and account requirements.
- [Data Checks](https://synehq.com/community/) and the [SQL field guide](https://synehq.com/learn/): community purpose and free examples.

Do not turn roadmap items into available features or copy performance numbers without the workload and validation context. Link to current pricing and project licenses rather than duplicating them here.
