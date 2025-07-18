import pandas as pd

#load CSV file
df = pd.read_csv("data/sample.csv")

#print original shape
print("Original shape:", df.shape)  

#drop rows with any missing values
cleaned_df = df.dropna()

#print cleaned shape
print("Cleaned shape:", cleaned_df.shape)

#preview cleaned data
print("\nCleaned data:")
print(cleaned_df)

cleaned_df.to_csv("data/cleaned_sample.csv", index=False)