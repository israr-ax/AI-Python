import numpy as np
import matplotlib.pyplot as plt

# Generate linear data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# Add bias term
X_b = np.c_[np.ones((100,1)), X]  # Add x0 = 1

# Gradient Descent parameters
theta = np.random.randn(2,1)  # initial weights
alpha = 0.1
n_iterations = 1000
m = 100

# Gradient Descent Loop
for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - alpha * gradients

print("Learned parameters (intercept, slope):", theta.ravel())

# Plot predictions
plt.scatter(X, y)
plt.plot(X, X_b.dot(theta), color='red')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression with Gradient Descent")
plt.show()