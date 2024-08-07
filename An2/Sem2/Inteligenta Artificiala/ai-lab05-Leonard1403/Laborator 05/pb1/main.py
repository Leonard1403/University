import pandas as pd
from sklearn.metrics import mean_squared_error
import math

# Citim datele din fisier
data = pd.read_csv("E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 05\pb1\sport.csv")
print(data)

# Selectam variabilele independente si dependente
X = data.iloc[:, :3]
y = data.iloc[:, 3:]

# Calculam RMSE pentru fiecare tinta in parte
rmse_weight = math.sqrt(mean_squared_error(X['Weight'], y['PredictedWeight']))
rmse_waist = math.sqrt(mean_squared_error(X['Waist'], y['PredictedWaist']))
rmse_pulse = math.sqrt(mean_squared_error(X['Pulse'], y['PredictedPulse']))

# Calculam masura de eroare globala
error = (rmse_weight + rmse_waist + rmse_pulse) / 3

# Afisam rezultatele
print(f"RMSE Weight: {rmse_weight:.2f}")
print(f"RMSE Waist: {rmse_waist:.2f}")
print(f"RMSE Pulse: {rmse_pulse:.2f}")
print(f"Error: {error:.2f}")

# Procedura de evaluare a unui algoritm de ML pentru o problema de regresie
# multi-target poate fi realizata prin compararea valorilor prezise cu cele
# reale si calcularea unei masuri de eroare. Una dintre cele mai folosite
# metode este calcularea rădăcinii erorii medie pătratice (RMSE).
# RMSE este o masura de dispersie care arata cat de departe sunt
# prezicerile de valorile reale, iar valoarea acesteia se calculeaza prin formula:
# RMSE = sqrt((1/n) * sum((predicted_i - real_i)^2))