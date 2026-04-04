import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Boxplot for Glucose vs Outcome
plt.figure(figsize=(8, 5))
sns.boxplot(x='Outcome', y='Glucose', data=df)
plt.title('Glucose Levels by Outcome')
plt.show()

# Pairplot to see relationships between multiple variables
# (Using a subset for clarity)
sns.pairplot(df[['Glucose', 'BMI', 'Age', 'Outcome']], hue='Outcome')
plt.show()

