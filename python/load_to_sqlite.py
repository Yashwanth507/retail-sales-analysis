import sqlite3
import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/Superstore_clean.csv")

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("../data/retail.db")
cursor = conn.cursor()

# Write dataframe to SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

# Verify row count
cursor.execute("SELECT COUNT(*) FROM orders")
print("Rows in table:", cursor.fetchone()[0])

conn.commit()
conn.close()
