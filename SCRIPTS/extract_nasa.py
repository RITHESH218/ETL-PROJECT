import os
import json
from pathlib import Path
from datetime import datetime
import requests # type: ignore

# Directory to save raw NASA data
DATA_DIR = Path(__file__).resolve().parents[1] / "DATA" / "RAW"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def extract_nasa_apod():
    api_key = os.getenv("NASA_API_KEY")  # <-- using environment variable
    if not api_key:
        raise ValueError("NASA_API_KEY is missing. Set it in environment variables.")

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key
    }

    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    # Save raw JSON file
    filename = DATA_DIR / f"nasa_apod_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filename.write_text(json.dumps(data, indent=2))

    print(f"Extracted NASA APOD saved to: {filename}")
    return data

if __name__ == "__main__":
    extract_nasa_apod()
