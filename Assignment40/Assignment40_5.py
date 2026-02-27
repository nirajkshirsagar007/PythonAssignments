'''
Q5.Without using accuracy_score, manually calculate accuracy:
verify whether it matches sklearn accuracy.
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
# Step 4: Manual Accuracy Calculation
########################################################

correct = 0

for actual, predicted in zip(Y_test, Y_pred):
    if actual == predicted:
        correct += 1

total = len(Y_test)

manual_accuracy = correct / total

print("Manual Accuracy:", manual_accuracy * 100, "%")

########################################################
# Step 5: Verify with sklearn
########################################################

from sklearn.metrics import accuracy_score

sk_accuracy = accuracy_score(Y_test, Y_pred)

print("Sklearn Accuracy:", sk_accuracy * 100, "%")