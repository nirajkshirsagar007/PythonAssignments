'''
Q9. Create a new column:
 PerformanceIndex = (StudyHours * 2) + Attendance
 Train the model including this new feature.
 Does accuracy improve?

'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

########################################################
# Step 1: Load dataset
########################################################

df = pd.read_csv("student_performance_ml.csv")

########################################################
# Step 2: Create new feature (Feature Engineering)
########################################################

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

print("New column added successfully!")

########################################################
# Step 3: Train with ORIGINAL features (baseline)
########################################################

X_old = df.drop("FinalResult", axis=1).drop("PerformanceIndex", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X_old, Y, test_size=0.2, random_state=42
)

model_old = DecisionTreeClassifier(random_state=42)
model_old.fit(X_train, Y_train)

pred_old = model_old.predict(X_test)
old_acc = accuracy_score(Y_test, pred_old)

print("Old Accuracy:", old_acc * 100)

########################################################
# Step 4: Train with NEW feature included
########################################################

X_new = df.drop("FinalResult", axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(
    X_new, Y, test_size=0.2, random_state=42
)

model_new = DecisionTreeClassifier(random_state=42)
model_new.fit(X_train, Y_train)

pred_new = model_new.predict(X_test)
new_acc = accuracy_score(Y_test, pred_new)

print("New Accuracy:", new_acc * 100)

########################################################
# Step 5: Compare
########################################################

if new_acc > old_acc:
    print("Accuracy improved after adding PerformanceIndex")
elif new_acc == old_acc:
    print("Accuracy stayed same")
else:
    print("Accuracy decreased")
