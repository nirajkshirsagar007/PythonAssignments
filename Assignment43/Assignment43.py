import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score



def PlayPredictor(DataPath):
    border = "-"*40

    # step1: load the dataset from csv file.
    print(border)
    print("Step 1: Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)
    print("Some entries from dataset")
    print(df.head())
    print(border)
    # remove index column if present
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    print(border)
    print("Dataset after removing index column")
    print(df.head())

    # Step 2: Clean and prepare dataset
    print(border)
    print("Step 2 : Data Cleaning")
    print(border)

    df.dropna(inplace=True)

    print("Total rows :",df.shape[0])
    print("Total columns :",df.shape[1])

    # convert string to numeric using LabelEncoder
    print(border)
    print("Applying Label Encoding")
    print(border)

    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df['Whether'] = le_weather.fit_transform(df['Whether'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    print("Encoded Dataset")
    print(df.head())

    # Step 3: Train Data
    print(border)
    print("Step 3 : Train Data using KNN")
    print(border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("Input features")
    print(X.head())

    print("Output feature")
    print(Y.head())

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)

    print("Training completed using full dataset")

    # Step 4: Test Data
    print(border)
    print("Step 4 : Testing the model")
    print(border)

    # Example test input
    weather = "Sunny"
    temp = "Cool"

    w = le_weather.transform([weather])
    t = le_temp.transform([temp])

    prediction = model.predict([[w[0],t[0]]])

    result = le_play.inverse_transform(prediction)

    print("Weather :",weather)
    print("Temperature :",temp)
    print("Prediction :",result[0])

    # Step 5: Accuracy calculation
    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of algorithm :",accuracy*100,"%")

def main():
    border = "-"*40

    print(border)
    print("Play Predictor using KNN")
    print(border)

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()