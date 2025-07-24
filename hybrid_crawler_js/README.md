# hybrid-crawler-js

A minimal, scalable crawler with conditional JavaScript rendering — built to balance coverage and cost at web scale.

## 🚀 What It Does

This crawler intelligently decides **when to run JavaScript rendering** (e.g. via Playwright) based on metadata like page structure, script density, and content sparsity.

Instead of rendering every page (which is expensive), it:
- Fetches HTML fast using `aiohttp`
- Scores each page for "JS-needed-ness" using simple heuristics
- Triggers JS rendering only when needed
- Tracks metrics: coverage uplift, rendering rate, cost per page

## 🔧 Tech Stack

- `aiohttp` – for async HTML fetching  
- `Playwright` – headless JS rendering on demand  
- `BeautifulSoup` / `lxml` – for HTML parsing  
- `pandas`, `tqdm` – for metrics and logging

## 🏗️ Folder Structure

```
hybrid_crawler_js/
├── crawler/           # Base fetcher, JS renderer, heuristics
├── pipeline/          # Main orchestration and config
├── utils/             # Logging and metrics
├── tests/             # Test scripts
├── data/              # Sample URLs and output
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

## 🧪 Example Use Case

Crawl 10M pages. Only 20% need JS rendering.  
You save **80% infra cost** and still capture **all meaningful content**.

## 📈 Coming Soon

- Coverage vs cost graphs
- A/B test harness
- Real-world benchmarks on public URL datasets

## 🙌 Inspired By

Andrew Chan’s blazing-fast crawler @ https://andrewkchan.dev/posts/crawler.html  
This builds on that idea to add **intelligent hybrid parsing.**

---

Contributions and suggestions welcome!
