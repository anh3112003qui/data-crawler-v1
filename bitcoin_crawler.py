"""bitcoin_crawler.py

Utility to fetch historical Bitcoin price data for a given year using CoinGecko.

Provides a `fetch_bitcoin_history` function that returns a list of daily price dictionaries.
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict

import requests


def _format_date(dt: datetime) -> str:
    """Format datetime as DD-MM-YYYY for CoinGecko API."""
    return dt.strftime("%d-%m-%Y")


def fetch_bitcoin_history(year: int = 2025) -> List[Dict]:
    """Fetch daily Bitcoin price (USD) for each day of `year`.

    Uses CoinGecko's `/coins/bitcoin/history` endpoint which accepts a date string.
    Returns a list of dicts with keys: `date` (YYYY-MM-DD) and `price_usd` (float).
    """
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    delta = timedelta(days=1)
    result: List[Dict] = []
    cur = start
    while cur <= end:
        date_str = _format_date(cur)
        url = f"https://api.coingecko.com/api/v3/coins/bitcoin/history?date={date_str}&localization=false"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        # Navigate JSON structure safely
        price = (
            data.get("market_data", {})
            .get("current_price", {})
            .get("usd")
        )
        if price is not None:
            result.append({"date": cur.strftime("%Y-%m-%d"), "price_usd": float(price)})
        else:
            # If price missing, record None
            result.append({"date": cur.strftime("%Y-%m-%d"), "price_usd": None})
        # Respect CoinGecko rate limits (max 10-30 calls/sec). Sleep a bit.
        time.sleep(1)
        cur += delta
    return result


def save_to_json(data: List[Dict], path: Path) -> None:
    """Save the fetched data to a JSON file with indentation."""
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch Bitcoin price data for a given year.")
    parser.add_argument("--year", type=int, default=2025, help="Year to fetch data for (default: 2025)")
    parser.add_argument("--output", type=Path, default=None, help="Path to write JSON output.")
    args = parser.parse_args()

    data = fetch_bitcoin_history(args.year)
    out_path = args.output or Path(f"bitcoin_{args.year}.json")
    save_to_json(data, out_path)
    print(f"Saved {len(data)} records to {out_path}")
