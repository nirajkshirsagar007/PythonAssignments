'''
Q3. Train the model using only:
StudyHours
Attandance
compare the accuracy with full-feature model.
is the model still performing well?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

########################################################
# Model 1 : Full features
########################################################

X_full = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X_full, Y, test_size=0.2, random_state=42
)

model_full = DecisionTreeClassifier(random_state=42)
model_full.fit(X_train, Y_train)

pred_full = model_full.predict(X_test)
acc_full = accuracy_score(Y_test, pred_full)

print("Accuracy (Full features): {:.2f}%".format(acc_full*100))


########################################################
# Model 2 : Only StudyHours & Attendance
########################################################

X_small = df[["StudyHours", "Attendance"]]

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X_small, Y, test_size=0.2, random_state=42
)

model_small = DecisionTreeClassifier(random_state=42)
model_small.fit(X_train2, Y_train2)

pred_small = model_small.predict(X_test2)
acc_small = accuracy_score(Y_test2, pred_small)

print("Accuracy (Only 2 features): {:.2f}%".format(acc_small*100))


########################################################
# Comparison
########################################################

print("Accuracy Difference: {:.2f}%".format((acc_full - acc_small)*100))