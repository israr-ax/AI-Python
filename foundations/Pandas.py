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

'''
    Converting Pandas → NumPy
'''
# Create DataFrame
data = {
    "Experience": [1,2,3,4,5,6],
    "Hours_Studied": [2,4,5,8,10,6],
    "Pass": [0,0,1,1,1,6]
}
df=pd.DataFrame(data)
print(df)

# Separate X and y
X=df[["Experience","Hours_Studied"]]
Y=df["Pass"]

# Convert to NumPy
X=X.values
Y=Y.values
print(type(X))
print(type(Y))

# Print shapes
print(X.shape)
print(Y.shape)

'''
Create a dataset of:Student Name Study Hours Sleep Hours Pass (0/1)
Then:
Handle missing values (if any)
Select features only numeric
Convert to NumPy
Print shape

'''
# Create a dataset of:Student Name Study Hours Sleep Hours Pass (0/1)
data={
    "Name":['Israr','Dheeraj','Pawan','Aman'],
    'Study Hours':[None,3,6,8],
    'Sleep Hours':[12,9,8,15],
    'Pass':[0,1,0,1]
}
df=pd.DataFrame(data)
print(df)

# Handle missing values (if any)
print("Detect missing values\n",df.isnull())
df['Study Hours']=df['Study Hours'].fillna(df['Study Hours'].mean())
print("Handle missing values\n",df)

# Select features only numeric
''' X=Input(Features)
    Y=Output (Label)
'''
X=df[['Study Hours','Sleep Hours']]  
y= df['Pass']

# Convert to NumPy
X=X.values
y=y.values
print(f"Convert from Pandas To Numpy\n {type(X)} , {type(y)}")

# Print shape
print(X.shape)
print(y.shape)