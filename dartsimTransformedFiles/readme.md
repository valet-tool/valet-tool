./run.sh --map-size=1000  --auto-range --num-targets=50 --num-threats=30

Dartsim works by simulating a team of drones that are suppose to detect targets and avoid getting destroyed. It determines its action by communicating with the adaptation manager. The adaptation manager makes a decision based on the environment. 

all simulation runs are seeded the value cooresponding to their run number. e.g. simulation run 1 in ernn server 1 and knn server 1 will have the seeded value 1

predicted/real upDown can have values 0/1/2 -> nothing/up/down

predicted/real tightLoose can have values 0/1/2 -> nothing/tight/Loose

destroyed can be either 0(survived) or 1 (died)

whereDestroyed.x is the distance covered before it died. The default value is 39 when the drones survived

