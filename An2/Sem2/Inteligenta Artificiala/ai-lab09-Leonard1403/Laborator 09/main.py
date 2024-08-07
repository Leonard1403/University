import numpy as np
import pandas as pd

# Load data
from matplotlib import pyplot as plt

from NeuralNetwork import NeuralNetwork

# Load data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = pd.read_csv(url, header=None)

# Extract features and labels
X = data.iloc[:, :-1].values
y_str = data.iloc[:, -1].values

# Map string labels to integers
label_map = {label: idx for idx, label in enumerate(set(y_str))}
y = np.array([label_map[label] for label in y_str])

# One-hot encoding for labels
# Mere: [1, 0, 0]
# Pere: [0, 1, 0]
# Banane: [0, 0, 1]

num_classes = len(set(y))
y_one_hot = np.eye(num_classes)[y]

# Normalize data
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Split data into training and test sets
num_samples = X.shape[0]
train_ratio = 0.8
num_train_samples = int(num_samples * train_ratio)
shuffle_indices = np.random.permutation(num_samples)
X_train = X[shuffle_indices[:num_train_samples]]
y_train = y_one_hot[shuffle_indices[:num_train_samples]]
X_test = X[shuffle_indices[num_train_samples:]]
y_test = y_one_hot[shuffle_indices[num_train_samples:]]

# Create neural network
input_size = X_train.shape[1]  # 4 (number of features)
hidden_size = 5
output_size = num_classes
learning_rate = 0.1
epochs = 1000
model = NeuralNetwork(input_size, hidden_size, output_size, learning_rate)

# Train neural network
model.train(X_train, y_train, epochs)

# Predict labels for test data
y_pred = model.predict(X_test)

# Compute accuracy
accuracy = np.mean(y_pred == np.argmax(y_test, axis=1))
print(f"Accuracy: {accuracy * 100:.2f}%")


from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# Compute confusion matrix
cm = confusion_matrix(np.argmax(y_test, axis=1), y_pred)
classes = ['Setosa', 'Versicolor', 'Virginica']

# Plot confusion matrix
fig, ax = plt.subplots()
im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
ax.figure.colorbar(im, ax=ax)
ax.set(xticks=np.arange(cm.shape[1]),
       yticks=np.arange(cm.shape[0]),
       xticklabels=classes, yticklabels=classes,
       ylabel='True label',
       xlabel='Predicted label')
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
fmt = 'd'
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], fmt),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black")
fig.tight_layout()
plt.show()

# Compute precision and recall for each class
precision = {}
recall = {}
for label in label_map:
    idx = label_map[label]
    true_positives = np.sum(np.logical_and(y_pred == idx, y_test[:, idx] == 1))
    false_positives = np.sum(np.logical_and(y_pred == idx, y_test[:, idx] == 0))
    false_negatives = np.sum(np.logical_and(y_pred != idx, y_test[:, idx] == 1))
    precision[label] = true_positives / (true_positives + false_positives)
    recall[label] = true_positives / (true_positives + false_negatives)

# Print precision and recall for each class
print(f"precision: {precision}")
print(f"recall: {recall}")
