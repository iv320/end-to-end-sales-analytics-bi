import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("sales_clean_superstore.xlsx")

# Basic check
print(df.head())
print(df.columns)

print(df.info())
print(df.describe())

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)

monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

df.to_csv("final_clean_superstore.csv", index=False)

