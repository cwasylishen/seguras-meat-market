# Seguras Meat Market — Sample Website

One-page sample site for **Seguras Meat Market**, a family-run, 100% grass-fed butcher shop in Uvita, Puntarenas, Costa Rica.

Built as a static HTML site for deployment on Cloudflare Pages.

## Live preview

Connect this repo to Cloudflare Pages with no build command and root output directory — it serves as-is.

## Deploy to Cloudflare Pages

1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git
2. Pick this repository
3. Build settings:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Build output directory:** `/`
   - **Root directory:** *(leave empty)*
4. Save and deploy

## Regenerate images

If you swap in new source photos, drop them next to `process_images.py` and run:

```
python process_images.py
```

This regenerates the responsive WebP variants and the transparent logo PNGs.

## Contact (business)

- Phone: +506 7021 5929
- WhatsApp: +506 8584 9777
- Email: Info@segurascr.com
- Facebook: https://www.facebook.com/segurasbutcher/
- Instagram: https://www.instagram.com/segurasmeatmarket/
