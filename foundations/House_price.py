import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionScratch:
    def __init__(self, lr=0.0000001, epochs=200):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.losses = []

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            # Prediction
            y_pred = np.dot(X, self.weights) + self.bias

            # Compute Loss (MSE)
            loss = np.mean((y - y_pred) ** 2)
            self.losses.append(loss)

            # Compute Gradients
            dw = (2 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (2 / n_samples) * np.sum(y_pred - y)

            # Update Parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            # Optional: Print progress
            if epoch % 20 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


# -----------------------------
# Small House Price Dataset
# -----------------------------
# Feature: House size (sq ft)
X = np.array([
    [500],
    [800],
    [1000],
    [1200],
    [1500],
    [1800]
])

# Target: Price (in thousands)
y = np.array([50, 80, 100, 120, 150, 180])


# -----------------------------
# Train Model
# -----------------------------
model = LinearRegressionScratch(lr=0.0000001, epochs=200)
model.fit(X, y)

# Predictions
predictions = model.predict(X)

print("\nFinal Weights:", model.weights)
print("Final Bias:", model.bias)


# -----------------------------
# Plot Loss Curve
# -----------------------------
plt.subplot(1,2,1)
plt.plot(model.losses)
plt.title("Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")


# -----------------------------
# Plot Predicted vs Actual
# -----------------------------
plt.subplot(1,2,2)
plt.scatter(y, predictions)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Predicted vs Actual")

# Perfect prediction line
plt.plot([min(y), max(y)],
         [min(y), max(y)])

plt.suptitle("House Price Prdictions")
plt.tight_layout()
plt.show()