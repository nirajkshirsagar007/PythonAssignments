import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):

    border = "-"*40

    # Step 1: Load dataset
    print(border)
    print("Step 1: Load dataset")
    print(border)

    df = pd.read_csv(DataPath)

    print("Dataset preview")
    print(df.head())

    # Step 2: Clean dataset
    print(border)
    print("Step 2: Clean dataset")
    print(border)

    df.dropna(inplace=True)

    print("Total rows:", df.shape[0])
    print("Total columns:", df.shape[1])

    # Step 3: Separate input and output
    print(border)
    print("Step 3: Separate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Input features:", X.columns.tolist())
    print("Output feature: Class")

    print("Shape of X:", X.shape)
    print("Shape of Y:", Y.shape)

    # Step 4: Split dataset
    print(border)
    print("Step 4: Split dataset")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y)

    print("X_train:", X_train.shape)
    print("X_test:", X_test.shape)
    print("Y_train:", Y_train.shape)
    print("Y_test:", Y_test.shape)

    # Step 5: Feature scaling
    print(border)
    print("Step 5: Feature scaling")
    print(border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Scaling completed")

    # Step 6: Try multiple K values
    accuracy_scores = []
    K_values = range(1, 21)

    print(border)
    print("Step 6: Accuracy for different K values")
    print(border)

    for k in K_values:

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train_scaled, Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(accuracy)

        print("K =", k, "Accuracy =", accuracy)

    # Step 7: Plot graph
    print(border)
    print("Step 7: Plot K vs Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores, marker='o')

    plt.title("K value vs Accuracy")
    plt.xlabel("K Value")
    plt.ylabel("Accuracy")

    plt.grid(True)
    plt.show()

    # Step 8: Best K value
    print(border)
    print("Step 8: Find Best K")
    print(border)

    best_k = K_values[accuracy_scores.index(max(accuracy_scores))]

    print("Best K value:", best_k)

    # Step 9: Train final model
    print(border)
    print("Step 9: Train final model")
    print(border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)

    final_model.fit(X_train_scaled, Y_train)

    Y_pred = final_model.predict(X_test_scaled)

    # Step 10: Final accuracy
    print(border)
    print("Step 10: Final Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Final Accuracy:", accuracy*100)

    # Step 11: Confusion matrix
    print(border)
    print("Step 11: Confusion Matrix")
    print(border)

    cm = confusion_matrix(Y_test, Y_pred)

    print(cm)

    # Step 12: Classification report
    print(border)
    print("Step 12: Classification Report")
    print(border)

    print(classification_report(Y_test, Y_pred))


def main():

    border = "-"*40

    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()