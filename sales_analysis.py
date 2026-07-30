import pandas as pd

# Load the dataset
df = pd.read_csv("data/sales.csv")

# Display the first 5 rows
print("===== E-Commerce Sales Dataset =====")
print(df.head())

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales: ₹", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit: ₹", total_profit)

# Total Orders
total_orders = len(df)
print("Total Orders:", total_orders)

# Average Sales
average_sales = df["Sales"].mean()
print("Average Sales: ₹", round(average_sales, 2))

# Best Selling Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category")
print(category_sales)
best_category = category_sales.idxmax()
print("\nBest Selling Category:", best_category)

import matplotlib.pyplot as plt

# Bar Chart - Sales by Category
category_sales.plot(kind="bar", figsize=(8,5), color="skyblue")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

# Save the graph
plt.savefig("images/sales_by_category.png")
# Show the graph
plt.show()

# Pie Chart - Profit by Category

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    category_profit,
    labels=category_profit.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Profit by Category")

plt.savefig("images/profit_pie_chart.png")

plt.show()

# Monthly Sales Line Chart

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.savefig("images/monthly_sales.png")

plt.show()

# Histogram - Sales Distribution

plt.figure(figsize=(8,5))

plt.hist(
    df["Sales"],
    bins=5,
    edgecolor="black"
)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.savefig("images/sales_histogram.png")

plt.show()

# Region-wise Sales

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.savefig("images/region_sales.png")

plt.show()