#!/usr/bin/env python
# coding: utf-8

# In[103]:


import pandas as pd
import numpy as np
import array
import time
from datetime import datetime


# In[104]:


#reading files
listLong = pd.read_csv("../tva_output.csv", parse_dates=True)
listPing = pd.read_csv("../ping.csv",parse_dates=True) 


# In[105]:


#putting the columns in memory
time = listLong.iloc[:, 1]
server = listLong.iloc[:, 2]
tactic = listLong.iloc[:, 3]
latency = listLong.iloc[:, 4]
cost = listLong.iloc[:, 5]
reliability = listLong.iloc[:, 6]

timePing = listPing.iloc[:, 0]
serverPing = listPing.iloc[:, 1]
reliabilityPing = listPing.iloc[:, 2]
pingPing = listPing.iloc[:, 3]

length = len(time) 
merged = np.zeros((length,7))


# In[106]:


#merging data
i = 0 
for j in range(0,length):
    merged[(j,1)] = server[j]
    merged[(j,2)] = tactic[j]
    
    if j > 23 and tactic[j] == 1:
        merged[(j,3)] = pingPing[i]
        i = i + 1
        
    merged[(j,4)] = latency[j]
    merged[(j,5)] = cost[j]
    merged[(j,6)] = reliability[j]

            
        
            


# In[107]:


#saving
np.savetxt("merged.csv", merged, delimiter=",", header="datetime,server,tactuc,ping,latency,cost,reliability")

