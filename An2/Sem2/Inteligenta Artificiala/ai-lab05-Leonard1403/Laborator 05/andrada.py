
from cmath import sqrt
from sklearn.metrics._classification import accuracy_score, precision_score, recall_score, log_loss, hamming_loss


def readCSV(filename):
    with open(filename) as file:
        lines = file.readlines()
        matrix =[]
        for line in lines:
            line = line.strip()
            matrix.append([x for x in line.split(",")])
        matrix.pop(0)
        mid = len(matrix[0])//2
        inputs = [row[:mid] for row in matrix]
        outputs = [row[mid:] for row in matrix]
        return inputs, outputs
    

def predictionError(list):
    realOutputs = [x[0] for x in list]
    computedOutputs = [x[1] for x in list]
    error = sum(abs(int(r) - int(c)) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs)
    loss = sum((int(r) - int(c)) ** 2 for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs)
    return [error, loss]


def calculatePredictionError(inputs, outputs):
    #problema de regresie multi-target
    list = [[] for _ in range(len(inputs[0]))]
    for i in range(len(inputs[0])):
        for j in range(len(inputs)):
            list[i].append([inputs[j][i], outputs[j][i]])
    result = []
    for i in range(len(list)):
        result.append(predictionError(list[i]))
    error = sum([x[0] for x in result]) / len(result)
    loss = sum([x[1] for x in result]) / len(result)
    return error, loss   


def runPredictionError():
    filename = "D:\\UBB FMI\\AI\\Lab5\\testData\\sport.csv"
    inputs, outputs = readCSV(filename)
    error, loss = calculatePredictionError(inputs, outputs)
    print(f"Eroare de predictie: {error}")
    print(f"Loss(problema de regresie): {loss}")


def calculateAPR(inputs,outputs):
    #clasificare multi-class
    inputsList = [x[0] for x in inputs]
    outputsList = [x[0] for x in outputs]
    labelNames = list(set(inputsList + outputsList))
    accuracy = accuracy_score(inputs, outputs)
    precision = precision_score(inputs,outputs, average = None, labels = labelNames)
    recall = recall_score(inputs, outputs, average = None, labels = labelNames)
    loss = hamming_loss(inputs, outputs)
    return accuracy, precision, recall, loss


def runCalculateAPR():
    filename = "D:\\UBB FMI\\AI\\Lab5\\testData\\flowers.csv"
    inputs, outputs = readCSV(filename)
    accuracy, precision, recall, loss = calculateAPR(inputs, outputs)
    print(f"Accuracy:  {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Loss(clasificare multi-class): {loss}")

def loss():
    realLabels1 = ['fruit', 'non-fruit','non-fruit','fruit']
    computedOutputs1 = [[0.9, 0.1], [0.4, 0.6], [0.1, 0.9], [0.8, 0.2]]
    print(f"Loss Fruits(clasificare binara): {log_loss(realLabels1, computedOutputs1)}")

    realLabels2 = ['spam', 'spam', 'ham', 'ham', 'spam', 'ham']
    computedOutputs2 = [ [0.7, 0.3], [0.2, 0.8], [0.4, 0.6], [0.9, 0.1], [0.7, 0.3], [0.4, 0.6]]
    print(f"Loss Emails: {log_loss(realLabels2, computedOutputs2)}")




runPredictionError()
runCalculateAPR()
loss()
