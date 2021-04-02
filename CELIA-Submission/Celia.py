
import os
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

from utilityFunction import *
from helpers import *



def celia(data,updateThreshold = 1000):


    print('updateThresold = ', updateThreshold)
    lastUpdate = 0
    utilitPredicted = []
    utilityReal = []
    award = []
    lostUtility = []
    shouldHaveUpdated = []
    performedUpdate = []

    temp = data.iloc[1]['timestamp'] - data.iloc[0]['timestamp']
    numOfUpdates = 0
    negativeAward = []
    for i in range(1,len(data)):

        timeDeltaReward = (data.iloc[i]['timestamp'] - data.iloc[lastUpdate]['timestamp'])

        predictedUtil = utilFunction(data.iloc[i].predicted_latency, data.iloc[i].predicted_cost,(float)(timeDeltaReward),1 )

        realUtility = utilFunction(data.iloc[i].latency, data.iloc[i].cost,(float)(timeDeltaReward), 1 )
        
        utilitPredicted.append(predictedUtil)
        
        utilityReal.append(realUtility)
        
        if predictedUtil >= updateThreshold:

            lastUpdate = i
            lostUtility.append(0)
            
            performedUpdate.append(1) #this is the should/not have updated checks 
            
            if realUtility >= updateThreshold:
                award.append(realUtility-updateThreshold)
                negativeAward.append(0)
                shouldHaveUpdated.append(1)
            else:
                award.append(0)
                shouldHaveUpdated.append(0)
                negativeAward.append(abs(realUtility-updateThreshold))
                
            numOfUpdates += 1
        else:
            award.append(0)
            
            performedUpdate.append(0)
            
            if realUtility >= updateThreshold:
                lostUtility.append(realUtility)
                negativeAward.append(realUtility-updateThreshold)

                shouldHaveUpdated.append(1)

            else:
                lostUtility.append(0) 
                
                negativeAward.append(0)

                shouldHaveUpdated.append(0)

    
    results = pd.DataFrame(np.stack([utilitPredicted,utilityReal, award, negativeAward, lostUtility,shouldHaveUpdated,performedUpdate],axis=1),columns=['predictedUtility','realUtility','reward','negativeReward','lostUtility','shouldHaveUpdated','performedUpdate'])
    return results, numOfUpdates


def celiaDataPrep(data, updateThreshold = 1000, returnDataOnly = False, fileHeaders = False):
    
    if fileHeaders == False:
        dataPred = data
        print('data copied')
    else:
        dataPred = pd.DataFrame(data)
        dataPred['timestamp'] = pd.to_datetime(data[fileHeaders['timestamp']])
        dataPred['predicted_latency'] = data[fileHeaders['predicted_latency']]
        dataPred['predicted_cost'] = data[fileHeaders['predicted_cost']]
        dataPred['latency'] = data[fileHeaders['latency']]
        dataPred['cost'] = data[fileHeaders['cost']]
        dataPred['predicted_reliability'] = data[fileHeaders['predicted_reliability']]
        dataPred['reliability'] = data[fileHeaders['reliability']]

    ### this is converting hours, minutes, seconds to a millisecond time series
    
    dataPred['Hours'] = dataPred.timestamp.dt.hour
    dataPred['Minutes'] = dataPred.timestamp.dt.minute
    dataPred['Seconds'] = dataPred.timestamp.dt.second
    
    cumulativeTime = [rowToTime(dataPred.iloc[0])]
    resetAddTime = 23*3600*1000
    resetAddTime += 59*60*1000
    resetAddTime += 60*1000



    for i in range(1,len(dataPred)):
        timeAtMoment = rowToTime(dataPred.iloc[i])
        lastTimeMoment = rowToTime(dataPred.iloc[i-1])
        if timeAtMoment > lastTimeMoment:
            cumuTime = cumulativeTime[i-1] + (timeAtMoment - lastTimeMoment)
            cumulativeTime.append(cumuTime)
        else:
            cumulativeTime.append(cumulativeTime[i-1]+(timeAtMoment+resetAddTime)-lastTimeMoment)
    #         print(cumulativeTime[i])
    
    cumulativeTime = cumulativeTime- cumulativeTime[0]
    

    newData = np.stack((cumulativeTime, dataPred.latency, dataPred.cost, dataPred.reliability, dataPred.predicted_latency, dataPred.predicted_cost, round(dataPred.predicted_reliability)),axis = 1)
    newData = pd.DataFrame(newData, columns=['timestamp', 'latency', 'cost', 'reliability', 'predicted_latency', 'predicted_cost', 'predicted_reliability' ])
    
    if returnDataOnly == True:
        print("returning data only")
        return newData
    else:
        return celia(newData, updateThreshold)

