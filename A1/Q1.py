import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def buildMatrix(l, degree):
    m = np.zeros((len(l), degree+1)) # initializing matrix
    
    powerList = []
    for i in range(degree+1):
        powerList.append(i)
    
    for row in range(len(l)):
        m[row] = l[row]
        m[row] = np.power(m[row], powerList)

    return m



if __name__ == "__main__":

    testFileName = "Datasets/Dataset_1_test.csv"
    
    testFile = pd.read_csv(testFileName, header=None)
    testFile = testFile.drop([2], axis=1) # empty column
    input_test = testFile[0]
    output_test = testFile[1]

    trainFileName = "Datasets/Dataset_1_train.csv"

    trainFile = pd.read_csv(trainFileName, header=None)
    trainFile = trainFile.drop([2], axis=1) # empty column
    input_train = trainFile[0]
    output_train = trainFile[1]

    validFileName = "Datasets/Dataset_1_valid.csv"

    validFile = pd.read_csv(validFileName, header=None)
    validFile = validFile.drop([2], axis=1) # empty column
    input_valid = validFile[0]
    output_valid = validFile[1]



