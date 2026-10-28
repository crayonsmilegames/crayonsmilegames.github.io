# CrayonSmile studio website

Public site: https://crayonsmilegames.github.io/

This repository contains only the public website. GitHub Pages publishes the
repository root from `main`. Keep the Godot app, private documents and release
files outside this repository.

## Local preview and validation

Run from this repository:

```sh
python -m http.server 8765 --bind 127.0.0.1
python tools/build_brand_pages.py
python tools/validate_seo.py
python tools/audit_live_search.py
```

Preview `/` and `/en/` and all four product routes at desktop and mobile sizes.
The homepages introduce the studio and link to `/games/somi-kids-world/`,
`/games/hangul-abc/`, `/games/somi-flashcards/` and `/games/somi-coloring/`.
Every product has an equivalent route under `/en/games/`. Privacy URLs stay the
same. Legacy Kids World feature/FAQ hashes redirect to its detailed product page;
`#somi-coloring` still points to the coloring card on the homepage.

`tools/build_brand_pages.py` holds the bilingual studio and new product copy.
The existing Kids World pages are preserved separately, including their FAQ,
screenshots and interactions. The validator checks all 12 public HTML pages,
local links and fragments, canonical and reciprocal language links, schema/FAQ
text agreement, store links, launch-state claims, sitemap coverage, crawler
access and UTF-8/CRLF encoding. It does not certify indexing or search rankings.
The live audit must run after publishing: it compares the 12 served pages with
local sources and checks HTTP indexing headers, the live sitemap/robots files,
and access with Googlebot, Bingbot, Yeti, OAI-SearchBot and PerplexityBot headers.
Header simulation does not prove actual crawler visits or account-side indexing.

Hangul ABC and FlashCards are marked coming soon. Add a verified store URL and
update the release state in the generator only when a product launches. Keep
the corresponding sitemap date current when publishing changed pages. Do not
change the privacy policy's effective date just for a navigation change.

## SEO and AI search maintenance

- Keep Korean and English metadata and factual app descriptions aligned.
- Update visible FAQ answers and matching JSON-LD answers together. The validator
  rejects drift.
- Organization and WebSite have shared `@id` values; the brand homepages use
  CollectionPage and ItemList. Product pages use SoftwareApplication and WebPage;
  Kids World pages also have matching visible FAQPage content.
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

SEO reference links:

- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/specialty/international/localized-versions
- https://developers.google.com/search/docs/appearance/structured-data/software-app
- https://developers.openai.com/api/docs/bots

Support: crayonsmile.games@gmail.com

## Public product artwork and factual sources

The separate Somi Coloring app has its own product page and Google Play link.
Keep it distinct from the coloring activity inside Somi Kids World.
Kids World pages describe only their own app and built-in coloring activity;
keep the separate Somi Coloring promotion and app schema on its own pages.

Public artwork in `assets/somi-coloring/` is copied unchanged from the Somi
Coloring Google Play upload assets. Product text is based on its store listing
and developer-provided store materials. Do not transfer Kids World content-pack,
storybook or family-recording claims to this separate app.

Hangul ABC copy follows its reviewed 2026-10-16 Korean store listing, titled
`소미와 가나다 한글놀이`; the internal project folder is `HangulABC`.
FlashCards copy follows `export/store-listing/ko-KR/full-description.txt`, titled
`소미와 낱말카드 놀이`. Avoid older design counts: the reviewed listing describes
20 collections and 400 cards, with some paid collections.

The new artwork is copied unchanged from reviewed public store-listing assets.
`tools/public-asset-provenance.json` records source paths and SHA256 hashes.
Only public marketing artwork belongs here; never copy app source or private data.

## Privacy policy maintenance

`tools/privacy_content.py` is the bilingual policy source; the site generator
builds `/privacy/` and `/en/privacy/` together. The policy effective date is
2026-10-28. Keep the app list, local profile data, guardian narration, on-device
camera/face landmarks, gallery storage, permissions, deletion and Google Play
processing aligned with the actual app behavior. Website hosting/font requests
and voluntary guardian support email are described separately from app-local data.

Runtime sources checked for this revision: Kids World's `scripts/main.gd`,
`scripts/audio_pack_manager.gd`, selfie bridge and privacy checklist; HangulABC's
`scripts/profile_editor.gd` and `scripts/progress_store.gd`; FlashCards'
`scripts/app_root.gd`; Coloring's canvas/app scripts; each app's export permissions
and Android manifest. Kids World currently requests camera/microphone permissions
after its first-launch introduction, as well as in feature flows when needed;
the policy describes this observed behavior. App permission timing changes require
separate runtime work and are not performed by the website generator.

Search guidance reviewed: Google Search Central's generative AI optimization
guide, OpenAI's crawler documentation and Naver Search Advisor's content-markup
guide. Existing normal SEO, crawlable factual text, language/canonical links and
consistent structured data are the foundation; no AI-specific file guarantees
indexing or inclusion in answers. Privacy references: Google Play User Data policy,
Google Privacy Policy and GitHub Pages/Privacy documentation.
