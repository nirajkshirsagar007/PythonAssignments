'''
Q8.Decision Tree Visualization
use:
from sklearn.tree import plot_tree
Visualise the trained decision tree.
which feature appears at the roo node?
why do you think that feature was selected first?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

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

plt.figure(figsize=(14,8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Decision Tree - Student Performance")
plt.show()
