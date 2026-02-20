'''
Build Your First End-to-End ML Pipeline
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create dataset
data = {
    "Hours_Studied": [9,2,3,4,5,6,7,8],
    "Marks": [35,40,50,60,65,70,80,90]
}

df = pd.DataFrame(data)

# Step 2: Separate features and target
X = df[["Hours_Studied"]]
y = df["Marks"]

# Step 3: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 4: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict
y_pred = model.predict(X_test)
print(y_pred)
# Step 6: Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2:", r2)
