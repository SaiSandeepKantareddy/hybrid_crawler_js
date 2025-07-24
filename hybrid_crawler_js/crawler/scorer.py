# Heuristic scorer to decide if JS is needed placeholder
from bs4 import BeautifulSoup

def score_js_need(html: str) -> float:
    """
    Heuristic score for how likely a page needs JS rendering.
    Returns a float between 0.0 (no JS needed) and 1.0 (JS very likely needed).
    """
    if not html or len(html.strip()) == 0:
        return 1.0

    soup = BeautifulSoup(html, "lxml")
    text = soup.get_text(strip=True)

    # Features
    num_scripts = len(soup.find_all("script"))
    num_links = len(soup.find_all("a"))
    num_divs = len(soup.find_all("div"))
    num_imgs = len(soup.find_all("img"))
    text_length = len(text)

    score = 0.0

    if text_length < 100:
        score += 0.4

    if num_scripts > 10:
        score += 0.3

    if num_links < 5 and num_divs > 50:
        score += 0.2

    if num_imgs == 0:
        score += 0.1

    if "please enable javascript" in text.lower():
        score += 0.6

    if soup.find("noscript"):
        score += 0.4

    return min(score, 1.0)



# Example usage
if __name__ == "__main__":
    test_html = """
    <html><head><script src="a.js"></script></head>
    <body><div>Welcome</div><script></script><script></script></body></html>
    """
    score = score_js_need(test_html)
    print(f"JS-needed score: {score:.2f}")
