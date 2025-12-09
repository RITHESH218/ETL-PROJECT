# 4. load_weather.py
 
import os

import time

import pandas as pd

from supabase import create_client

from dotenv import load_dotenv
 
# Initialize the Supabase client

load_dotenv()

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
 
 
def load_to_supabase():

    # Load cleaned CSV

    csv_path = "../DATA/STAGED/nasa_apod_cleaned.csv"

    if not os.path.exists(csv_path):

        raise FileNotFoundError(f"Missing file: {csv_path}")
 
    df = pd.read_csv(csv_path)

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d") 
    df = df.where(pd.notnull(df), None)

    batch_size = 10
 
    # Batch Insert Loop

    for i in range(0, len(df), batch_size):

        batch_df = df.iloc[i:i + batch_size]
        batch = batch_df.to_dict("records")

        values = [
            (
                f"('{r['date']}', "
                f"'{r['title']}', "
                f"'{(r['explanation'] or '').replace('\'', '\'\'')}', "
                f"'{(r.get('url') or '')}', "
                f"'{(r['hdurl'] or '')}', "
                f"'{(r.get('media_type') or '')}', "
                f"'{(r.get('service_version') or '')}')"
            )
            for r in batch
        ]
 
        insert_sql = (
            "INSERT INTO nasa_apod "
            "(date, title, explanation, url, hdurl, media_type, service_version) "
            f"VALUES {','.join(values)};"
        )
 
        # Execute SQL via RPC

        supabase.rpc("execute_sql", {"query": insert_sql}).execute()

        print(f"Inserted rows {i + 1} → {min(i + batch_size, len(df))}")
        time.sleep(0.3)
 
    print("Finished loading NASA APOD data.")
 
 
if __name__ == "__main__":

    load_to_supabase()

 