import numpy as np
import matplotlib.pyplot as plt

# Generare date de intrare sintetice
np.random.seed(0)
# X = np.linspace(0, 10, 100)[:, np.newaxis]
# Y_true = 2 * X + 5 + np.random.randn(100, 1)

# X = [10, 10, 10, 8]
# Y_true = [8.04,9.14,7.46,6.58]

# X = [4, 4.3, 4.7, 5, 5.4, 5.8]
# Y_true = [4.5, 4.8, 5, 5.3, 5.6, 6]

X = [1, 2, 2, 2, 5]
Y_true = [1, 2, 3, 4, 5]

# Convertirea listei X in ndarray
X = np.array(X)
# Transformarea matricei X intr-un vector coloana
X = X.reshape(-1, 1)
# Adaugarea unei coloane de 1 la matricea X pentru a reprezenta termenul liber
X_b = np.hstack((np.ones((X.shape[0], 1)), X))

# Afisare date de intrare
plt.scatter(X, Y_true, color='blue', label='Date reale')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Rezolvare problema de regresie
X_b = np.hstack((np.ones((X.shape[0], 1)), X))  # Adaugam o coloana de 1 la matricea X pentru a reprezenta termenul liber
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y_true)  # Calculam coeficientii optimali
Y_pred = X_b.dot(theta)  # Calculam valorile prezise ale Y

# Afisare rezultate
plt.scatter(X, Y_true, color='blue', label='Date reale')
plt.plot(X, Y_pred, color='red', label='Regresie liniara')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Calculare functie de loss (Mean Squared Error)
def mse(Y_true, Y_pred):
    return np.mean((Y_true - Y_pred) ** 2)

loss = mse(Y_true, Y_pred)

# Afisare functie de loss
plt.plot(X, Y_pred, color='red', label='Regresie liniara')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Functie de loss (MSE): {loss:.2f}')
plt.legend()
plt.show()

plt.plot(X, Y_pred, color='red', label='Regres')
