
#This is the utility function used by CELIA.
def utilFunction(latency, cost, reward = 100, reliability = 1):
    epsilon = 0.00000000000000000000000000000000000000000000001

    if reliability == 0:
        return 0
    else:
        return ((reward)/(latency*1000+cost*500+epsilon)) * int(round(reliability)) 
    
