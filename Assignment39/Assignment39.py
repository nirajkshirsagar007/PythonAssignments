import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


'''
Q1. Import DecesionTreeClassifier from sklearn.
Create a model object and train it using fit()
'''

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult",axis=1)

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state= 42
)

print("Model successfully created: ",model)

model.fit(X_train,Y_train)
print("model training completed")

'''
Q2. Use the trained model to predict results for X_test.
Display predicted values along with actual values.
'''
y_pred = model.predict(X_test)

results = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": y_pred
})
print(results)

'''
Q3.Calculate model accuracy using accuracy_score.
Display the result in percentage format.
'''
accuracy = accuracy_score(Y_test,y_pred)

print("Model Accuracy:{:.2f}% ".format(accuracy * 100))

'''
Q4. Generate confusion matrix using sklearn.
Display it using ConfusionMatrixDisplay.

Explain clearly:
True Positive
True Negative
False Positive
False Negative

'''
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Generate confusion matrix
cm = confusion_matrix(Y_test, y_pred)

print("Confusion Matrix:\n", cm)

# Display graphically
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

plt.show()

'''
Q5. Calculate:

Training accuracy
Testing accuracy

compare both and comment whether the model is overfitting or underfitting.
'''

# Training accuracy
train_pred = model.predict(X_train)
train_acc = accuracy_score(Y_train, train_pred)
print("Training Accuracy : {:.2f}%".format(train_acc * 100))

# Testing accuracy
test_pred = model.predict(X_test)
test_acc = accuracy_score(Y_test, test_pred)

print("Testing Accuracy  : {:.2f}%".format(test_acc * 100))

'''
Q6.Train three Decision tree models with:

max_depth = 1
max_depth = 3
max_depth = None
compare there testing accuracies and write your observations. 
'''
depths = [1, 3, None]

for d in depths:
    
    # Create model with different depth
    model = DecisionTreeClassifier(max_depth=d, random_state=42)
    
    # Train
    model.fit(X_train, Y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Accuracy
    acc = accuracy_score(Y_test, y_pred)
    
    print(f"Max Depth = {d}  --> Testing Accuracy = {acc*100:.2f}%")

    '''
    Q7. Use the trained model to predict result for a student with:

    StudyHours = 6
    Attendance = 85
    PreviousScore = 66
    AssignmentsCompleted = 7
    SleepHours = 7
    will the student Pass or Fail?
    '''

    new_student = pd.DataFrame([{
    "StudyHours": 6,
    "Attendance": 85,
    "PreviousScore": 66,
    "AssignmentsCompleted": 7,
    "SleepHours": 7
}])

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Result: PASS")
else:
    print("Result: FAIL")

'''
Q8. Write a single structured Python program that performs:
1. Dataset loading
2. Data analysis
3. Visualisation
4. Train-test split
5. Model training
6. Prediction
7. Accuracy calculation
8. Confusion matrix generation 
9. Final conculation

Your code should include proper comments explaining each step.
'''
    