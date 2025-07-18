import pandas as pd

#load cleaned csv
df = pd.read_csv("data/cleaned_sample.csv")

#convert to json
json_data = df.to_json(orient="records", indent=4)

print(json_data)

with open("data/cleaned_sample.json","w") as f:
    f.write(json_data)