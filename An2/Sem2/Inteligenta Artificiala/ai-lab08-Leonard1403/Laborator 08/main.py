import math
import random

import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model
from numpy import argmax
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from MyLogisticRegression import MyLogisticRegression
from logisticRegressionMulti import LogisticRegressorMulti

# Pasul 1 - Extragerea datelor
def loadData1():
    filename = 'data/wdbc.data'
    f = open(filename, 'r')

    ins = []
    outs = []

    for line in f.readlines():
        cols = line[:-1].split(",")
        ins.append([float(cols[2]), float(cols[3])])
        if cols[1] == 'M':
            outs.append(1)
        else:
            outs.append(0)
    return ins, outs
def loadData2():
    filename = 'data/iris.data'
    f = open(filename, 'r')

    ins = []
    outs = []

    for line in f.readlines():
        cols = line[:-1].split(",")
        ins.append([float(cols[0]), float(cols[1]), float(cols[2]), float(cols[3])])
        outs.append(cols[4])
    return ins, outs

def prepareData2(ins, outs, ratio=0.9):
    labels = []
    for x in outs:
        if x not in labels:
            labels.append(x)
    y = []
    for x in outs:
        yy = [0] * len(labels)
        for i in range(len(labels)):
            if labels[i] == x:
                yy[i] = 1
        y.append(yy)

    outs = y
    scaler = StandardScaler()

    scaler.fit(ins)
    ins = scaler.transform(ins)

    random.seed(5)
    dataSize = len(ins)
    indexes = [e for e in range(dataSize)]

    trainingSize = math.floor(dataSize * ratio)
    testSize = dataSize - trainingSize

    trainingIndexes = random.sample(indexes, trainingSize)
    testIndexes = [e for e in indexes if e not in trainingIndexes]

    insT = [ins[e] for e in trainingIndexes]
    outsT = [outs[e] for e in trainingIndexes]
    insV = [ins[e] for e in testIndexes]
    outsV = [outs[e] for e in testIndexes]

    return insT, outsT, insV, outsV

# Pasul 2- Normalizarea, impartirea si plotarea datelor
def plotClassificationData(feature1, feature2, outputs, title = None, outputNames = ['malignant', 'benign']):
    labels = set(outputs)
    noData = len(feature1)
    outputNames = ['malignant', 'benign']
    for crtLabel in labels:
        x = [feature1[i] for i in range(noData) if outputs[i] == crtLabel ]
        y = [feature2[i] for i in range(noData) if outputs[i] == crtLabel ]
        plt.scatter(x, y,label= outputNames[crtLabel])
    plt.xlabel('mean radius')
    plt.ylabel('mean texture')
    plt.legend()
    plt.title(title)
    plt.show()

def normalisation(trainData, testData):
    scaler = StandardScaler()
    if not isinstance(trainData[0], list):
        # encode each sample into a list
        trainData = [[d] for d in trainData]
        testData = [[d] for d in testData]

        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data

        # decode from list to raw values
        normalisedTrainData = [el[0] for el in normalisedTrainData]
        normalisedTestData = [el[0] for el in normalisedTestData]
    else:
        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data
    return normalisedTrainData, normalisedTestData

def split(inputs, outputs, ratio=0.8):
    # split data into train and test subsets
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(ratio * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    # normalise the features
    # print(trainInputs, testInputs)

    trainInputs, testInputs = normalisation(trainInputs, testInputs)

    return trainInputs, trainOutputs, testInputs, testOutputs
def split2(input, outputs, ratio=0.8):
    scaler = StandardScaler()

    scaler.fit(input)
    inputs = scaler.transform(input)

    random.seed(5)
    dataSize = len(input)
    indexes = [e for e in range(dataSize)]

    trainingSize = math.floor(dataSize * ratio)

    trainingIndexes = random.sample(indexes, trainingSize)
    testIndexes = [e for e in indexes if e not in trainingIndexes]

    feature1train = [inputs[e] for e in trainingIndexes]
    feature2train = [outputs[e] for e in trainingIndexes]
    feature1test = [inputs[e] for e in testIndexes]
    feature2test = [outputs[e] for e in testIndexes]

    # print(feature1train, feature1test)

    # normalisation(feature1train, feature1test)

    plotClassificationData(feature1train, feature2train, feature2test, ['Iris-setosa','Iris-versicolor','Iris-virginica'])
    return feature1train, feature1test, feature2train, feature2test

def plotPredictions(outputs, feature1, feature2, realOutputs, computedOutputs, title, labelNames):
    labels = list(set(outputs))
    noData = len(feature1)
    for crtLabel in labels:
        x = [feature1[i] for i in range(noData) if realOutputs[i] == crtLabel and computedOutputs[i] == crtLabel ]
        y = [feature2[i] for i in range(noData) if realOutputs[i] == crtLabel and computedOutputs[i] == crtLabel]
        plt.scatter(x, y, label = labelNames[crtLabel] + ' (correct)')
    for crtLabel in labels:
        x = [feature1[i] for i in range(noData) if realOutputs[i] == crtLabel and computedOutputs[i] != crtLabel ]
        y = [feature2[i] for i in range(noData) if realOutputs[i] == crtLabel and computedOutputs[i] != crtLabel]
        plt.scatter(x, y, label = labelNames[crtLabel] + ' (incorrect)')
    plt.xlabel('mean radius')
    plt.ylabel('mean texture')
    plt.legend()
    plt.title(title)
    plt.show()

def problema1():
    ins, outs = loadData1()
    print(ins)
    print(outs)
    # split2(ins,outs)
    trainInputs, trainOutputs, testInputs, testOutputs = split(ins, outs)

    model  = MyLogisticRegression()
    model.fit(trainInputs, trainOutputs)
    w0, w1, w2 = model.intercept_, model.coef_[0], model.coef_[1]
    print('y(feat1, feat2) = ', w0, '+ ', w1, '*feat1 + ', w2, '*feat2')
    computedTestOutputs = model.predict(testInputs)

    feature1train = [ex[0] for ex in trainInputs]
    feature2train = [ex[1] for ex in trainInputs]
    feature1test = [ex[0] for ex in testInputs]
    feature2test = [ex[1] for ex in testInputs]
    plotClassificationData(feature1train, feature2train, trainOutputs, 'normalised train data')
    plotPredictions(outs, feature1test, feature2test, testOutputs, computedTestOutputs, 'Predictions on test data', ['malignant', 'benign'])

def problema2_tool():
    ycomputed = []
    ins, outs = loadData2()

    # print(ins)
    # print(outs)

    trainInputs, trainOutputs, testInputs, testOutputs = prepareData2(ins,outs)
    yreal = [x[0] * 0 + x[1] * 1 + x[2] * 2 for x in testOutputs]

    model = LogisticRegressorMulti()
    model.fit(trainInputs, trainOutputs)
    computedTestOutputs = model.predict(testInputs)
    for i in computedTestOutputs:
        ycomputed.append(argmax(i))
    w0, w1, w2 = model.returnw()
    print('y(feat1, feat2) = ', w0, '+ ', w1, '*feat1 + ', w2, '*feat2')

    accuracy = len([i for i in range(len(ycomputed)) if ycomputed[i] == yreal[i]]) / len(ycomputed)
    print(accuracy)

    model  = sklearn.linear_model.LogisticRegression(multi_class = "ovr")
    # model.fit(trainInputs, trainOutputs)

    model.fit(trainInputs, [x[0] * 0 + x[1] * 1 + x[2] * 2 for x in trainOutputs])
    w0, w1, w2 = model.intercept_, model.coef_[0], model.coef_[1]
    print('y(feat1, feat2) = ', w0, '+ ', w1, '*feat1 + ', w2, '*feat2')

    computedTestOutputs = model.predict(testInputs)

    ycomputed.clear()
    for i in computedTestOutputs:
        ycomputed.append(argmax(i))
    #  list comprehension
    accuracy = len([i for i in range(len(ycomputed)) if ycomputed[i] == yreal[i]]) / len(ycomputed)
    print(accuracy)

if __name__ == '__main__':
    # problema1()
    problema2_tool()
