#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys
import pandas as pd


# utility = (reward^5)/ (latency+cost)
def calculateUtil(latency, cost, reward = 100, reliability = 1):
    
    if latency > 0 or cost > 0 and latency+cost != 0:
        return ((reward)/(latency+cost)) * reliability 
    else:
        return -1

# this funciton picks up the latency and the cost columns from a csv file
def readUtilityIntoArray(fileName, costColName, latencyColName, reliabilityName):
    
    
    file = pd.read_csv(fileName)
    latencies = file[costColName]
    costs = file[latencyColName]
    # in case the file doesn't have reliability vals, it defaults to a list of 0
    try:
        reliabilityVals = file[reliabilityName]
    except:
        reliabilityVals = [1] * len(costs)

    data = []
    for i in range(len(latencies)):
         data.append(calculateUtil(latencies[i], costs[i], reliabilityVals[i]))
        
        
    return data

# calculate the utility of each latency, cost row
def genUtilityDataFrame(realFile, realCostColName, realLatencyColName, realReliabilityColName, predictedCostColName, predictedLatencyColName, predictedReliabilityColName ):
    realUtility = readUtilityIntoArray(realFile, realCostColName, realLatencyColName, realReliabilityColName)
    predictedUtility = readUtilityIntoArray(realFile, predictedCostColName, predictedLatencyColName, predictedReliabilityColName)
    
    finalData = list(zip(realUtility, predictedUtility))
#   Create the pandas DataFrame 
    df = pd.DataFrame(finalData,columns=['realUtility', 'predictedUtility']) 
    return df


def main(args):
    if len(args)<3:
        print ("file names missing")
        
    if len(args) < 9:
        File = args[1]
        realCostColName = "Cost.1"
        realLatencyColName = "Latency.1"
        realReliabilityColName = "Reliability.1"
        predictedCostColName = "predicted_Cost"
        predictedLatencyColName = "predicted_Latency"
        predictedReliabilityColName = "predicted_Reliability"
        outputFile = args[2]
    else:
        File = args[1]
        realCostColName = args[2]
        realLatencyColName = args[3]
        realReliabilityColName = args[4]
        predictedCostColName = args[5]
        predictedLatencyColName = args[6]
        predictedReliabilityColName = args[7]
        outputFile = args[8]
   
    realPredictedUtility = genUtilityDataFrame(File, realCostColName, realLatencyColName, realReliabilityColName, predictedCostColName, predictedLatencyColName, predictedReliabilityColName)
    # writing to file
    realPredictedUtility.to_csv(outputFile)
    
if __name__ == "__main__":
    main(sys.argv)



