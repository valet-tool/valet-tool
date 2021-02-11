Reward Threshold: 1000
I tried multiple values to test the frequency of the updates. I settled on 1000 because values less than that resulted in the system updating too frequenctly and too sparodically if the values were higher. Also as the threshold represents a service level Agreement, I wanted the value to be easier to use.

predicted utility: time since last update /  predicted cost + predicted latency
the predicted utility is used to check whether the system should update or not. It is different for every decision step because it uses time since last update. Therefore at each decision step, it has a higher chance of being updated since time since last update increases.

real utility: time since last update /  real cost + real latency
real utility is the actual groubd truth utility of performing the update. It is different for every decision step because it uses time since last update. Therefore at each decision step, it has a higher utility for performing an update since time since last update increases.

award: real utility - Reward Threshold(1000)
It is the award the system gets when it performs an update. It is the difference of the real utility of performign the update and the reward threshold. It is zero when no update is performed.

lostUtility: real utility when update doesn't happen when it should
The lost utility is the utility lost by the system when it doesn't perform the update when it should have according to the real utility. It's default value is zero. When the system doesn't update when it is suppose to, the penalty is qual to the  the real utility.

cost and latencies: The machine learning models have been trained on a normalized dataset(including the output) for performance reasons. But because of Dartsim's inability to handle continous values, we had to transform the data. all the cost and latencies have been shifted by their minimum value and scaled by 50 in order for dartsim to function properly. I applied the same logic over here for consistency's sake and so it was easier to set a reward threshold.



