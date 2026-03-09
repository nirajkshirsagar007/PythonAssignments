import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdvertiser(DataPath):

    border = "-"*40

    # Step 1: Load Dataset
    print(border)
    print("Step 1: Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print("Some entries from dataset")
    print(df.head())

    print(border)

    # Step 2: Clean Dataset
    print(border)
    print("Step 2: Clean the dataset")
    print(border)

    df.dropna(inplace=True)

    print("Total records:",df.shape[0])
    print("Total columns:",df.shape[1])

    # Step 3: Separate input and output variables
    print(border)
    print("Step 3: Separate independent and dependent variables")
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Input features:")
    print(X.head())

    print("Output feature:")
    print(Y.head())

    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape)

    # Step 4: Split dataset into training and testing (50%)
    print(border)
    print("Step 4: Split dataset into training and testing")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,Y,test_size=0.5,random_state=42)

    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print("Y_train shape:",Y_train.shape)
    print("Y_test shape:",Y_test.shape)

    # Step 5: Train Linear Regression Model
    print(border)
    print("Step 5: Train Linear Regression Model")
    print(border)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    print("Model training completed")

    # Step 6: Test the Model
    print(border)
    print("Step 6: Test the Model")
    print(border)

    Y_pred = model.predict(X_test)

    print("Predicted values")
    print(Y_pred[:10])

    # Step 7: Display expected vs predicted values
    print(border)
    print("Step 7: Expected vs Predicted values")
    print(border)

    result = pd.DataFrame({
        "Actual":Y_test,
        "Predicted":Y_pred
    })

    print(result.head(10))

    # Step 8: Model Performance
    print(border)
    print("Step 8: Model Performance")
    print(border)

    mse = mean_squared_error(Y_test,Y_pred)
    r2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error:",mse)
    print("R2 Score:",r2)

    # Step 9: Plot Graph
    print(border)
    print("Step 9: Plot Graph")
    print(border)

    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual vs Predicted Sales")
    plt.grid(True)
    plt.show()


def main():

    border = "-"*40

    print(border)
    print("Advertising Sales Predictor using Linear Regression")
    print(border)

    MarvellousAdvertiser("Advertising.csv")


if __name__ == "__main__":
    main()