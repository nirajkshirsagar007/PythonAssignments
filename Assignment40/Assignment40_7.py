'''
Q7. Train model using:
random_state = 0
random_state = 10 
random_state = 42
Compare testing accuracy.
Does the result change?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

########################################################
# Load dataset
########################################################

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

states = [0, 10, 42]

print("Testing accuracy for different random states:\n")

for state in states:

    # split
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=state
    )

    # model
    model = DecisionTreeClassifier(random_state=state)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    acc = accuracy_score(Y_test, Y_pred)

    print(f"random_state = {state}  →  Accuracy = {acc*100:.2f}%")