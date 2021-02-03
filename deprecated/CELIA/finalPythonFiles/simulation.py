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