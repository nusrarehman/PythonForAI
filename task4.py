import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([2, 4, 6, 8, 10])


reg = LinearRegression().fit(X, Y)

y_pred = reg.predict([[10]])
print("Predicted value when x=10:", y_pred[0])


plt.scatter(X, Y, c="blue", label="Data Points")
plt.plot(X, reg.predict(X), c="red", label="Regression Line")
plt.scatter(10, y_pred, c="green", marker="x", s=100, label="Prediction (x=10)")
plt.title("Linear Regression Demo")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.show()