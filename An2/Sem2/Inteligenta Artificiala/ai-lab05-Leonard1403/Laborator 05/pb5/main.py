import numpy as np

# entropia încrucișată
def cross_entropy(probabilities, labels):
    n_samples = len(probabilities)
    loss = 0.0
    for i in range(n_samples):
        y_true = np.zeros(2)
        if labels[i] == 'fruit':
            y_true[0] = 1
        else:
            y_true[1] = 1
        y_pred = probabilities[i]
        loss += -np.sum(y_true * np.log(y_pred))
    return loss / n_samples

probabilities = np.array([[0.9, 0.1], [0.4,0.6], [0.1,0.9], [0.8, 0.2]])
labels = ['fruit', 'non-fruit', 'non-fruit', 'fruit']

loss = cross_entropy(probabilities, labels)
print("Cross-entropy loss: ", loss)
