import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("../data/retail.db")
cursor = conn.cursor()

# Dictionary of queries
queries = {
    "Total Sales": """
        SELECT ROUND(SUM(Sales),2) AS TotalSales FROM orders
    """,

    "Total Profit": """
        SELECT ROUND(SUM(Profit),2) AS TotalProfit FROM orders
    """,

    "Total Orders": """
        SELECT COUNT(DISTINCT [Order ID]) AS TotalOrders FROM orders
    """,

    "Top 5 Products by Sales": """
        SELECT [Product Name], ROUND(SUM(Sales),2) AS TotalSales
        FROM orders
        GROUP BY [Product Name]
        ORDER BY TotalSales DESC
        LIMIT 5
    """,

    "Sales by Region": """
        SELECT Region, ROUND(SUM(Sales),2) AS TotalSales
        FROM orders
        GROUP BY Region
        ORDER BY TotalSales DESC
    """,

    "Profit by Category": """
        SELECT Category, ROUND(SUM(Profit),2) AS TotalProfit
        FROM orders
        GROUP BY Category
        ORDER BY TotalProfit DESC
    """,

    "Monthly Sales Trend": """
        SELECT strftime('%Y-%m', [Order Date]) AS Month,
               ROUND(SUM(Sales),2) AS TotalSales
        FROM orders
        GROUP BY Month
        ORDER BY Month
    """,

    "Top 5 Customers by Sales": """
        SELECT [Customer Name], ROUND(SUM(Sales),2) AS TotalSales
        FROM orders
        GROUP BY [Customer Name]
        ORDER BY TotalSales DESC
        LIMIT 5
    """,

    "Discount Impact": """
        SELECT ROUND(AVG(Discount),2) AS AvgDiscount,
               ROUND(AVG(Profit),2) AS AvgProfit
        FROM orders
    """,

    "Ship Mode Preference": """
        SELECT [Ship Mode], COUNT(*) AS Orders
        FROM orders
        GROUP BY [Ship Mode]
        ORDER BY Orders DESC
    """
}

# Run queries
for name, q in queries.items():
    print(f"\n{name}:")
    for row in cursor.execute(q):
        print(row)

conn.close()
