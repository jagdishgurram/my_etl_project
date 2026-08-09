import pandas as pd
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL

from dotenv import load_dotenv
import os
load_dotenv()

connection = os.getenv("CONNECTION_URL")
engine = create_engine(connection)

def run_etl():
    # Extract
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Jagdish", "Karlib", "Tarun"],
        "Age": [25, 30, 35, 21, 22, 20],
    }
    df = pd.DataFrame(data)

    # Transform
    df["Age_in_5_years"] = df["Age"] + 5
    
    df.to_sql(
        "employees",
        engine,
        if_exists="append",
        index=False
    )
    
    return df

if __name__ == "__main__":
    df = run_etl()
    print("Final DataFrame:")
    print(df)