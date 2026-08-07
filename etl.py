import pandas as pd
#from sqlalchemy import create_engine

def run_etl():
    # Extract
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Jagdish", "Karlib"],
        "Age": [25, 30, 35, 21, 22],
    }
    df = pd.DataFrame(data)

    # Transform
    df["Age_in_5_years"] = df["Age"] + 5
    
    return df

if __name__ == "__main__":
    df = run_etl()
    print("Final DataFrame:")
    print(df)