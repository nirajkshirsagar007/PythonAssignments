'''
Q6. Identify students where:

y_test != y_pred
Diaplay those rows
how many students were misclassified?
what common pattern do you observe?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

########################################################
# Step 1: Load and train model FIRST
########################################################

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)


model.fit(X_train, Y_train)

########################################################
# Step 3: Predict on TEST data (for accuracy)
########################################################

Y_pred = model.predict(X_test)
########################################################
# Step 4: Combine test data with predictions
########################################################

results = X_test.copy()

results["Actual"] = Y_test.values
results["Predicted"] = Y_pred

########################################################
# Step 5: Filter misclassified rows
########################################################

misclassified = results[results["Actual"] != results["Predicted"]]

print("Misclassified Students:")
print(misclassified)

########################################################
# Step 6: Count mistakes
########################################################

print("\nTotal Misclassified:", len(misclassified))