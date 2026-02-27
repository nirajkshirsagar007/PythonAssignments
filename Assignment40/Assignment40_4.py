'''
Q4. Create a new Dataframe with details of 5 new students.
use the trained model to predict their results.
Display predictions clearly.
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
# Step 2: Create new students
########################################################

new_students = pd.DataFrame({
    "StudyHours": [6, 2, 8, 4, 5],
    "Attendance": [85, 55, 95, 60, 75],
    "PreviousScore": [66, 40, 88, 50, 70],
    "AssignmentsCompleted": [7, 2, 9, 3, 6],
    "SleepHours": [7, 5, 8, 6, 7]
})


########################################################
# Step 3: Predict
########################################################

predictions = model.predict(new_students)

new_students["PredictedResult"] = predictions

print(new_students)