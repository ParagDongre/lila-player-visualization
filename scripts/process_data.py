import pandas as pd
import os

data_folder = "data/player_data"

all_data = []

for root, dirs, files in os.walk(data_folder):
    for file in files:
        if file.endswith(".nakama-0"):
            path = os.path.join(root, file)

            try:
                df = pd.read_parquet(path)
                all_data.append(df)
            except:
                print("Skipped:", path)

df_all = pd.concat(all_data)

print("Total rows:", len(df_all))

df_all.to_csv("backend/events.csv", index=False)
