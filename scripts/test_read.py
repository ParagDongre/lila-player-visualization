import pandas as pd

file_path = "data/player_data/February_10/0019c582-574d-4a53-9f77-554519b75b4c_1298e3e2-2776-4038-ba9b-72808b041561.nakama-0"

df = pd.read_parquet(file_path)

print(df.head())
print("\nColumns:")
print(df.columns)
