Arguments:
- Data file
- real cost col name
- real latency col name 
- real reliability col name
- predicted cost col name
- predicted latency col name 
- predicted reliability col name
- output file name

### How to run the script:
option 1
e.g.
python utilityScript.py data.csv realCost realLatency realReliability predCost predLatency predReliability outputUtilityFile.csv

option 2 (will default to hard coded col names)
e.g.
python utilityScript.py data.csv outputUtilityFile.csv