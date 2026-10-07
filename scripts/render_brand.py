#!/usr/bin/env python3
"""Render the GitHub profile artwork with Pillow and the approved raster identity."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "brand" / "source"
FONTS = ROOT / "brand" / "fonts"
OUTPUT = ROOT / "profile" / "assets"
WINE, IVORY, BLUSH, CORAL = "#26191D", "#FFF7F4", "#FFB8B0", "#FF6666"


def font(family, size, weight):
    face = ImageFont.truetype(str(FONTS / f"{family}-Variable.ttf"), size)
    axes = face.get_variation_axes()
    face.set_variation_by_axes([
        weight if axis["name"] == b"Weight" else
        36 if axis["name"] == b"Optical size" else axis["default"]
        for axis in axes
    ])
    return face


def lockup(symbol_height, color):
    """Keep full ink heights at 1:0.78, gap 0.26, and center the descenders."""
    symbol = Image.open(SOURCE / "approved-symbol-mask.png").convert("L")
    word = Image.open(SOURCE / "approved-wordmark-mask.png").convert("L")
    sh, wh = symbol_height, round(symbol_height * 0.78)
    sw = round(symbol.width * sh / symbol.height)
    ww = round(word.width * wh / word.height)
    gap = round(symbol_height * 0.26)
    mask = Image.new("L", (sw + gap + ww, sh))
    mask.paste(symbol.resize((sw, sh), Image.Resampling.LANCZOS), (0, 0))
    mask.paste(word.resize((ww, wh), Image.Resampling.LANCZOS), (sw + gap, (sh - wh) // 2))
    ink = Image.new("RGBA", mask.size, color)
    ink.putalpha(mask)
    return ink


def pattern(canvas, right_crop=0):
    """Use native square cells, cropped at the canvas edge, with 75% opacity."""
    pixels = Image.open(SOURCE / "customer-pixel-pattern.png").convert("RGBA")
    pixels.putalpha(pixels.getchannel("A").point(lambda a: round(a * 0.75)))
    canvas.alpha_composite(pixels, (canvas.width - pixels.width + right_crop, canvas.height - pixels.height))


def text(draw, xy, words, face, color):
    draw.text(xy, words, font=face, fill=color, anchor="lt")


def render_banner(mobile=False):
    size = (960, 960) if mobile else (1800, 720)
    canvas = Image.new("RGBA", size, WINE)
    pattern(canvas, right_crop=300 if not mobile else 0)
    draw = ImageDraw.Draw(canvas)
    if mobile:
        canvas.alpha_composite(lockup(78, IVORY), (72, 70))
        text(draw, (72, 235), "Answers your", font("Newsreader", 120, 430), IVORY)
        text(draw, (72, 365), "team can check.", font("Newsreader", 120, 430), BLUSH)
        text(draw, (76, 545), "AI analytics workspace", font("Manrope", 36, 500), IVORY)
        text(draw, (76, 609), "Ask. Inspect. Share.", font("Manrope", 31, 500), BLUSH)
    else:
        canvas.alpha_composite(lockup(76, IVORY), (96, 74))
        text(draw, (100, 235), "Answers your", font("Newsreader", 144, 430), IVORY)
        text(draw, (100, 386), "team can check.", font("Newsreader", 144, 430), BLUSH)
        text(draw, (104, 590), "AI analytics workspace", font("Manrope", 34, 500), IVORY)
    filename = "synehq-banner-mobile.png" if mobile else "synehq-banner.png"
    canvas.convert("RGB").save(OUTPUT / filename, optimize=True)


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    render_banner()
    render_banner(mobile=True)
    for name, color in [("ivory", IVORY), ("wine", WINE)]:
        lockup(222, color).save(OUTPUT / f"synehq-logo-{name}.png", optimize=True)
    print("Rendered desktop/mobile banners and two transparent logo lockups.")
