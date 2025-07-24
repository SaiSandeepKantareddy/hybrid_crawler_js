# hybrid-crawler-js

A scalable web crawler that intelligently decides **when** to render pages with JavaScript — saving infrastructure cost while maximizing content coverage.

Inspired by [Andrew Chan’s billion-page crawler](https://andrewkchan.dev/posts/crawler.html), this project adds a **conditional JS rendering layer**, driven by metadata heuristics like DOM sparsity, script count, and text length.

## Project Structure

```

hybrid\_crawler\_js/
├── crawler/
│   ├── base\_fetcher.py       # Fast async HTML fetcher
│   ├── js\_renderer.py        # Playwright-based JS renderer
│   └── scorer.py             # Heuristic scoring function
├── pipeline/
│   ├── hybrid\_runner.py      # Main orchestrator
│   └── config.yaml           # Config: input file + JS score threshold
├── utils/
│   └── metrics.py            # Coverage, cost, quality metrics
├── tests/
│   └── test\_end\_to\_end.py    # Test runner
├── data/
│   ├── urls\_sample.txt       # Sample URLs to crawl
│   └── hybrid\_output.csv     # Output: content, scores, flags
└── README.md

````

## Installation

```bash
git clone https://github.com/your-username/hybrid-crawler-js
cd hybrid-crawler-js

# Set up Python environment
pip install -r requirements.txt

# Install Playwright and browser engine
playwright install
````

## Usage

### Step 1: Add URLs to crawl

Edit `data/urls_sample.txt`:

```text
https://www.airbnb.com
https://twitter.com
https://www.linkedin.com/jobs
```

### Step 2: Adjust the config

`pipeline/config.yaml`:

```yaml
urls_file: data/urls_sample.txt
js_threshold: 0.7
```

Set `js_threshold` to `0.0` to **force JS rendering** for all URLs (for testing).

### Step 3: Run the hybrid crawler

```bash
python -m pipeline.hybrid_runner
```

This will:

* Fetch pages using `aiohttp`
* Score each page's content
* Render with Playwright only if needed
* Save results to `data/hybrid_output.csv`


## Example Output

`data/hybrid_output.csv`:

| URL                                                    | used\_js | score | error                                |
| ------------------------------------------------------ | -------- | ----- | ------------------------------------ |
| [https://airbnb.com](https://airbnb.com)               | True     | 0.7   |                                      |
| [https://twitter.com](https://twitter.com)             | False    | 1.0   | Playwright error (headers too large) |
| [https://linkedin.com/jobs](https://linkedin.com/jobs) | False    | 0.0   |                                      |


## Metrics

You can summarize the results using:

```bash
python utils/metrics.py
```

Sample Output:

```
Summary Metrics:
        total_pages: 3
   js_rendered_pages: 1
      js_rendered_%: 33.3
           avg_score: 0.566
       error_rate_%: 33.3
 avg_content_length: 18390
```

## How It Works

* `base_fetcher.py`: Async HTTP fetch for fast crawling
* `scorer.py`: Applies heuristic rules (text length, DOM density, noscript tags, etc.) to estimate whether JS is needed
* `js_renderer.py`: Uses Playwright to render JS-heavy pages on demand
* `hybrid_runner.py`: Orchestrates fetch → score → decide → render pipeline

## Testing

Run a full end-to-end test with:

```bash
python -m tests.test_end_to_end
```

Verifies output file creation, scoring, and JS routing behavior.

## Next Features

* Screenshot capture (`.png`)
* Parallel Playwright rendering pool
* robots.txt support
* Configurable scoring weights
* Lightweight JS-needed classifier (coming)

## Disclaimer

Sample URLs included in this project (e.g., Airbnb, Twitter, LinkedIn) are for **educational and testing purposes only**.

This project:

* Does **not** store, republish, or distribute any third-party content.
* Does **not** perform large-scale scraping.
* Is intended to demonstrate technical architecture for hybrid crawling only.

Always consult a website's **Terms of Service** and **robots.txt** before crawling at scale.

## Acknowledgements

Built as an open-source proof-of-concept following the brilliant [crawler performance post by Andrew Chan](https://andrewkchan.dev/posts/crawler.html).

## Questions or Suggestions?

Open an issue or drop a message.
