# Orchestration logic placeholder
import asyncio
import yaml
import pandas as pd
from tqdm import tqdm

from crawler.base_fetcher import BaseFetcher
from crawler.scorer import score_js_need
from crawler.js_renderer import JSRenderer
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def load_urls(config_path: str) -> (list, float):
    """Load URLs and JS threshold from config YAML"""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    with open(config['urls_file'], 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
    return urls, float(config.get("js_threshold", 0.7))


async def main(config_path: str):
    # Load config
    urls, threshold = load_urls(config_path)

    # Initialize components
    fetcher = BaseFetcher()
    renderer = JSRenderer()
    hybrid_results = []

    print(f"\nFetching {len(urls)} URLs...")
    fetch_results = await fetcher.fetch_all(urls)

    print("\nScoring pages and conditionally rendering with JS...")
    for result in tqdm(fetch_results):
        url = result["url"]
        html = result["content"]
        error = result["error"]

        if error:
            hybrid_results.append({**result, "used_js": False, "score": 1.0})
            continue

        score = score_js_need(html)

        if score >= threshold:
            # Re-render with JS
            rendered_result = await renderer.render_page(url)
            hybrid_results.append({**rendered_result, "used_js": True, "score": score})
        else:
            # Use original content
            hybrid_results.append({**result, "used_js": False, "score": score})

    # Save results
    df = pd.DataFrame(hybrid_results)
    df.to_csv("data/hybrid_output.csv", index=False)
    print("\nDone. Saved to data/hybrid_output.csv")


if __name__ == "__main__":
    asyncio.run(main("pipeline/config.yaml"))
