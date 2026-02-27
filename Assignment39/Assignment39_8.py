#################################################################
# Import Libraries
#################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

Border = "-"*50

#################################################################
# Step 1: Load the Dataset
#################################################################
print(Border)
print("Step 1: Load the Dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

print("Dataset loaded successfully")
print(df.head())


#################################################################
# Step 2: Data Analysis (EDA)
#################################################################
print(Border)
print("Step 2: Data Analysis")
print(Border)

print("Shape :", df.shape)
print("Columns :", list(df.columns))
print("Missing values:\n", df.isnull().sum())
print("Final Result Distribution:\n", df["FinalResult"].value_counts())
print(df.describe())


#################################################################
# Step 3: Visualization
#################################################################
print(Border)
print("Step 3: Visualization")
print(Border)

# Histogram of StudyHours
sns.histplot(df["StudyHours"], bins=10, kde=True)
plt.title("Study Hours Distribution")
plt.show()

# Scatter plot (Pass/Fail colored)
sns.scatterplot(x="StudyHours", y="PreviousScore", hue="FinalResult", data=df)
plt.title("StudyHours vs PreviousScore")
plt.show()


#################################################################
# Step 4: Train-Test Split
#################################################################
print(Border)
print("Step 4: Train-Test Split")
print(Border)

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)


#################################################################
# Step 5: Model Training
#################################################################
print(Border)
print("Step 5: Model Training")
print(Border)

model = DecisionTreeClassifier(max_depth=5, random_state=42)

model.fit(X_train, Y_train)

print("Model training completed")


#################################################################
# Step 6: Prediction
#################################################################
print(Border)
print("Step 6: Prediction")
print(Border)

y_pred = model.predict(X_test)

results = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": y_pred
})

print(results.head())


#################################################################
# Step 7: Accuracy Calculation
#################################################################
print(Border)
print("Step 7: Accuracy")
print(Border)

accuracy = accuracy_score(Y_test, y_pred)

print("Testing Accuracy: {:.2f}%".format(accuracy*100))


#################################################################
# Step 8: Confusion Matrix
#################################################################
print(Border)
print("Step 8: Confusion Matrix")
print(Border)

cm = confusion_matrix(Y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.show()


#################################################################
# Step 9: Final Conclusion
#################################################################
print(Border)
print("Step 9: Final Conclusion")
print(Border)

print("Model Accuracy:", accuracy*100, "%")
accuracy_percentage = accuracy*100
if accuracy_percentage > 80:
    print("Model performance is GOOD")
elif accuracy_percentage > 60:
    print("Model performance is AVERAGE")
else:
    print("Model performance is POOR")