import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("cleaned_terrorism_data.csv")
except FileNotFoundError:
    print("Error: The 'cleaned_terrorism_data.csv' file was not found.")
    df = None

if df is not None and not df.empty:
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    plt.figure(figsize=(12, 6))
    group_inj_fata = df.groupby("PERPETRATOR GROUP")["INJ AND FATA"].sum().reset_index()
    group_inj_fata = group_inj_fata.sort_values(by="INJ AND FATA", ascending=False).head(20)
    sns.barplot(data=group_inj_fata, x="PERPETRATOR GROUP", y="INJ AND FATA", palette="Set2")
    plt.title('Top 20 PERPETRATOR GROUPs by INJ AND FATA')
    plt.xlabel('PERPETRATOR GROUP')
    plt.ylabel('Count')
    plt.xticks(rotation=90)

    
    plt.show()

    
    plt.figure(figsize=(12, 6))
    city_inj_fata = df.groupby("CITY")[["INJ AND FATA"]].sum().reset_index()
    city_inj_fata = city_inj_fata.sort_values(by="INJ AND FATA", ascending=False).head(20)
    sns.barplot(data=city_inj_fata, x="CITY", y="INJ AND FATA", palette="Set2")
    plt.title('Top 20 Cities by INJ AND FATA')
    plt.xlabel('CITY')
    plt.ylabel('Count')
    plt.xticks(rotation=90)

    plt.show()

    df = df.dropna(subset=['DATE'])

    if not df.empty:
        
        plt.figure(figsize=(12, 6))
        top_20_cities = city_inj_fata['CITY']
        df_top_20 = df[df['CITY'].isin(top_20_cities)]
        sns.lineplot(data=df_top_20, x='DATE', y='INJ AND FATA', hue='CITY', palette="Set2")
        plt.title('INJ AND FATA Over Time for Top 20 Cities')
        plt.xlabel('DATE')
        plt.ylabel('INJ AND FATA')
        plt.xticks(rotation=45)

        
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(12, 6))
        inj_fata_zero = df[df['INJ AND FATA'] == 0]
        sns.histplot(data=inj_fata_zero, x='PERPETRATOR GROUP', discrete=True, color='skyblue')
        plt.title('Histogram of PERPETRATOR GROUP with least fatalities')
        plt.xlabel('PERPETRATOR GROUP')
        plt.ylabel('Count')
        plt.xticks(rotation=90)

        plt.show()

    else:
        print("Data analysis cannot proceed due to empty dataset after filtering by 'DATE'.")

else:
    print("Data analysis cannot proceed due to missing or empty dataset.")
