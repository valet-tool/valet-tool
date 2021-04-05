
import numpy as np
import pandas as pd
import json
import os
from Celia import *

def simulation(data,threshold, headers = False):

    print(headers)
    result, numOfUpdates = celiaDataPrep(data, threshold, fileHeaders = headers)

    utilDif = np.sum(abs(result.predictedUtility-result.realUtility))
    reward = sum(result.reward)
    negativeReward = sum(result.negativeReward)
    lostUtil = sum(result.lostUtility)

    decisionShouldHaveDid = len(result[result.shouldHaveUpdated == 1][result.performedUpdate == 1])
    decisionShouldHaveDidNot = len(result[result.shouldHaveUpdated == 1][result.performedUpdate == 0])
    decisionNotHaveDid = len(result[result.shouldHaveUpdated == 0][result.performedUpdate == 1])
    decisionNotHaveDidNot = len(result[result.shouldHaveUpdated == 0][result.performedUpdate == 0])

    wrongDecisions = decisionShouldHaveDidNot + decisionNotHaveDid
    correctDecisions = decisionShouldHaveDid + decisionNotHaveDidNot
    stats = [utilDif, reward, negativeReward, numOfUpdates, lostUtil, wrongDecisions, correctDecisions, decisionShouldHaveDid, decisionShouldHaveDidNot, decisionNotHaveDid, decisionNotHaveDidNot]
    return  result, stats

def main(argFile):
    celiaStats = []
    
    inputFileName = argFile['inputFileName']
    inputDirectory = argFile['inputDirectory']
    outputFileName = argFile['outputFileName']
    outputDirectory = argFile['outputDirectory']
    outputStatFileName = argFile['outputStatFileName']
    threshold = argFile['threshold']
    
    if 'headers' in argFile.keys():
            headers = argFile['headers']
    else:
        headers = False

    if argFile['multiFile'] == False:
        
        dataPred = pd.read_csv(inputDirectory+inputFileName)

        result, stats = simulation(dataPred,threshold,headers)
        
        stats.insert(0,inputFileName)
        celiaStats.append(stats)
        
        try:
            result.to_csv(outputDirectory+outputFileName)
        except:
            result.to_csv(outputDirectory+'/'+outputFileName)
    
    
    if argFile['multiFile'] == True:
            
        fileNames = []

        for (dirpath, dirnames, filenames) in os.walk(inputDirectory):
            
            for file in filenames:
                if '.csv' in file:
                    fileNames.append([dirpath, file])
        
        # for f in os.listdir(argFile['inputDirectory']):
        #     if '.csv' in f:
        #         fileNames.append(f)
        if len(fileNames) == 0:
            print('No Files in directory')
            return
        
        notDone = []
        errorMsg = []
        for i in fileNames:

            dataPred = pd.read_csv(os.path.join(i[0], i[1]))
            print("starting "+ str(i[1]))

            try: 
                    
                result, stats = simulation(dataPred,threshold,headers)
                stats.insert(0,i[1])

                celiaStats.append(stats)
                
                try:
                    result.to_csv(outputDirectory+i[1])
                except:
                    result.to_csv(outputDirectory+'/'+i[1])
            except Exception as e:
                notDone.append(os.path.join(i[0], i[1]))
                errorMsg.append(e)

                
    celiaStats = pd.DataFrame(celiaStats, columns=['predictionType','utilDif','reward','negativeReward', 'numOfUpdates','lostUtil', 'wrongDecisions', 'correctDecisions', 'decisionShouldHaveDid', 'decisionShouldHaveDidNot', 'decisionNotHaveDid', 'decisionNotHaveDidNot'])
  
    try:
        celiaStats.to_csv(outputDirectory+outputStatFileName)
    except:
        celiaStats.to_csv(outputDirectory+'/'+outputStatFileName)

    print("Not Done:")
    pd.DataFrame([notDone, errorMsg]).to_csv(outputDirectory+'/notDone.csv')
    print(notDone)

if __name__ == "__main__":
    argFile = {}
    with open(sys.argv[1]) as f:
        argFile = json.load(f)

    main(argFile)