import numpy as np


class LogisticRegressionCustom:
    def __init__(self, alpha=0.01, n_iterations=2000, fit_intercept=True):
        self.alpha = alpha
        self.n_iterations = n_iterations
        self.fit_intercept = fit_intercept

    # adaugă o coloană de 1-uri la matricea X.
    def add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    # aplică funcția sigmoid pe vectorul z, adică 1 / (1 + exp(-z)).
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    # calculează softmax-ul vectorului z, adică exp(z) / sum(exp(z)).
    def softmax(self, z):
        exp_z = np.exp(z)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def fit(self, X, y):
        # irst step is to check if fitting an intercept in the model is desired. If yes, the intercept is added to the input matrix X.
        if self.fit_intercept:
            X = self.add_intercept(X)

        # number of classes is calculated, and the parameter matrix theta is initialized with zero values.
        self.classes = np.unique(y)
        # number of iterations defined by the n_iterations argument are applied, and for each iteration, the dot product between the input matrix X and the parameter matrix theta is calculated to obtain a matrix z
        self.num_classes = len(self.classes)
        self.theta = np.zeros((X.shape[1], self.num_classes))

        # on the number of classes, the model outputs A are calculated using the sigmoid or softmax function, respectively
        for i in range(self.n_iterations):
            z = np.dot(X, self.theta)
            # depending on the number of classes, the model outputs A are calculated using the sigmoid or softmax function, respectively.
            if self.num_classes == 2:
                A = self.sigmoid(z)
                # cost = (-1 / X.shape[0]) * np.sum(y * np.log(A) + (1 - y) * np.log(1 - A))
                dz = A - y.reshape(-1, 1)
            else:
                A = self.softmax(z)
                # cost = (-1 / X.shape[0]) * np.sum(y * np.log(A))
                dz = A - (y == self.classes.reshape(1, -1))
            #gradients for the parameters are calculated by backpropagating the errors, and then the parameter matrix theta is updated through gradient descent using the learning rate alpha.
            dw = (1 / X.shape[0]) * np.dot(X.T, dz)
            self.theta -= self.alpha * dw

        return self

    def predict(self, X):
        if self.fit_intercept:
            X = self.add_intercept(X)

        if self.num_classes == 2:
            return np.round(self.sigmoid(np.dot(X, self.theta))).astype(int)
        else:
            return self.classes[np.argmax(self.softmax(np.dot(X, self.theta)), axis=1)]
