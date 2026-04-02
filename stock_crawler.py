"""stock_crawler.py

Utility to fetch historical stock price data for a given ticker and year using Yahoo Finance.

Provides a `fetch_stock_history` function that returns a list of daily price dictionaries.
"""

import csv
import json
import time
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from typing import List, Dict

import requests


def _unix_timestamp(dt: datetime) -> int:
    """Convert a datetime to a Unix timestamp (seconds)."""
    return int(dt.replace(tzinfo=timezone.utc).timestamp())


def fetch_stock_history(symbol: str, year: int = 2024) -> List[Dict]:
    """Fetch daily historical stock data for `symbol` for the full `year`.

    The function queries Yahoo Finance's CSV download endpoint, parses the CSV,
    and returns a list of dictionaries with keys: date, open, high, low, close,
    adjclose, volume.
    """
    # Define start and end of the year in UTC
    start_dt = datetime(year, 1, 1, tzinfo=timezone.utc)
    end_dt = datetime(year, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
    period1 = _unix_timestamp(start_dt)
    period2 = _unix_timestamp(end_dt)

    url = (
        f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}"
        f"?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=true"
    )
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    # Parse CSV content
    csv_file = StringIO(response.text)
    reader = csv.DictReader(csv_file)
    data: List[Dict] = []
    for row in reader:
        # Convert numeric fields, handle missing data (e.g., "null")
        try:
            parsed = {
                "date": row["Date"],
                "open": float(row["Open"]) if row["Open"] != "null" else None,
                "high": float(row["High"]) if row["High"] != "null" else None,
                "low": float(row["Low"]) if row["Low"] != "null" else None,
                "close": float(row["Close"]) if row["Close"] != "null" else None,
                "adjclose": float(row["Adj Close"]) if row["Adj Close"] != "null" else None,
                "volume": int(row["Volume"]) if row["Volume"] != "null" else None,
            }
        except Exception:
            # Skip malformed rows
            continue
        data.append(parsed)
    return data


def save_to_json(data: List[Dict], path: Path) -> None:
    """Save the fetched data to a JSON file with indentation."""
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch historical stock data for a given ticker and year.")
    parser.add_argument("symbol", help="Ticker symbol, e.g., AAPL")
    parser.add_argument("--year", type=int, default=2024, help="Year to fetch data for (default: 2024)")
    parser.add_argument("--output", type=Path, default=None, help="Path to write JSON output. Defaults to <symbol>_<year>.json")
    args = parser.parse_args()

    result = fetch_stock_history(args.symbol, args.year)
    out_path = args.output or Path(f"{args.symbol}_{args.year}.json")
    save_to_json(result, out_path)
    print(f"Saved {len(result)} records to {out_path}")
