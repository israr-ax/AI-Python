import matplotlib.pyplot as plt
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
plt.scatter(x,y)
plt.show()

