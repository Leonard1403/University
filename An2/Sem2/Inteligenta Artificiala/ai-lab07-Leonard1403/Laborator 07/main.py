import csv
import matplotlib.pyplot as plt
from math import log, sqrt


# load all the data from a csv file
# load all the data from a csv file
import numpy as np
from sklearn.linear_model import SGDRegressor


def loadDataMoreInputs(fileName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    return dataNames, data

# extract a particular feature (column)
def extractFeature(allData, names, featureName):
    pos = names.index(featureName)
    return [float(data[pos]) if data[pos] != '' else None for data in allData]

# replace missing values with mean value
def replaceMissingValues(data):
    total = 0
    count = 0
    for value in data:
        if value is not None:
            total += value
            count += 1
    mean = total / count
    return [value if value is not None else mean for value in data]

# plot a histogram for some data x
def plotDataHistogram(x, variableName):
    n, bins, patches = plt.hist(x, 20)
    plt.title('Histogram of ' + variableName)
    plt.show()

# standardisation
# it preserves the data distribution
import os

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data', 'v1_world-happiness-report-2017.csv')

names, allData = loadDataMoreInputs(filePath)
gdp = extractFeature(allData, names, 'Economy..GDP.per.Capita.')
gdp = replaceMissingValues(gdp) # replace missing values with mean value

happy = extractFeature(allData, names, 'Happiness.Score')
happy = replaceMissingValues(happy) # replace missing values with mean value

m = sum(gdp) / len(gdp)
s = (1 / (len(gdp) - 1) * sum([(p - m) ** 2 for p in gdp])) ** 0.5
gdpZscore = [(p - m) / s for p in gdp]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,5))
ax1.hist(gdp, 20)
ax1.set_title('gdp histo')
ax2.hist(gdpZscore, 20)
ax2.set_title('z-score gdp histo')
plt.show()

# m = sum(happy) / len(happy)
# s = (1 / (len(happy) - 1) * sum([(p - m) ** 2 for p in happy])) ** 0.5
# happyZscore = [(p - m) / s for p in gdp]
happyZscore = happy

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,5))
ax1.hist(happy, 20)
ax1.set_title('happy histo')
ax2.hist(happyZscore, 20)
ax2.set_title('z-score happy histo')
plt.show()

inputs = gdpZscore
outputs = happyZscore

np.random.seed(5)
indexes = [i for i in range(len(inputs))]
trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace = False)
testSample = [i for i in indexes  if not i in trainSample]

trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]

testInputs = [inputs[i] for i in testSample]
testOutputs = [outputs[i] for i in testSample]

plt.plot(trainInputs, trainOutputs, 'ro', label = 'training data')   #train data are plotted by red and circle sign
plt.plot(testInputs, testOutputs, 'g^', label = 'testing data')     #test data are plotted by green and a triangle sign
plt.title('train and test data')
plt.xlabel('GDP capita')
plt.ylabel('happiness')
plt.legend()
plt.show()


xx = [[el] for el in trainInputs]

xx = np.array(xx)
trainOutputs = np.array(trainOutputs)

# print(xx)
# print(trainOutputs)

from linear_regression import LinearRegression

model = LinearRegression()
model.fit(xx, trainOutputs)

w0 = model.bias
w1 = model.weights[0]


noOfPoints = 1000
xref = []
val = min(trainInputs)
step = (max(trainInputs) - min(trainInputs)) / noOfPoints
for i in range(1, noOfPoints):
    xref.append(val)
    val += step
yref = [w0 + w1 * el for el in xref]

plt.plot(trainInputs, trainOutputs, 'ro', label = 'training data')  #train data are plotted by red and circle sign
plt.plot(xref, yref, 'b-', label = 'learnt model')                  #model is plotted by a blue line
plt.title('train data and the learnt model')
plt.xlabel('GDP capita')
plt.ylabel('happiness')
plt.legend()
plt.show()

computedTestOutputs = model.predict(xx)

error = 0.0
for t1, t2 in zip(computedTestOutputs, testOutputs):
    error += (t1 - t2) ** 2
error = error / len(testOutputs)
print('prediction error (manual): ', error)

