import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to database
conn = sqlite3.connect("../data/retail.db")

# 1. Sales by Region
region_df = pd.read_sql_query("""
    SELECT Region, ROUND(SUM(Sales),2) AS TotalSales
    FROM orders
    GROUP BY Region
    ORDER BY TotalSales DESC
""", conn)

plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="TotalSales", data=region_df, palette="viridis")
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.show()

# 2. Profit by Category
category_df = pd.read_sql_query("""
    SELECT Category, ROUND(SUM(Profit),2) AS TotalProfit
    FROM orders
    GROUP BY Category
    ORDER BY TotalProfit DESC
""", conn)

plt.figure(figsize=(6,5))
sns.barplot(x="Category", y="TotalProfit", data=category_df, palette="coolwarm")
plt.title("Profit by Category")
plt.ylabel("Total Profit")
plt.show()

# 3. Monthly Sales Trend
monthly_df = pd.read_sql_query("""
    SELECT strftime('%Y-%m', [Order Date]) AS Month,
           ROUND(SUM(Sales),2) AS TotalSales
    FROM orders
    GROUP BY Month
    ORDER BY Month
""", conn)

plt.figure(figsize=(12,5))
sns.lineplot(x="Month", y="TotalSales", data=monthly_df, marker="o", color="blue")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.ylabel("Total Sales")
plt.show()

# 4. Top 5 Products
products_df = pd.read_sql_query("""
    SELECT [Product Name], ROUND(SUM(Sales),2) AS TotalSales
    FROM orders
    GROUP BY [Product Name]
    ORDER BY TotalSales DESC
    LIMIT 5
""", conn)

plt.figure(figsize=(10,5))
sns.barplot(x="TotalSales", y="Product Name", data=products_df, palette="magma")
plt.title("Top 5 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.show()

# 5. Ship Mode Preference
ship_df = pd.read_sql_query("""
    SELECT [Ship Mode], COUNT(*) AS Orders
    FROM orders
    GROUP BY [Ship Mode]
    ORDER BY Orders DESC
""", conn)

plt.figure(figsize=(6,6))
plt.pie(ship_df["Orders"], labels=ship_df["Ship Mode"], autopct='%1.1f%%', startangle=140)
plt.title("Ship Mode Preference")
plt.show()

conn.close()
