# etl.py
import pandas as pd

def run_etl():
    # Extract
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Jagdish"],
        "Age": [25, 30, 35, 21],
    }
    df = pd.DataFrame(data)

    # Transform
    df["Age_in_5_years"] = df["Age"] + 5

    # Load (just print for now)
    print("Final DataFrame:")
    print(df)

if __name__ == "__main__":
    run_etl()