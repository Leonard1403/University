import numpy as np


# theta_j = theta_j - alpha * (1/m) * sum((h(x^(i)) - y^(i)) * x_j^(i))

# theta_j is the j-th parameter (or weight) of the linear regression model
# alpha is the learning rate (a hyperparameter that controls the step size at each iteration)
# m is the number of training examples
# h(x^(i)) is the predicted value for the i-th training example, given the current values of the parameters
# y^(i) is the actual (ground truth) value for the i-th training example
# x_j^(i) is the j-th feature of the i-th training example

# J(theta) = (1/2m) * sum((h(x^(i)) - y^(i))^2)

class LinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for i in range(self.num_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
