"""Entry point for the placeholder crawler.

Running this module will invoke the dummy ``crawl`` function and print its
result. This demonstrates that the package is importable and that the
project layout works with ``python -m src.main``.
"""

from src.crawler.core import crawl

def main() -> None:
    results = crawl()
    for url in results:
        print(f"Crawled: {url}")

if __name__ == "__main__":
    main()
