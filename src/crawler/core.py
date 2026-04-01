"""Placeholder crawler implementation.

The real crawler would contain network requests, parsing logic, and data storage.
For now we provide a simple function that returns a static list so the package
has importable behaviour and can be exercised by tests.
"""

def crawl() -> list[str]:
    """Return a static list of dummy URLs.

    Returns
    -------
    list[str]
        A list containing a single placeholder URL string.
    """
    return ["https://example.com"]
