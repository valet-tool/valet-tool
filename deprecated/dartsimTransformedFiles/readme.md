./run.sh --map-size=1000  --auto-range --num-targets=50 --num-threats=30

Dartsim works by simulating a team of drones that are supposed to detect targets and avoid getting destroyed. It determines its action by communicating with the adaptation manager. The adaptation manager makes a tactic decision based on the environment. When implementing these tactics, Dartsim has a fixed latency value associated with these. We have changed it to cater variable latencies. We have also inserted cost value which we are emulating as the energy levels of the drone. When this value reaches 0, the drones die and the mission fails. When making tactic decision, the adaptation manager looks at the latencies of tactics and their cost. 

Because Dartsim has no concept of "Servers” we have split the data according to the servers and run dartsim on each set of data. All simulation runs are seeded the value corresponding to their run number. e.g. simulation run 1 in ernn server 1 and knn server 1 will have the random seeded value  of 1. This will allow us fair comparison among the models as all of them were working in the same environment. All simulation runs were run with 50 targets and 30 threats.

predicted/real upDown can have values 0/1/2 -> nothing/up/down

predicted/real tightLoose can have values 0/1/2 -> nothing/tight/Loose

destroyed can be either 0(survived) or 1 (died)

whereDestroyed.x is the distance covered before it died. The default value is 39 when the drones survived

disregard the decisionTime col becasue in our case, those values should be consistant. 