import pandas as pd

# Load dataset
df = pd.read_csv("../data/Superstore.csv", encoding="latin1")

print("Before cleaning:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna({"Postal Code": 0, "Discount": 0}, inplace=True)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Save cleaned data
df.to_csv("../data/Superstore_clean.csv", index=False)

print("After cleaning:", df.shape)
print("Cleaned data saved as Superstore_clean.csv")
