import pandas as pd
import json
import glob
import os
from datetime import datetime

def transform_nasa_data():
    # Ensure staged directory exists
    os.makedirs("../DATA/STAGED", exist_ok=True)

    # Get latest raw NASA APOD file
    files = sorted(glob.glob("../DATA/RAW/nasa_apod_*.json"))
    if not files:
        raise FileNotFoundError("No NASA APOD raw JSON files found.")

    latest_file = files[-1]

    # Load JSON
    with open(latest_file, 'r') as f:
        data = json.load(f)

    # Build DataFrame with expected columns
    df = pd.DataFrame([{
        "date": data['date'],
        "title": data['title'],
        "explanation": data.get("explanation"),
        "url": data.get("url"),
        "hdurl": data.get("hdurl"),
        "media_type": data.get("media_type"),
        "service_version": data.get("service_version")
      
    }])

    # Output path
    output_path = "../DATA/STAGED/nasa_apod_cleaned.csv"
    df.to_csv(output_path, index=False)

    print(f"Transformed NASA APOD saved to: {output_path}")
    return df


if __name__ == "__main__":
    transform_nasa_data()
