import pandas as pd

melbourne_file_path = "melb_data.csv"
melbourne_data = pd.read_csv("")

print(melbourne_data.columns)
print(melbourne_data)

melbourne_data = melbourne_data.dropna(axis=0)
