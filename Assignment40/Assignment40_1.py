'''
Q1. After training the Decision Tree model, use:
model.feature_importances_
Diaplay importance score of each feature.
which feature contributes the most in predicting FinalResult?
Which Feature contributes the least?
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Step 1: Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Step 2: Split features and target
X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

# Step 3: Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Step 4: Create and train model 
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

# Step 5: Get feature importances
importances = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
})

importance_df = importance_df.sort_values(by="Importance", ascending=False)

print(importance_df)