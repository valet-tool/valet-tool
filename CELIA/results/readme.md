Reward Threshold: 1000
I tried multiple values to test the frequency of the updates. I settled on 1000 because values less than that resulted in the system updating too frequenctly and too sparodically if the values were higher. Also as the threshold represents a service level Agreement, I wanted the value to be easier to use.

predicted utility: time since last update /  predicted cost + predicted latency

real utility: time since last update /  real cost + real latency

award: predicted utility - Reward Threshold(1000)

lostUtility: real utility when update doesn't happen when it should

cost and latencies: all the cost and latencies have been shifted by their minimum value and scaled by 50 in order for dartsim to function properly. I applied the same logic over here

