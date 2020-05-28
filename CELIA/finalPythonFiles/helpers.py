
import numpy as np
import pandas as pd

def rowToTime(row):
    timeAtMoment = row.Hours*3600*1000
    timeAtMoment += row.Minutes*60*1000
    timeAtMoment += row.Seconds*1000
    return timeAtMoment


def shiftTransformCol50(data):
    return (data + abs(data.min()))*50


def predictionStatAnalysis(data):
    cost =  np.sqrt(np.mean((data.TotalCost - data.predicted_TotalCost)**2))
    latency = np.sqrt(np.mean((data.Latency - data.predicted_Latency)**2))
    print('cost RMSE: ', cost)
    print('latency RMSE: ', latency)
    print('avg rmse', (cost+latency)/2)



