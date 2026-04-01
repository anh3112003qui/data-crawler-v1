import pytest
from src.crawler.core import crawl

def test_crawl_returns_placeholder():
    result = crawl()
    assert isinstance(result, list)
    assert result == ["https://example.com"]
