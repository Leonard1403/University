import numpy as np
import idx2numpy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from NeuralNetwork import NeuralNetwork

# Load MNIST data
X = idx2numpy.convert_from_file('data/train-images.idx3-ubyte')
y = idx2numpy.convert_from_file('data/train-labels.idx1-ubyte')

# Convert labels to one-hot encoding
y_one_hot = np.zeros((y.shape[0], 10))
y_one_hot[np.arange(y.shape[0]), y] = 1

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X.reshape(X.shape[0], -1), y_one_hot, test_size=0.2)

# Create neural network object
nn = NeuralNetwork(input_size=X_train.shape[1], hidden_size=50, output_size=10)

# Train neural network
epochs = 1000
nn.train(X_train, y_train, epochs)

# Test neural network
y_pred = nn.predict(X_train)
accuracy = accuracy_score(np.argmax(y_train, axis=1), y_pred)
print(f"Training accuracy: {accuracy}")

y_pred = nn.predict(X_val)
accuracy = accuracy_score(np.argmax(y_val, axis=1), y_pred)
print(f"Validation accuracy: {accuracy}")

from sklearn.metrics import confusion_matrix

# Test neural network
# y_pred = nn.predict(X_val)
y_true = np.argmax(y_val, axis=1)

print("y_pred " + str(y_pred))

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Compute precision and recall for each class
precision = {}
recall = {}

for label in range(10):
    true_positives = np.sum(np.logical_and(y_pred == label, y_true == label))
    false_positives = np.sum(np.logical_and(y_pred == label, y_true != label))
    false_negatives = np.sum(np.logical_and(y_pred != label, y_true == label))
    precision[label] = true_positives / (true_positives + false_positives)
    recall[label] = true_positives / (true_positives + false_negatives)

# Print precision and recall for each class
print(f"precision: {precision}")
print(f"recall: {recall}")

# Plot confusion matrix
import matplotlib.pyplot as plt

classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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

while True:
    # Ask user for input
    idx = int(input("Enter digit index (0-59999): "))

    # Display image
    plt.imshow(X[idx], cmap='gray')
    plt.title(f"Digit: {y[idx]}")
    plt.show()

    # Predict output
    output = nn.forward(X[idx].reshape(1, -1))
    predicted_digit = np.argmax(output)

    print(f"Predicted digit: {predicted_digit}")