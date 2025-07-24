# Base HTML fetcher placeholder
import aiohttp
import asyncio
from aiohttp import ClientTimeout
from typing import List, Dict

class BaseFetcher:
    def __init__(self, timeout: int = 10, concurrency: int = 50):
        self.timeout = ClientTimeout(total=timeout)
        self.semaphore = asyncio.Semaphore(concurrency)

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> Dict:
        async with self.semaphore:
            try:
                async with session.get(url) as response:
                    text = await response.text()
                    return {
                        "url": url,
                        "status": response.status,
                        "content": text,
                        "error": None
                    }
            except Exception as e:
                return {
                    "url": url,
                    "status": None,
                    "content": "",
                    "error": str(e)
                }

    async def fetch_all(self, urls: List[str]) -> List[Dict]:
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            tasks = [self.fetch(session, url) for url in urls]
            return await asyncio.gather(*tasks)

# Example usage
if __name__ == "__main__":
    import sys
    import json

    urls = [
        "https://example.com",
        "https://example.org"
    ]

    fetcher = BaseFetcher()

    async def run():
        results = await fetcher.fetch_all(urls)
        for r in results:
            print(json.dumps(r, indent=2))

    asyncio.run(run())
