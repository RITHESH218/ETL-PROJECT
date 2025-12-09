import os
import time
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv

# Load env variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL","").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY","").strip()

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase credentials missing. Set SUPABASE_URL and SUPABASE_KEY.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def escape_string(value):
    """Escape single quotes for SQL."""
    if value is None:
        return ""
    return str(value).replace("'", "''")


def load_to_supabase():
    # Compute CSV path relative to this script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "../DATA/STAGED/nasa_apod_cleaned.csv")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing file: {csv_path}")

    df = pd.read_csv(csv_path)

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df["extracted_at"] = pd.to_datetime(df["extracted_at"]).dt.strftime("%Y-%m-%d %H:%M:%S")

    df = df.where(pd.notnull(df), None)

    batch_size = 10

    for i in range(0, len(df), batch_size):
        batch_df = df.iloc[i:i + batch_size]
        batch = batch_df.to_dict("records")

        values = [
            (
                f"('{r['date']}', "
                f"'{escape_string(r['title'])}', "
                f"'{escape_string(r.get('explanation'))}', "
                f"'{escape_string(r.get('url'))}', "
                f"'{escape_string(r.get('hdurl'))}', "
                f"'{escape_string(r.get('media_type'))}', "
                f"'{escape_string(r.get('service_version'))}', "
                f"'{r['extracted_at']}')"
            )
            for r in batch
        ]

        insert_sql = (
            "INSERT INTO nasa_apod "
            "(date, title, explanation, url, hdurl, media_type, service_version, extracted_at) "
            f"VALUES {','.join(values)};"
        )

        supabase.rpc("execute_sql", {"query": insert_sql}).execute()

        print(f"Inserted rows {i + 1} → {min(i + batch_size, len(df))}")
        time.sleep(0.3)

    print("Finished loading NASA APOD data.")



if __name__ == "__main__":
    load_to_supabase()
