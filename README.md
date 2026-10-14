# Somi Kids World · CrayonSmile website

Public site: https://crayonsmilegames.github.io/

This repository contains only the public website. GitHub Pages publishes the
repository root from `main`. Keep the Godot app, private documents and release
files outside this repository.

## Local preview and validation

Run from this repository:

```sh
python -m http.server 8765 --bind 127.0.0.1
python tools/validate_seo.py
```

Preview `/` and `/en/` at desktop and mobile sizes. Check the app summary, FAQ
keyboard/touch interaction and no-JavaScript readability. The validator checks
all four public HTML pages, local links and fragments, canonical and reciprocal
language links, schema/FAQ text agreement, store links, sitemap coverage, crawler
access and UTF-8/CRLF encoding. It does not certify indexing or search rankings.

## SEO and AI search maintenance

- Keep Korean and English metadata and factual app descriptions aligned.
- Update visible FAQ answers and matching JSON-LD answers together. The validator
  rejects drift.
- Organization, WebSite and SoftwareApplication have stable shared `@id` values;
  each language page has its own WebPage and FAQPage identifiers.
- Free download does not mean every content pack is free. Keep this distinction
  in visible copy and the offer description. Do not invent ratings or reviews
  to qualify for software-app rich results.
- Preserve the existing Google verification token. Its presence does not prove
  the Search Console property is currently verified or accessible.
- `robots.txt` allows public search crawlers including OAI-SearchBot. Search
  access and model-training controls are separate; this update preserves the
  existing general crawler policy.
- Update sitemap `lastmod` and page `dateModified` only when that page changes.
  The FAQ review date is not the effective date of the privacy policy.
- No special AI file or schema guarantees inclusion in generated answers. FAQ
  markup describes visible content and does not promise FAQ rich results.

After deployment, check the live pages and sitemap. In an authorized Google
Search Console account, submit `https://crayonsmilegames.github.io/sitemap.xml`
and inspect both homepage URLs. Review impressions, queries, clicks and indexed
pages over time. No tracking SDK is added to the site.

Official references checked for this update:

- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/specialty/international/localized-versions
- https://developers.google.com/search/docs/appearance/structured-data/software-app
- https://developers.openai.com/api/docs/bots

Support: crayonsmile.games@gmail.com
