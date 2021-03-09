library(forecast)
library(ggplot2)
library(gridExtra)
setwd("C:/MachineLearningWork")

#manually change the data source for different servers/tactics
data = read.csv("server8tactic1.csv")
myLatency = data[,c(1,2)]
myCost = data[,c(1,3)]

trainC = myCost[1:267,]
trainL = myLatency[1:267,]
#use these for tactic 1, as it assumes a daily cycle
fitLatency <- auto.arima(ts(trainL[,2],frequency=24),D=1)
fitCost <- auto.arima(ts(trainC[,2],frequency=24),D=1)

#use these for tactics 2-5
fitLatency <- auto.arima(ts(trainL[,2]))
fitCost <- auto.arima(ts(trainC[,2]))


forecasted_dataL = forecast(fitLatency, h = 70)
plot(forecasted_dataL) # not necessary
forecasted_dataC = forecast(fitCost, h = 70)
plot(forecasted_dataC) #not necessary 
plot(forecast(auto.arima(ts(train[,2],frequency=24),D=1),h=35))
write.csv(forecasted_dataL, file = "s8t1pL.csv") #adjust names manually
write.csv(forecasted_dataC, file = "s8t1pC.csv") #adjust names manually


