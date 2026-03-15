import pandas as pd
from sklearn.linear_model import LinearRegression

def MultipleRegression():

    data = {
        "StudyHours":[1,2,3,4,5],
        "SleepHours":[7,6,7,6,8],
        "Marks":[50,55,60,65,70]
    }

    df = pd.DataFrame(data)

    X = df[['StudyHours','SleepHours']]
    Y = df['Marks']

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient for StudyHours :",model.coef_[0])
    print("Coefficient for SleepHours :",model.coef_[1])
    print("Intercept :",model.intercept_)

MultipleRegression()