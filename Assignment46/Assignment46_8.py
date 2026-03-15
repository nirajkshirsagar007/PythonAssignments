import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "StudyHours":[1,2,3,4,5],
    "Marks":[50,55,60,65,70]
}

df = pd.DataFrame(data)

X = df[['StudyHours']]
Y = df['Marks']

model = LinearRegression()
model.fit(X,Y)

prediction = model.predict([[6]])

print("Predicted Marks for 6 study hours:",prediction[0])