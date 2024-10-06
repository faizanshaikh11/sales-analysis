import pandas as pd

# Load the data
data = pd.read_csv(r"E:\archive (1)\data.csv", encoding='ISO-8859-1')

# Display the first few rows
print(data.head())

# Get a summary of the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Check for duplicate entries
duplicates = data.duplicated().sum()
print(f'Duplicate entries: {duplicates}')

# If needed, remove duplicates
data = data.drop_duplicates()

print(data)

# Calculate total sales per transaction
data = pd.read_csv(r"E:\archive (1)\data.csv", encoding='ISO-8859-1')
data.describe
data['TotalSales'] = data['UnitPrice'] * data['Quantity']

# Group by country and sum sales
country_sales = data.groupby('Country')['TotalSales'].sum().reset_index()

# Sort the results
country_sales = country_sales.sort_values(by='TotalSales', ascending=False)

# Display top 10 countries by sales
print(country_sales.head(10))

# Optional: Visualize the results using a bar chart
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(country_sales['Country'][:10], country_sales['TotalSales'][:10], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.title('Top 10 Countries by Total Sales')
plt.xticks(rotation=45)
plt.show()# Top 10 products by quantity sold
top_products = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("Top 10 Best-Selling Products:")
print(top_products)
import seaborn as sns

# Visualization
plt.figure(figsize=(12,6))
#sns.scatterplot(data=df, x='x_column', y='y_column', hue='y_column', palette='color_palette', legend=False)

sns.barplot(x=top_products.values, y=top_products.index, hue=top_products.index, palette='viridis',legend=False)
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product Description')
plt.title('Top 10 Best-Selling Products')
plt.show()
#low sales produt


# Identify products with low sales volume
low_sales = data.groupby('Description')['Quantity'].sum().sort_values(ascending=True).head(10)
print("Top 10 Slow-Moving Products:")
print(low_sales)
import matplotlib.pyplot as plt
import seaborn as sns
# Visualization
plt.figure(figsize=(12,6))
sns.barplot(x=low_sales.values, y=low_sales.index,hue=low_sales.index, palette='pastel')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product Description')
plt.title('Top 10 Slow-Moving Products')
plt.show()

# Recommendations
print("\nRecommendations:")
print("Consider promotions, discounts, or discontinuation for slow-moving products to free up inventory space.")


# Identify products with high sales volume
data.describe
data.columns
a = data["Description"].isnull()
high_sales_sales = data.groupby('Description')['Quantity']
high_sales = top_products[top_products > top_products.quantile(0.75)]
print("High Sales Products:")
print(high_sales)

# Recommendations
print("\nRecommendations:")
print("Ensure sufficient stock levels for high-selling products to prevent stockouts.")

# Number of purchases per customer
purchase_counts = customer_stats['NumPurchases']

# Plotting the distribution
plt.figure(figsize=(10,6))
sns.histplot(purchase_counts, bins=50, kde=False, color='green')
plt.title('Distribution of Number of Purchases per Customer')
plt.xlabel('Number of Purchases')
plt.ylabel('Number of Customers')
plt.show()

# Identifying repeat customers
repeat_customers = customer_stats[customer_stats['NumPurchases'] > 1]
print(f"Number of Repeat Customers: {repeat_customers.shape[0]}")

# Visualization: Repeat vs New Customers
labels = ['New Customers', 'Repeat Customers']
sizes = [df['CustomerID'].nunique() - repeat_customers.shape[0], repeat_customers.shape[0]]
colors = ['#ff9999','#66b3ff']
plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('New vs Repeat Customers')
plt.axis('equal')
plt.show()
