# Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)

# Step 1: Mean of X and Y
mean_x = sum(X) / n
mean_y = sum(Y) / n

print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)

# Step 2: Calculate slope (m)
num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den

# Step 3: Calculate intercept (c)
c = mean_y - m * mean_x

print("\nSlope (m) =", round(m,2))
print("Intercept (c) =", round(c,2))

# Step 4: Regression equation
print("\nRegression Equation:")
print(f"Y = {round(m,2)}X + {round(c,2)}")

# Step 5: Prediction
x_new = 6
y_pred = m * x_new + c

print("\nPredicted Y for X =", x_new, ":", round(y_pred,2))