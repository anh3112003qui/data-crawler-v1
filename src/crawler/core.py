"""Placeholder crawler implementation.

The real crawler would contain network requests, parsing logic, and data storage.
For now we provide a simple function that returns a static list so the package
has importable behaviour and can be exercised by tests.
"""

import re
import requests

def crawl() -> list[str]:
    """Return a static list of dummy URLs.

    Returns
    -------
    list[str]
        A list containing a single placeholder URL string.
    """
    return ["https://example.com"]


def fetch_title(url: str) -> str:
    """Fetch a URL and return its HTML page title.

    Returns an empty string if the title cannot be found.
    """
    response = requests.get(url)
    response.raise_for_status()
    match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

