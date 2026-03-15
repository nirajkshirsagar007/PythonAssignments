import pandas as pd
from sklearn.linear_model import LinearRegression

def StudyRegression():

    # Dataset
    data = {
        "StudyHours":[1,2,3,4,5],
        "Marks":[50,55,60,65,70]
    }

    df = pd.DataFrame(data)

    X = df[['StudyHours']]
    Y = df['Marks']

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient :",model.coef_[0])
    print("Intercept :",model.intercept_)

StudyRegression()