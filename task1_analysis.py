import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())
print(os.listdir())
                                        # STEP 1: Load cleaned dataset
df = pd.read_csv("cleaned_online_retail.csv")

# Convert InvoiceDate to datetime (with error handling)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Remove rows where date conversion failed
df = df.dropna(subset=['InvoiceDate'])

# STEP 2: Create time features
df['Month'] = df['InvoiceDate'].dt.to_period('M')
df['Year'] = df['InvoiceDate'].dt.year

# STEP 3: Revenue Trends (Monthly)
monthly_revenue = df.groupby('Month')['Revenue'].sum().reset_index()

# Sort by Month (important for correct graph)
monthly_revenue = monthly_revenue.sort_values('Month')

print("\nMonthly Revenue:\n", monthly_revenue)

# Plot Monthly Revenue
plt.figure(figsize=(10,5))
plt.plot(monthly_revenue['Month'].astype(str), monthly_revenue['Revenue'])
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# STEP 4: Top-Selling Products
top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:\n", top_products)

# STEP 5: Regional Performance (Country)
country_sales = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)
print("\nTop Countries:\n", country_sales.head(10))

# STEP 6: High-Value Customers
top_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop Customers:\n", top_customers)

# STEP 7: Save outputs for dashboard
monthly_revenue.to_csv("monthly_revenue.csv", index=False)
top_products.to_csv("top_products.csv")
country_sales.to_csv("country_sales.csv")
top_customers.to_csv("top_customers.csv")

print("\n✅ Analysis completed and files saved successfully")