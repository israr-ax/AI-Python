import pandas as pd 
#Create a data table then perform basic statistics
data = {
    "Name" : ["AHMED", "ISRAR","ALI","TURAB"],
    "Age":[21,22,18,17],
    "Marks": [88,98,90,89]
}
df=pd.DataFrame(data)
print(df)

print("Average Marks",df['Marks'].mean())
print("Max marks",df["Marks"].max())
print(df.describe())

'''Create a DataFrame with: Product,Price ,Quantity

Find average price Filter products with price > 500

Add new column: Total = Price * Quantity '''

# Create a DataFrame with: Product,Price ,Quantity
data={
    'Product': ['Soap', 'Facewash', 'Detergent', 'Shampoo'],
    'Price' :  [210,450,550,870],
    'Quantity': [6,5,3,12]
}
df=pd.DataFrame(data)
print(df)
# Find average price and  Filter products with price > 500
print(f"Average Price:{df['Price'].mean()} \nFilter products with price:\n{df[df['Price']>300]}")

# Add new column: Total = Price * Quantity
df['TOTAL'] = df['Price'] * df['Quantity']
print(df)


'''Create a DataFrame with:
Product Price Quantity (one missing value)
Then:
Detect missing values
Fill with mean
Print cleaned DataFrame '''

# '''Create a DataFrame with: Product Price Quantity 
data={
    'Product': ['Soap', 'Facewash', 'Detergent', 'Shampoo'],
    'Price' :  [210,450,None,870],
    'Quantity': [6,None,3,12]
}
df=pd.DataFrame(data)
print(df)

# Detect missing values
print(f"Detect missing values:\n {df.isnull()}")

# Fill with mean
df.fillna({
    'Price': df['Price'].mean(),
    'Quantity': df['Quantity'].mean()
}, inplace=True)

# Print cleaned DataFrame
print(f"Fill mising values:\n{df}")