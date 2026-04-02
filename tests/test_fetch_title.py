import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from unittest.mock import Mock, patch
from src.crawler.core import fetch_title

def test_fetch_title_success():
    html = "<html><head><title>Example Page</title></head><body></body></html>"
    mock_response = Mock()
    mock_response.text = html
    mock_response.raise_for_status = Mock()
    with patch('requests.get', return_value=mock_response) as mock_get:
        title = fetch_title('http://example.com')
        mock_get.assert_called_once_with('http://example.com')
        assert title == "Example Page"

def test_fetch_title_no_title():
    html = "<html><head></head><body></body></html>"
    mock_response = Mock()
    mock_response.text = html
    mock_response.raise_for_status = Mock()
    with patch('requests.get', return_value=mock_response):
        title = fetch_title('http://example.com')
        assert title == ""
