import pandas as pd
import json
import glob
import os
from datetime import datetime

def transform_nasa_data():
    # Base dir = script folder
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    raw_dir = os.path.join(BASE_DIR, "../DATA/RAW")
    staged_dir = os.path.join(BASE_DIR, "../DATA/STAGED")
    os.makedirs(staged_dir, exist_ok=True)

    # Find latest raw NASA JSON
    files = sorted(glob.glob(os.path.join(raw_dir, "nasa_apod_*.json")))
    if not files:
        raise FileNotFoundError("No NASA APOD raw JSON files found.")

    latest_file = files[-1]

    with open(latest_file, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame([{
        "date": data.get("date"),
        "title": data.get("title"),
        "explanation": data.get("explanation"),
        "url": data.get("url"),
        "hdurl": data.get("hdurl"),
        "media_type": data.get("media_type"),
        "service_version": data.get("service_version"),
        "extracted_at": datetime.now()
    }])

    output = os.path.join(staged_dir, "nasa_apod_cleaned.csv")
    df.to_csv(output, index=False)

    print(f"Transformed NASA APOD saved to: {output}")
    return df

if __name__ == "__main__":
    transform_nasa_data()
