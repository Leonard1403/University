import pandas as pd
from sklearn.metrics import mean_squared_error
import math

data = pd.read_csv("E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 05\pb1\happy.csv")

print(data)

X = data.iloc[:, 1:2]
Y = data.iloc[:, 2:3]
print(X)
print(Y)

rmse_happiness = math.sqrt(mean_squared_error(X['HappinessScore'], Y['PredictedScore']))

error = (rmse_happiness) / 1

print(f"RMSE Happiness: {rmse_happiness}")
# print(f"Error: {error:.2f}")