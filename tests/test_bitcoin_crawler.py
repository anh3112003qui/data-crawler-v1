import builtins
import json
from datetime import datetime
from unittest.mock import patch, MagicMock

import pytest

from bitcoin_crawler import fetch_bitcoin_history

# Helper to generate mock response JSON
def make_mock_response(price):
    return {
        "market_data": {
            "current_price": {"usd": price}
        }
    }

@pytest.mark.parametrize("year,expected_days", [
    (2025, 2),  # We'll limit the range in the mock to first two days
])
def test_fetch_bitcoin_history(monkeypatch, year, expected_days):
    # Prepare a side_effect function that returns a mock response for each day
    call_counter = {'i': 0}

    def mock_get(url, timeout=30):
        # Increment counter per call
        i = call_counter['i']
        call_counter['i'] += 1
        # Generate a price that increments by 100 each day starting at 50000
        price = 50000 + i * 100
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = make_mock_response(price)
        return mock_resp

    # Patch requests.get to use the dynamic mock and bypass sleep
    with patch("requests.get", side_effect=mock_get) as mock_get_func:
        with patch('time.sleep', return_value=None):
            result = fetch_bitcoin_history(year)
        # Verify the first two days have the expected prices
        assert result[0]["date"] == datetime(year, 1, 1).strftime("%Y-%m-%d")
        assert result[0]["price_usd"] == 50000.0
        assert result[1]["date"] == datetime(year, 1, 2).strftime("%Y-%m-%d")
        assert result[1]["price_usd"] == 50100.0
        # Ensure requests.get was called for at least the first two days
        assert mock_get_func.call_count >= 2
