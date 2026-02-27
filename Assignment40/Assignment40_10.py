'''
Q10.Train model with:
Max_depth = None
Calculate:
 Training accuracy
 Testing accuracy
 if training accuracy is 100% but testing accuracy is lower, explain why this happens
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

########################################################
# Load dataset
########################################################

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

########################################################
# Train model with max_depth = None
########################################################

model = DecisionTreeClassifier(max_depth=None, random_state=42)

model.fit(X_train, Y_train)

########################################################
# Predictions
########################################################

train_pred = model.predict(X_train)
test_pred  = model.predict(X_test)

########################################################
# Manual accuracy (no sklearn)
########################################################

train_acc = (train_pred == Y_train).sum() / len(Y_train)
test_acc  = (test_pred  == Y_test).sum()  / len(Y_test)

print("Training Accuracy :", train_acc * 100)
print("Testing Accuracy  :", test_acc * 100)
