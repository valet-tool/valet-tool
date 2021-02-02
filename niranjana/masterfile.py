#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:07:09 2021

@author: nd7896
"""
import math
import numpy as np
import pandas as pd
from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from datetime import datetime
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVR
from sklearn.multioutput import MultiOutputRegressor
from sklearn.neighbors import KNeighborsRegressor


# Function for converting series data to a supervised data of format, t-1, t, t+1
## Basically feeding in the (t-1)th data to predict the t data
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

def getColumnNames(column_names, server, tactic):
    column_names = list(column_names)
    
    #column_names = [column_names[-3:], column_names[:-3]]
    #dataset = dataset[column_names]
    
    columns_arr = ["" for k in column_names]
    
    for ind in range(0, len(column_names)):
        app_str = "_server_"+str(server)+"_tactic_"+str(tactic)
        columns_arr[ind] = str(column_names[ind]) + app_str
        

    #dataset.columns = columns_arr
    #columns_drop = ["timestamp", "ping_timestamp"]
    #dataset.drop(columns_drop)
    #columns_arr = [columns_arr[-3:], columns_arr[:-3]]
        
    return columns_arr

def createMasterFrame(num_servers, num_tactics):
    cols = ["timestamp", "ping_timestamp", "ping_success"]
    count = -1
    for i in num_servers:
        for j in num_tactics:
            count = count + 1
            print("I:", i, "J", j)
            train_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_train.csv"
            test_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_test.csv"
            
            if count==0:#i == 1 and j == 1:

                train_frame = pd.read_csv(train_filename)
                #train_frame = break_timestamp(train_frame)
                train_frame = train_frame.drop(columns=cols)
                new_columns_train = getColumnNames(train_frame.columns, i ,j)
                #train_frame = train_frame[new_columns_train]
                train_frame.columns = new_columns_train
                
                test_frame = pd.read_csv(test_filename)
                #test_frame = break_timestamp(test_frame)
                test_frame = test_frame.drop(columns=cols)
                new_columns_test = getColumnNames(test_frame.columns, i ,j)
                #test_frame = test_frame[new_columns_test]
                test_frame.columns = new_columns_test
                
            else:

                train_data = pd.read_csv(train_filename)
                train_data = train_data.drop(columns=cols)
                #train_data = break_timestamp(train_data)
                train_frame = pd.concat([train_frame, train_data],axis=1)
                new_columns_train += getColumnNames(train_data.columns, i, j) 
                #train_frame = train_frame[new_columns_train]
                train_frame.columns = new_columns_train
                
                test_data = pd.read_csv(test_filename)
                test_data = test_data.drop(columns=cols)
                #test_data = break_timestamp(test_data)
                test_frame = pd.concat([test_frame, test_data], axis=1)
                new_columns_test += getColumnNames(test_data.columns, i, j) 
                #test_frame = test_frame[new_columns_test]
                test_frame.columns = new_columns_test
    
    return train_frame, test_frame

def break_timestamp(dataset):
    temp_time = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f") for d in dataset["timestamp"]]
    dataset["hours"] = [dh.hour for dh in temp_time]
    dataset["minutes"] = [dm.minute for dm in temp_time]
    dataset["seconds"] = [ds.second for ds in temp_time]

    temp_time = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f") for d in dataset["ping_timestamp"] if type(d)==str]
    dataset["ping_hours"] = [dh.hour for dh in temp_time]
    dataset["ping_minutes"] = [dm.minute for dm in temp_time]
    dataset["ping_seconds"] = [ds.second for ds in temp_time]
    
    for i in range(0, len(dataset)):
    	d = dataset["ping_timestamp"]
    	if type(d) == str:
    		temp_time = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")
    		dataset["ping_hours"].iloc[i] = [temp_time.hour]
    		dataset["ping_minutes"].iloc[i] = [temp_time.minute]
    		dataset["ping_seconds"].iloc[i] = [temp_time.second]

    return dataset


if __name__=="__main__":
    #first ieration is plain with ping data
    #second iteration is with all servers data
    #TODO: ADD other models
    mlp_models_results = pd.DataFrame(columns = ["RMSE","MSE", "MAE"] , index = ["Plain Ping", "All Servers"])
    lstm_models_results = pd.DataFrame(columns = ["RMSE","MSE", "MAE"] , index = ["Plain Ping", "All Servers"])
    svr_rbf_models_results = pd.DataFrame(columns = ["RMSE","MSE", "MAE"] , index = ["Plain Ping", "All Servers"])
    svr_linear_models_results = pd.DataFrame(columns = ["RMSE","MSE", "MAE"] , index = ["Plain Ping", "All Servers"])
    kNN_models_results = pd.DataFrame(columns = ["RMSE","MSE", "MAE"] , index = ["Plain Ping", "All Servers"])
    for iterations in range(0,2):
        tactics = [1]
        if iterations==0:
            
            servers = [1] 
            train_master_dataframe, test_master_dataframe = createMasterFrame(servers, tactics)
            # load dataset
            dataset = train_master_dataframe #.values
            values = dataset.values
            
            values_validation = test_master_dataframe.values
            
            
            ## Calling the function to do the preprocessing the data and removing unwanted columns
            
            
            # frame as supervised learning
            reframed = series_to_supervised(values, 1, 1)
            reframed_validation = series_to_supervised(values_validation, 1, 1)
            # drop columns we don't want to predict
            reframed.drop(reframed.columns[[6,10,11]], axis=1, inplace=True)
            reframed_validation.drop(reframed_validation.columns[[6,10,11]], axis=1, inplace=True)
            print(reframed.head(1))
            
            ## Splitting the data into training and validation sets
            
            
            train = reframed.values
            test = reframed_validation.values
            # split into input and outputs
            train_X, train_y = train[:, :-3], train[:,-3:]
            test_X, test_y = test[:, :-3], test[:,-3:]
            # reshape input to be 3D [samples, timesteps, features]
            train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
            test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
            print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
            
            
            ## Run this cell for MLP , else Run the next cell for LSTM
            
            # flatten input
            n_input = train_X.shape[1] * train_X.shape[2]
            X = train_X.reshape((train_X.shape[0], n_input))
            
            test_dataset= test_master_dataframe #test_dataset.drop(columns=["timestamp","ping_timestamp","ping_success"])
            test_values = test_dataset.values
            reframed_test = series_to_supervised(test_values, 1, 1)
            reframed_test.drop(reframed_test.columns[[6,10,11]], axis=1, inplace=True)
            testset = reframed_test.values
            testset_X, testset_y = testset[:, :-3], testset[:,-3:]
            testdataReshaped = test_X #testset_X.reshape((testset_X.shape[0], 1, testset_X.shape[1]))
            testset_y = test_y


        elif iterations==1:
            
            servers = np.arange(2,4)
            train_master_dataframe_temp, test_master_dataframe_temp = createMasterFrame(servers, tactics)
            train_master_dataframe = pd.concat([reframed, train_master_dataframe_temp], axis = 1)
            test_master_dataframe = pd.concat([reframed_validation, test_master_dataframe_temp], axis = 1)

    #servers = np.arange(1,4)
    #tactics = [1]#np.arange(1,6)
    #cols_orig = ["timestamp", "time_since_last_recording", "latency", "cost", "reliability", "ping_timestamp", "time_since_last_ping", "ping_success", "ping_time"]
        

       
        # define MLP model
        model = Sequential()
        model.add(Dense(100, activation='relu', input_dim=n_input))
        model.add(Dense(3))
        model.compile(optimizer='adam', loss='mse')
        history= model.fit(X, train_y, epochs=20, verbose=1)
        # plot history
        pyplot.plot(history.history['loss'], label='train')
        pyplot.legend()
        pyplot.show()
    
        


        ## For MLP use below line only
        yhat = model.predict(testset_X)
    
        print(yhat)
        dataset_results_mlp = pd.DataFrame({'predicted_Latency': yhat[:, 0], 'predicted_Cost': yhat[:, 1],
                           'predicted_Reliability': yhat[:, 2]})
        dataset_results_mlp['predicted_Reliability'].loc[dataset_results_mlp['predicted_Reliability'] >0.5] = 1
        dataset_results_mlp['predicted_Reliability'].loc[dataset_results_mlp['predicted_Reliability'] <0.5] = 0
    
    
        frames = [test_dataset, dataset_results_mlp]
        result_mlp = pd.concat(frames,axis =1)
    
        ## Finding the root mean squared error of the model
    
        rmse = sqrt(mean_squared_error(yhat, testset_y))
        print('Test RMSE for MLP: ' , rmse)
    
        mse = mean_squared_error(yhat, testset_y)
        print('Test MSE for MLP: ',  mse)
    
        mae = mean_absolute_error(yhat, testset_y)
        print('Test MAE for MLP: ',  mae)
        
        mlp_models_results["RMSE"].iloc[iterations] = rmse
        mlp_models_results["MSE"].iloc[iterations] = mse
        mlp_models_results["MAE"].iloc[iterations] = mae
        
        
        
        #################################################################################
        # design LSTM network  has 1000 hidden layers , used adam optimizer and mse loss function
        model = Sequential()
        model.add(LSTM(1000, input_shape=(train_X.shape[1], train_X.shape[2])))
        model.add(Dense(3))
        
        print(model.summary())
        
        model.compile(loss='mse', optimizer='adam')
        # fit network
        history = model.fit(train_X, train_y, epochs=20, batch_size=72, validation_data=(test_X, test_y), verbose=1, shuffle=False)
        # plot history
        pyplot.plot(history.history['loss'], label='train')
        pyplot.plot(history.history['val_loss'], label='test')
        pyplot.legend()
        pyplot.show()
        
#        test_dataset = test_master_dataframe
#        #test_dataset= test_dataset.drop(columns=["timestamp","ping_timestamp","ping_success"])
#        #print(test_dataset.head())
#        test_values = test_dataset.values
#        reframed_test = series_to_supervised(test_values, 1, 1)
#        reframed_test.drop(reframed_test.columns[[6,10,11]], axis=1, inplace=True)
#        testset = reframed_test.values
#        testset_X, testset_y = testset[:, :-3], testset[:,-3:]
#        testdataReshaped = testset_X.reshape((testset_X.shape[0], 1, testset_X.shape[1]))
#        print(testset_X.shape, testset_X.shape)
        
        yhat = model.predict(test_X)

        print(yhat)
        dataset_results_lstm = pd.DataFrame({'predicted_Latency': yhat[:, 0], 'predicted_Cost': yhat[:, 1],
                               'predicted_Reliability': yhat[:, 2]})
        dataset_results_lstm['predicted_Reliability'].loc[dataset_results_lstm['predicted_Reliability'] >0.5] = 1
        dataset_results_lstm['predicted_Reliability'].loc[dataset_results_lstm['predicted_Reliability'] <0.5] = 0
        
        frames = [test_dataset, dataset_results_mlp, dataset_results_lstm]
        result_lstm = pd.concat(frames,axis =1)
    
        ## Finding the root mean squared error of the model
    
        rmse = sqrt(mean_squared_error(yhat, testset_y))
        print('Test RMSE for LSTM: ' , rmse)
    
        mse = mean_squared_error(yhat, testset_y)
        print('Test MSE for LSTM: ',  mse)
    
        mae = mean_absolute_error(yhat, testset_y)
        print('Test MAE for LSTM: ',  mae)
        
        lstm_models_results["RMSE"].iloc[iterations] = rmse
        lstm_models_results["MSE"].iloc[iterations] = mse
        lstm_models_results["MAE"].iloc[iterations] = mae
        
        
        
        ###############################################################
        regressor = SVR(kernel='rbf')
        # flatten input
        tesetdataReshaped = test_X
        n_input = testdataReshaped.shape[1] * testdataReshaped.shape[2]
        X2 = testdataReshaped.reshape((testdataReshaped.shape[0], n_input))
        regr = MultiOutputRegressor(regressor)
        
        regr.fit(X,train_y)
        out= regr.predict(X2)
        
        rmse = sqrt(mean_squared_error(out,testset_y))
        print('Test RMSE for SVR RBF: ' , rmse)
        
        mse = mean_squared_error(out,testset_y)
        print('Test MSE for SVR RBF: ' , mse)
        
        mae = mean_absolute_error(out,testset_y)
        print('Test MSE for SVR RBF: ' , mae)
        
        
        svr_rbf_models_results["RMSE"].iloc[iterations] = rmse
        svr_rbf_models_results["MSE"].iloc[iterations] = mse
        svr_rbf_models_results["MAE"].iloc[iterations] = mae
        
        
        ##########################################################
        regressor = SVR(kernel='linear')
        # flatten input
        tesetdataReshaped = test_X
        n_input = testdataReshaped.shape[1] * testdataReshaped.shape[2]
        X2 = testdataReshaped.reshape((testdataReshaped.shape[0], n_input))
        regr = MultiOutputRegressor(regressor)
        regr.fit(X,train_y)
        out= regr.predict(X2)
        
        rmse = sqrt(mean_squared_error(out,testset_y))
        print('Test RMSE for SVR Linear: ' , rmse)
        
        mse = mean_squared_error(out,testset_y)
        print('Test MSE for SVR Linear: ' , mse)
        
        mae = mean_absolute_error(out,testset_y)
        print('Test MSE for SVR Linear: ' , mae)
        
        
        svr_linear_models_results["RMSE"].iloc[iterations] = rmse
        svr_linear_models_results["MSE"].iloc[iterations] = mse
        svr_linear_models_results["MAE"].iloc[iterations] = mae
        
        ###########################################################
        
        knn = KNeighborsRegressor()
        regr_knn = MultiOutputRegressor(knn)

        # flatten input
        tesetdataReshaped = test_X
        n_input = testdataReshaped.shape[1] * testdataReshaped.shape[2]
        X2 = testdataReshaped.reshape((testdataReshaped.shape[0], n_input))

        regr_knn.fit(X,train_y)
        regr_knn.predict(testset_X)
        out= regr_knn.predict(X2)
        
        rmse = sqrt(mean_squared_error(out,testset_y))
        print('Test RMSE for kNN: ' , rmse)
        
        mse = mean_squared_error(out,testset_y)
        print('Test MSE for kNN: ' , mse)
        
        mae = mean_absolute_error(out,testset_y)
        print('Test MSE for kNN: ' , mae)
        
        
        kNN_models_results["RMSE"].iloc[iterations] = rmse
        kNN_models_results["MSE"].iloc[iterations] = mse
        kNN_models_results["MAE"].iloc[iterations] = mae
        
        
        
    train_master_dataframe.to_pickle("results/train_master_dataframe.pkl")
    test_master_dataframe.to_pickle("results/test_master_dataframe.pkl")
    svr_rbf_models_results.to_pickle("results/svr_rbf_results.pkl")
    svr_linear_models_results.to_pickle("results/svr_linear_results.pkl")
    kNN_models_results.to_pickle("results/kNN_results.pkl")
    mlp_models_results.to_pickle("results/mlp_results.pkl")
    lstm_models_results.to_pickle("results/lstm_results.pkl")


    #dataset = break_timestamp(dataset)
    #dataset= dataset.drop(columns=col_arr)#["ID"])
    #dataset = dataset[["hours","minutes","seconds","latency","cost","reliability"]]
    #norm_scaler = Normalizer().fit(dataset.iloc[:,0:3])
    #dataset.loc[:,0:3] = norm_scaler.transform(dataset.iloc[:,0:3])
    
    
    #data_1 = pd.read_csv("/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_1_tactic_1_train.csv")
    #data_2 = pd.read_csv("/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_2_tactic_1_train.csv")
    #data_3 = pd.read_csv("/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_1_tactic_2_train.csv")
    
    #indices_1 = [data_1["timestamp"].iloc[:].values == data_2["timestamp"].iloc[:].values)]
    
    #indices_2 = data_1["timestamp"].iloc[:].values == data_3["timestamp"].iloc[:].values)
