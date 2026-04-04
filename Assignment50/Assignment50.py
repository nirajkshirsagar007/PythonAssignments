import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("bank-full.csv", sep=";")

# Show first rows
print(df.head())

# Dataset info
print(df.info())

# Count missing/unknown values
print(df.isnull().sum())

# Replace 'unknown' values
df = df.replace("unknown", np.nan)
print(df.isnull().sum())

# Fill missing values using mode
df = df.fillna(df.mode().iloc[0])

# Visualize target class distribution
sns.countplot(x=df['y'])
plt.title("Target Class Distribution (Subscribed vs Not Subscribed)")
plt.show()
# ------------------------
# PREPROCESSING FIXED
# ------------------------

# Label Encoding categorical columns
categorical_cols = df.select_dtypes(include=['object', 'string']).columns

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Split X and y BEFORE SCALING
X = df.drop("y", axis=1)
y = df["y"]

# Scale only X numeric columns
numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns

scaler = StandardScaler()
X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

log_model = LogisticRegression(max_iter=2000)
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)
log_prob = log_model.predict_proba(X_test)[:, 1]

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_pred = knn_model.predict(X_test)
knn_prob = knn_model.predict_proba(X_test)[:, 1]

rf_model = RandomForestClassifier(n_estimators=200)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_prob = rf_model.predict_proba(X_test)[:, 1]

# Evaluate Models
def evaluate_model(y_test, y_pred, y_prob, model_name):
    print("\n==============================")
    print(f" MODEL: {model_name}")
    print("==============================")
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))

    # Plot Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"{model_name} - Confusion Matrix")
    plt.show()

    # Plot ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.title(f"{model_name} - ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.show()

evaluate_model(y_test, log_pred, log_prob, "Logistic Regression")
evaluate_model(y_test, knn_pred, knn_prob, "K-Nearest Neighbors")
evaluate_model(y_test, rf_pred, rf_prob, "Random Forest Classifier")