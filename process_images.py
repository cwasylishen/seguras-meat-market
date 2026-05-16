"""Generate web-optimized assets for Seguras Meat Market site."""
import os
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

def make_sizes(infile, base, sizes):
    """Resize an image to multiple widths and save as WebP."""
    img = Image.open(infile).convert('RGB')
    aspect = img.height / img.width
    for width, suffix, quality in sizes:
        new_h = int(width * aspect)
        out = img.resize((width, new_h), Image.LANCZOS)
        outfile = f"{base}{suffix}.webp"
        out.save(outfile, 'WEBP', quality=quality, method=6)
        kb = os.path.getsize(outfile) // 1024
        print(f"  {outfile:32s} {width}x{new_h}  {kb} KB")

print("Hero (steak on cutting board)...")
make_sizes('hero.jpg', 'hero', [
    (640,  '-mobile',  78),
    (1024, '-tablet',  80),
    (1440, '-desktop', 82),
])

print("Craft (meatball rolling, Seguras paper)...")
make_sizes(
    '568594556_18071260922251384_1512553144303937946_n.jpg',
    'craft',
    [(600, '-sm', 80), (900, '-md', 82)],
)

print("Cuts (overhead tray of cuts and veg)...")
make_sizes(
    '566969686_18071260949251384_4152304506735328126_n.jpg',
    'cuts',
    [(600, '-sm', 80), (900, '-md', 82)],
)

print("Fire (flame-licked steak on grill)...")
make_sizes(
    '540534832_18065662712251384_490209066222765275_n.jpg',
    'fire',
    [(800, '-sm', 80), (1400, '-md', 82)],
)

print("Logo (transparent variants)...")
src = Image.open('logo.jpg').convert('L')
# Wordmark is black on white. Invert -> wordmark becomes white on black.
# Use the inverted image as the alpha channel for solid-color renders.
inverted = ImageOps.invert(src)

def render_logo(color_rgb, outfile):
    canvas = Image.new('RGBA', src.size, color_rgb + (0,))
    canvas.putalpha(inverted)
    bbox = canvas.getbbox()
    if bbox:
        # Add a small padding around the cropped area
        pad = 8
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                min(canvas.width, bbox[2] + pad), min(canvas.height, bbox[3] + pad))
        canvas = canvas.crop(bbox)
    canvas.save(outfile, 'PNG', optimize=True)
    kb = os.path.getsize(outfile) // 1024
    print(f"  {outfile:32s} {canvas.size}  {kb} KB")

# logo-dark.png  = used on DARK backgrounds  -> WHITE wordmark on transparent
render_logo((255, 255, 255), 'logo-dark.png')
# logo-light.png = used on LIGHT backgrounds -> BLACK wordmark on transparent (also used as favicon)
render_logo((0, 0, 0), 'logo-light.png')

print("Done.")
