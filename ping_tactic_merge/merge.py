#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import array
import time 
import datetime
from dateutil.relativedelta import relativedelta


# In[2]:


#reading files
listLong = pd.read_csv("../tva_output.csv", parse_dates=True)
listPing = pd.read_csv("../ping.csv",parse_dates=True) 


# In[17]:


a = time[1]
b = time[2]


# In[25]:


a, b


# In[48]:


start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S.%f')

diff = relativedelta(ends, start)


# In[49]:


diff


# In[50]:


ends.microsecond


# In[58]:


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
merged = np.zeros((length,12))


# In[107]:


#merging data
i = 0  #counter for ping values
c = 0  #counter for last time
for j in range(0,length):
    t = time[j]
    currentTime = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
    month = currentTime.month
    day = currentTime.day
    hour = currentTime.hour
    minute = currentTime.minute
    second = currentTime.second + currentTime.microsecond/1000000
    microsecond = currentTime.microsecond
    merged[(j,0)] = month
    merged[(j,1)] = day
    merged[(j,2)] = hour
    merged[(j,3)] = minute
    merged[(j,4)] = second
    merged[(j,5)] = server[j]
    merged[(j,6)] = tactic[j]
    
    if j > 23 and tactic[j] == 1:
        p = timePing[i]
        currentPingTime =  datetime.datetime.strptime(p, '%Y-%m-%d %H:%M:%S.%f')
        currentTimeSeconds = (currentTime.month * 2.628e+6 + currentTime.day * 86400 + currentTime.hour * 3600 + currentTime.minute * 60 + currentTime.second + currentTime.microsecond/1000000 )
        currentPingTimeSeconds = (currentPingTime.month * 2.628e+6 + currentPingTime.day * 86400 + currentPingTime.hour * 3600 + currentPingTime.minute * 60 + currentPingTime.second + currentPingTime.microsecond/1000000 )
        age = currentTimeSeconds - currentPingTimeSeconds
        merged[(j,7)] = pingPing[i]
        merged[(j,8)] = age
        i = i + 1
    else:
        merged[(j,7)] = np.nan 
        merged[(j,8)] = np.nan 
        
    merged[(j,9)] = latency[j]
    merged[(j,10)] = cost[j]
    merged[(j,11)] = reliability[j]

            
        
            


# In[109]:


#saving
np.savetxt("merged.csv", merged, delimiter=",", header="month,day,hour,minute,second,server,tactic,ping,age of ping(seconds),latency,cost,reliability")


# In[ ]:




