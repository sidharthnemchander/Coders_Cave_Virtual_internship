import pandas as pd

try:
    df = pd.read_csv("terrorism_data.csv")
except FileNotFoundError:
    print("Error: The 'terrorism_data.csv' file was not found.")
    df = None

if df is not None and not df.empty:
    if df["TARGET TYPE"].isnull().any():
        df["TARGET TYPE"].fillna("Unknown", inplace=True)

    df.drop_duplicates(inplace=True)

    try:
        df["INJURED"] = pd.to_numeric(df["INJURED"], errors="coerce")
    except ValueError:
        print("Error: Unable to convert 'INJURED' column to numeric.")

    df["DATE"] = pd.to_datetime(df["DATE"], dayfirst=True, errors="coerce")

    df = df[df["INJURED"] <= 1000]

    df.reset_index(drop=True, inplace=True)


    df.to_csv("cleaned_terrorism_data.csv", index=False)
else:
    print("Data cleaning cannot proceed due to missing or empty dataset.")


