import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix, classification_report, 
                             roc_curve, roc_auc_score, ConfusionMatrixDisplay)


df = pd.read_csv("diabetes.csv")

print(df.head())

print("\n--- Column Info ---")
print(df.info())

print("\n--- Null Values Check ---")
print(df.isnull().sum())

print("\n--- Descriptive Statistics ---")
print(df.describe())

plt.figure(figsize=(6, 4))
sns.countplot(x='Outcome', data=df, palette='viridis')
plt.title('Distribution of Outcome (0: Non-Diabetic, 1: Diabetic)')
plt.show()
# Histogram for Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], kde=True, color='blue')
plt.title('Age Distribution')
plt.show()

# Step 2.1: Handle zeros (replace with median)
cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in cols_with_zeros:
    df[col] = df[col].replace(0, df[col].median())

# Step 2.2: Split Features and Target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Step 2.3: Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2.4: Feature Scaling (crucial for models like Logistic Regression)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Step 3.1: Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 3.2: Make predictions
y_pred = model.predict(X_test)

# Step 3.3: Evaluation
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))



# 1. Generate predictions and probabilities
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# 2. Print numeric metrics
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
print(f"ROC AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 3. Visualize Confusion Matrix
ConfusionMatrixDisplay.from_predictions(y_test, y_pred, 
                                        display_labels=['Non-Diabetic', 'Diabetic'], 
                                        cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# 4. Plot ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc_score(y_test, y_pred_proba):.2f})')
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
