# Import libraries
import csv
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# Load data

# data = pd.read_csv('data/v1_world-happiness-report-2017.csv')
data = pd.read_csv('output.csv')
X = data[['Economy..GDP.per.Capita.', 'Freedom']].values
y = data['Happiness.Score'].values

# Happiness.Score, Economy..GDP.per.Capita., Freedom

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model and fit it to the data
model = LinearRegression()
model.fit(X_train, y_train)

w0, w1, w2 = model.intercept_, model.coef_[0], model.coef_[1]
print('f(x) = ', w2, ' * x^2 + ', w1, ' * x + ', w0)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Validation MSE:', mse)

# Visualize the data and the model
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_train[:,0], X_train[:,1], y_train, c='r', marker='o')
ax.set_xlabel('GDP per capita')
ax.set_ylabel('Freedom')
ax.set_zlabel('Happiness')
x_surf, y_surf = np.meshgrid(np.linspace(X_train[:,0].min(), X_train[:,0].max(), 100),
                             np.linspace(X_train[:,1].min(), X_train[:,1].max(), 100))
z_surf = model.intercept_ + model.coef_[0] * x_surf + model.coef_[1] * y_surf
ax.plot_surface(x_surf, y_surf, z_surf, cmap='coolwarm')
plt.show()

# formule in curs
# standard scalar