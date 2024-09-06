# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
# X represents the independent variable (e.g., number of study hours)
# y represents the dependent variable (e.g., exam score)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Reshape to make it a 2D array
y = np.array([1, 2, 4, 4, 5])

# Create a linear regression model
model = LinearRegression()

# Train the model (fit the data)
model.fit(X, y)

# Predict using the model
y_pred = model.predict(X)

# Print coefficients
print(f"Slope (Coefficient): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Visualize the data and the fitted line
# .legend() & .show() methods are I/O blocking
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Regression line')
plt.xlabel('Independent Variable (X)')
plt.ylabel('Dependent Variable (y)')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()

# To predict a new value, you can do something like:
new_value = np.array([[6]])  # Predict y for X=6
predicted_value = model.predict(new_value)
print(f"Predicted value for X=6: {predicted_value[0]}")
