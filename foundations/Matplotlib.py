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

'''
Create a “Student Performance Dashboard”:

Generate random student data:Marks,Study hours,Attendance
Visualize:
Histogram of marks
Scatter (study hours vs marks)
Bar chart (attendance categories) '''

# Generate random student data:
np.random.seed(42)
Marks=np.random.randint(40,98,10)
Study_Hours = np.random.randint(1,12.5 , 10)
categories =['Present','Absent','Late','Leave']
Attendence = np.random.randint(0,100,size=len(categories))
    
# Histogram of Marks
plt.subplot(1,3,1)
plt.hist(Marks, bins=10, edgecolor='black') 
plt.xlabel('Marks')
plt.ylabel('Distribution')
plt.title('Marks distribution')

# Scatter Graph (Study Hours VS Marks)
plt.subplot(1,3,2)
plt.scatter(Study_Hours,Marks)
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study_Hours and Marks ')

#Attendence Bar Chart
plt.subplot(1,3,3)
plt.bar(categories, Attendence, color=['red','blue','green','orange','gray'] )
plt.xlabel('Attendence Category')
plt.ylabel('Count')
plt.title('Attendence Summary')

plt.suptitle("Student Dashboard")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()