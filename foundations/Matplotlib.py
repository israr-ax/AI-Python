import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

# Line plot
x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y)
plt.show()

# Bar Plot
plt.bar(["A","B","C"], [5,7,3])
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.show()

# Plot a line chart of numbers 1–10 vs their squares.
x = [1,2,3,4,5,6,7,8,9,10]
y = [x**2 for x in x]

plt.plot(x, y)
plt.xlabel("Chart of Numbers")
plt.ylabel("Squares of Numbers")
plt.scatter(x,y)
plt.show()

# Create a bar chart for 5 subjects and their marks.
X=["OOP","PF","DSA","CN","OS"]
Y=[33,57,87,43,66]
plt.bar(X,Y, color=['red','blue','green','orange','gray'])
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()


'''
Create random salary data (100 values).

Plot histogram.

Identify if data looks skewed. '''

# Generate random salary data.
np.random.seed(40)
salary=np.random.randint(30000,150000,100)

#Plot Histogram 
plt.hist(salary, bins=10, edgecolor='black')
plt.xlabel("Salay")
plt.ylabel("Distribution")
plt.title("Salary Distribution")
plt.show()

# Check Skewed
salary=pd.Series(salary)
print("Skewness of data :" , salary.skew())
