import numpy as np
import matplotlib.pyplot as plt

# dataset
x = np.array([1,2,3,4,5])
y = np.array([20000,25000,30000,35000,40000])

# calculate slope and intercept
x_mean = np.mean(x)
y_mean = np.mean(y)

m = np.sum((x-x_mean)*(y-y_mean)) / np.sum((x-x_mean)**2)
c = y_mean - m*x_mean

# prediction
y_pred = m*x + c

# predict salary for 6 years
salary_6 = m*6 + c
print("Predicted Salary for 6 years:", salary_6)

# plot
plt.scatter(x,y,label="Data Points")
plt.plot(x,y_pred,label="Regression Line")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()