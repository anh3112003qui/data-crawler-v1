import json
import unittest
from unittest.mock import patch, Mock
from pathlib import Path

from stock_crawler import fetch_stock_history, save_to_json

SAMPLE_CSV = """Date,Open,High,Low,Close,Adj Close,Volume
2024-01-02,100,110,90,105,105,1000000
2024-01-03,106,112,101,108,108,1200000
"""

class TestFetchStockHistory(unittest.TestCase):
    @patch('stock_crawler.requests.get')
    def test_fetch_parses_csv(self, mock_get):
        mock_resp = Mock()
        mock_resp.text = SAMPLE_CSV
        mock_resp.raise_for_status = Mock()
        mock_get.return_value = mock_resp

        data = fetch_stock_history('FAKE', year=2024)
        self.assertEqual(len(data), 2)
        first = data[0]
        self.assertEqual(first['date'], '2024-01-02')
        self.assertAlmostEqual(first['open'], 100.0)
        self.assertAlmostEqual(first['high'], 110.0)
        self.assertAlmostEqual(first['low'], 90.0)
        self.assertAlmostEqual(first['close'], 105.0)
        self.assertAlmostEqual(first['adjclose'], 105.0)
        self.assertEqual(first['volume'], 1000000)

    def test_save_to_json(self, tmp_path=Path('/tmp')):
        # Use a temporary directory provided by pytest could be better, but for simplicity use /tmp
        data = [{"date": "2024-01-02", "open": 100.0, "high": 110.0, "low": 90.0, "close": 105.0, "adjclose": 105.0, "volume": 1000000}]
        output_path = Path('/tmp/stock_test.json')
        save_to_json(data, output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            loaded = json.load(f)
        self.assertEqual(loaded, data)

if __name__ == '__main__':
    unittest.main()
