#!/usr/bin/env python3
"""Compose the Solmara poster: square-crop the AI scene (keeping the
lighthouse), set the name and tagline with PIL, and write entry.png
(1024x1024). Deterministic: same inputs give the same bytes."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import hashlib

SRC = 'scene.png'
SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def tracked_text(draw, cx, y, text, font, fill, tracking=0):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + tracking


def shadow_text(base, cx, y, text, font, fill, shadow, tracking=0, blur=3, dy=4):
    layer = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    widths = [d.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        d.text((x, y + dy), ch, font=font, fill=shadow)
        x += w + tracking
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(layer)
    d2 = ImageDraw.Draw(base)
    tracked_text(d2, cx, y, text, font, fill, tracking)


def main():
    im = Image.open(SRC).convert('RGB')
    crop = im.crop((640, 0, 1920, 1280)).resize((1024, 1024), Image.LANCZOS)
    out = crop.convert('RGBA')
    WHITE = (255, 255, 255, 255)
    SHADOW = (10, 40, 90, 180)
    GOLD = (255, 200, 90, 255)
    title_font = ImageFont.truetype(SERIF, 104)
    shadow_text(out, 512, 42, 'SOLMARA', title_font, WHITE, SHADOW,
                tracking=18, blur=4, dy=5)
    d = ImageDraw.Draw(out)
    d.rectangle([512 - 70, 172, 512 + 70, 176], fill=GOLD)
    tag_font = ImageFont.truetype(SANS, 33)
    shadow_text(out, 512, 952, 'WHERE THE LIGHT COMES HOME', tag_font,
                WHITE, SHADOW, tracking=6, blur=3, dy=3)
    out.convert('RGB').save('entry.png', 'PNG')
    data = open('entry.png', 'rb').read()
    print('entry.png bytes:', len(data))
    print('entry.png sha256:', hashlib.sha256(data).hexdigest())


if __name__ == '__main__':
    main()
