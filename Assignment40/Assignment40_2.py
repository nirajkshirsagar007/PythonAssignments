'''
Q2. Remove the column SleepHours from the dataset.
train the model again .
compare new accuracy with previous accuracy.
Does removing this feature affect performance?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

########################################################
# Model 1 : With ALL features
########################################################

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model1 = DecisionTreeClassifier(random_state=42)
model1.fit(X_train, Y_train)

pred1 = model1.predict(X_test)
acc_full = accuracy_score(Y_test, pred1)

print("Accuracy with all features:", acc_full*100)


########################################################
# Model 2 : Remove SleepHours
########################################################

X_new = df.drop(["FinalResult", "SleepHours"], axis=1)

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X_new, Y, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train2, Y_train2)

pred2 = model2.predict(X_test2)
acc_removed = accuracy_score(Y_test2, pred2)

print("Accuracy without SleepHours:", acc_removed*100)


########################################################
# Comparison
########################################################

print("\nAccuracy Difference:", (acc_removed - acc_full)*100)