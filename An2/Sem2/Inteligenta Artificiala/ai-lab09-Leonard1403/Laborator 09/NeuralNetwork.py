import numpy as np

# This code implements a neural network with a single hidden layer,
# which uses sigmoid activation functions for the hidden layer and
# softmax activation function for the output layer. The network takes
# input data of size input_size, has hidden_size neurons in the hidden
# layer, and output_size neurons in the output layer.

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.bias1 = np.zeros((1, self.hidden_size))
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)
        self.bias2 = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def softmax(self, x):
        exp_scores = np.exp(x)
        return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    def forward(self, X):
        # Hidden layer
        self.hidden_layer = np.dot(X, self.weights1) + self.bias1
        self.hidden_layer_activation = self.sigmoid(self.hidden_layer)

        # Output layer
        self.output_layer = np.dot(self.hidden_layer_activation, self.weights2) + self.bias2
        self.output_layer_activation = self.softmax(self.output_layer)

        return self.output_layer_activation

    def backward(self, X, y, y_hat):
        # Output layer
        error_output_layer = y_hat - y
        d_output_layer = error_output_layer / y.shape[0]

        # Hidden layer
        error_hidden_layer = np.dot(d_output_layer, self.weights2.T) * self.sigmoid_derivative(
            self.hidden_layer_activation)
        d_hidden_layer = error_hidden_layer / y.shape[0]

        # Update weights and biases
        self.weights2 -= self.learning_rate * np.dot(self.hidden_layer_activation.T, d_output_layer)
        self.bias2 -= self.learning_rate * np.sum(d_output_layer, axis=0, keepdims=True)
        self.weights1 -= self.learning_rate * np.dot(X.T, error_hidden_layer)
        self.bias1 -= self.learning_rate * np.sum(error_hidden_layer, axis=0, keepdims=True)

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            # Forward propagation
            y_hat = self.forward(X)

            # Backward propagation
            self.backward(X, y, y_hat)

            # Compute loss
            loss = np.mean(-np.sum(y * np.log(y_hat), axis=1))

            # Print loss every 100 epochs
            # if epoch % 100 == 0:
            print(f"Epoch {epoch}: Loss = {loss:.4f}")

    def predict(self, X):
        y_hat = self.forward(X)
        return np.argmax(y_hat, axis=1)
