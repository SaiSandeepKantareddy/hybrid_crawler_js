# hybrid_crawler_js

A minimal, scalable crawler with conditional JavaScript rendering — built to balance coverage and cost at web scale.

## What It Does

This crawler intelligently decides **when to run JavaScript rendering** (e.g. via Playwright) based on metadata like page structure, script density, and content sparsity.

Instead of rendering every page (which is expensive), it:
- Fetches HTML fast using `aiohttp`
- Scores each page for "JS-needed-ness" using simple heuristics
- Triggers JS rendering only when needed
- Tracks metrics: coverage uplift, rendering rate, cost per page

## Tech Stack

- `aiohttp` – for async HTML fetching  
- `Playwright` – headless JS rendering on demand  
- `BeautifulSoup` / `lxml` – for HTML parsing  
- `pandas`, `tqdm` – for metrics and logging


