#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:07:09 2021

@author: nd7896
"""
import math
import numpy as np
from collections import deque
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

def createMasterFrame(num_servers, num_tactics, base_path_parts = None):
    cols = ["timestamp", "ping_timestamp", "ping_success"]
    count = -1
    for i in num_servers:
        for j in num_tactics:
            count = count + 1
            print("I:", i, "J", j)
            
            if base_path_parts:
                train_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics_weekend_sample_rate/"+str(base_path_parts[0])+"normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_train_weekdayOneHot"+str(base_path_parts[1])+".csv"
                
                test_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics_weekend_sample_rate/"+str(base_path_parts[0])+"normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_test_weekdayOneHot"+str(base_path_parts[1])+".csv"
                
                validation_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics_weekend_sample_rate/"+str(base_path_parts[0])+"normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_validation_weekdayOneHot"+str(base_path_parts[1])+".csv"
            else:
                train_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics_weekend_sample_rate/normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_train_weekdayOneHot.csv"
                #"/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_train.csv"
                test_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics_weekend_sample_rate/normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_test_weekdayOneHot.csv"
                validation_filename = "/home/nd7896/data/TVA_E/valet-tool/parse_tactics_weekend_sample_rate/normalized_tva_server_"+str(i)+"_tactic_"+str(j)+"_validation_weekdayOneHot.csv"
            
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
                
                
                validation_frame = pd.read_csv(validation_filename)
                #test_frame = break_timestamp(test_frame)
                validation_frame = validation_frame.drop(columns=cols)
                new_columns_validation = getColumnNames(validation_frame.columns, i ,j)
                #test_frame = test_frame[new_columns_test]
                validation_frame.columns = new_columns_validation
                
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
                
                validation_data = pd.read_csv(validation_filename)
                validation_data = validation_data.drop(columns=cols)
                #test_data = break_timestamp(test_data)
                validation_frame = pd.concat([validation_frame, validation_data], axis=1)
                new_columns_validation += getColumnNames(validation_data.columns, i, j) 
                #test_frame = test_frame[new_columns_test]
                validation_frame.columns = new_columns_validation
    
    return train_frame, test_frame, validation_frame

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

    model_trials = 10
    base_columns = ["RMSE","MSE", "MAE"]
    columns_w_trials = []
    
    for i in range(0, model_trials):
        #mod_columns = []
        for j in range(0, len(base_columns)):
            columns_w_trials.append(base_columns[j] +" " +str(i))
        #columns_w_trials.append(mod_columns)
    
    
    mlp_models_results = pd.DataFrame(columns = columns_w_trials , index = ["Plain Ping", "All Servers", "5 sample Sampling Rate", "10 sample Sampling Rate", "20 sample Sampling Rate"])
    lstm_models_results = pd.DataFrame(columns = columns_w_trials , index = ["Plain Ping", "All Servers","5 sample Sampling Rate", "10 sample Sampling Rate", "20 sample Sampling Rate"])
    
    svr_rbf_models_results = pd.DataFrame(columns = base_columns , index = ["Plain Ping", "All Servers","5 sample Sampling Rate", "10 sample Sampling Rate", "20 sample Sampling Rate"])
    svr_linear_models_results = pd.DataFrame(columns = base_columns , index = ["Plain Ping", "All Servers","5 sample Sampling Rate", "10 sample Sampling Rate", "20 sample Sampling Rate"])
    kNN_models_results = pd.DataFrame(columns = base_columns , index = ["Plain Ping", "All Servers","5 sample Sampling Rate", "10 sample Sampling Rate", "20 sample Sampling Rate"])
    
    server_to_predict = np.arange(1,4)
    
    for curr_server in server_to_predict:
        
        for iterations in range(-1,0):#(-1,5):
            #Iteration 0: Plain ping data
            #Iteration 1: All servers ping data
            #Iteration 2: 5 sampling rate
            #Iteration 3: 10 sampling rate
            #Iteration 4: 20 sampling rate
            tactics = [1]
            if iterations<=0:
                
                servers = [curr_server]#[1] 
                
                
                train_master_dataframe, test_master_dataframe, validation_master_dataframe = createMasterFrame(servers, tactics)
                # load dataset
                dataset = train_master_dataframe #.values
                values = dataset.values
                
                values_validation = validation_master_dataframe.values#test_master_dataframe.values
                
                values_test = test_master_dataframe.values
                
                
                
                temp=[]
                original_indices = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                columns_to_remove = [int(val + train_master_dataframe.shape[1]) for val in original_indices]
                
                if iterations==-1:
                    additional_columns_to_remove = [4, 5]
                else:
                    additional_columns_to_remove = None
                
                if additional_columns_to_remove != None:
                    columns_to_remove += additional_columns_to_remove
                    
                
                
                
                ## Calling the function to do the preprocessing the data and removing unwanted columns
                
                #0,4,5
                #[13, 17, 18]
                # frame as supervised learning
                reframed = series_to_supervised(values, 1, 1)
                reframed_validation = series_to_supervised(values_validation, 1, 1)
                reframed_test = series_to_supervised(values_test, 1, 1)
                # drop columns we don't want to predict
                reframed.drop(reframed.columns[columns_to_remove], axis=1, inplace=True)
                reframed_validation.drop(reframed_validation.columns[columns_to_remove], axis=1, inplace=True)
                reframed_test.drop(reframed_test.columns[columns_to_remove], axis=1, inplace=True)
                print(reframed.head(1))
                
                
                
                ## Splitting the data into training and validation sets
                
                
                train = reframed.values
                valid = reframed_validation.values
                test = reframed_test.values
                
                predict_columns = [14, 15, 16]
                feature_columns = [ind for ind in range(0,train.shape[1]) if ind not in predict_columns]
                
                # split into input and outputs
                train_X, train_y = train[:, feature_columns], train[:,-len(predict_columns):]
                valid_X, valid_y = valid[:, feature_columns], valid[:,-len(predict_columns):]
                test_X, test_y = test[:, feature_columns], test[:,-len(predict_columns):]
                # reshape input to be 3D [samples, timesteps, features]
                train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
                valid_X = valid_X.reshape((valid_X.shape[0], 1, valid_X.shape[1]))
                test_X_prior = test_X
    
                test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
                print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape, test_X.shape, test_y.shape)
                
                
                
                # flatten input
                n_input = train_X.shape[1] * train_X.shape[2]
                X = train_X.reshape((train_X.shape[0], n_input))
                
                test_dataset = test_master_dataframe #test_dataset.drop(columns=["timestamp","ping_timestamp","ping_success"])
                # test_values = test_dataset.values
                
                # reframed_test = series_to_supervised(test_values, 1, 1)
                # reframed_test.drop(reframed_test.columns[[6,10,11]], axis=1, inplace=True)
                # testset = reframed_test.values
                # testset_X, testset_y = testset[:, :-3], testset[:,-3:]
                testdataReshaped = test_X
                testset_X, testset_y = test_X_prior, test_y
                #testset_X.reshape((testset_X.shape[0], 1, testset_X.shape[1]))
    
    
            else:
                
                base_path_parts = None
                # servers = np.arange(1,4)
                
                # server_arr = deque(servers)
                # while server_arr[0] != curr_server:
                #     server_arr.rotate(1)
                # servers = list(server_arr)
                
                servers = [curr_server]
                
                if iterations!=1:
                    if iterations==2:
                        sample_rate = 5
                    elif iterations==3:
                        sample_rate = 10
                    elif iterations==4:
                        sample_rate = 20
                    
                    base_path_parts = ["sampleRate/","sample_rate_"+str(sample_rate)]
                
                # train_master_dataframe = pd.concat([reframed, train_master_dataframe_temp], axis = 1)
                # validation_master_dataframe = pd.concat([reframed_validation, validation_master_dataframe_temp], axis = 1)
                # test_master_dataframe = pd.concat([reframed_test, test_master_dataframe_temp], axis = 1)
                # load dataset
                train_master_dataframe, test_master_dataframe, validation_master_dataframe = createMasterFrame(servers, tactics, base_path_parts)
                
                dataset = train_master_dataframe #.values
                values = dataset.values
                
                values_validation = validation_master_dataframe.values#test_master_dataframe.values
                
                values_test = test_master_dataframe.values
                
                
                ## Calling the function to do the preprocessing the data and removing unwanted columns
                temp=[]
                original_indices = [0, 4, 5, 6, 7, 8, 9, 10 , 11, 12]
                #updating original indices for 3 servers
                # for i in range(0, len(servers)):
                #     if i!=0:
                #         temp_indices = [val+i*(train_master_dataframe.shape[1]/len(servers)-1) for val in original_indices]
                #         temp+=temp_indices
                # original_indices+=temp
                #pushing the original indices to remove in shifted frame    
                columns_to_remove = [int(val + train_master_dataframe.shape[1]) for val in original_indices]
                
                if iterations!=1:
                    #dropping ping pdata columns for sampling rate iterations
                    columns_to_remove.append(4)
                    columns_to_remove.append(5)
                    
                
                        
                        
                #+12, 3 times
                #Original indices:[0, 4, 5, 13, 17, 18, 26, 30, 31, 37, 41, 42]
                # frame as supervised learning
                reframed = series_to_supervised(values, 1, 1)
                reframed_validation = series_to_supervised(values_validation, 1, 1)
                reframed_test = series_to_supervised(values_test, 1, 1)
                # drop columns we don't want to predict
                reframed.drop(reframed.columns[columns_to_remove], axis=1, inplace=True)
                reframed_validation.drop(reframed_validation.columns[columns_to_remove], axis=1, inplace=True)
                reframed_test.drop(reframed_test.columns[columns_to_remove], axis=1, inplace=True)
                print(reframed.head(1))
                
                ## Splitting the data into training and validation sets
                
                
                train = reframed.values
                valid = reframed_validation.values
                test = reframed_test.values
                # split into input and outputs
                #[39, 40, 41]
                #predict_columns = [14, 15, 16]#[39, 40, 41]
                #feature_columns = [ind for ind in range(0,train.shape[1]) if ind not in predict_columns]
                
                train_X, train_y = train[:, feature_columns], train[:,-len(predict_columns):]
                valid_X, valid_y = valid[:, feature_columns], valid[:,-len(predict_columns):]
                test_X, test_y = test[:, feature_columns], test[:,-len(predict_columns):]
                # reshape input to be 3D [samples, timesteps, features]
                train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
                valid_X = valid_X.reshape((valid_X.shape[0], 1, valid_X.shape[1]))
                test_X_prior = test_X
                test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
                print(train_X.shape, train_y.shape, valid_X.shape, valid_y.shape, test_X.shape, test_y.shape)
                
                
                
                # flatten input
                n_input = train_X.shape[1] * train_X.shape[2]
                X = train_X.reshape((train_X.shape[0], n_input))
                
                test_dataset = test_master_dataframe #test_dataset.drop(columns=["timestamp","ping_timestamp","ping_success"])
                #test_values = test_dataset.values
                
                #reframed_test = series_to_supervised(test_values, 1, 1)
                #reframed_test.drop(reframed_test.columns[[6,10,11]], axis=1, inplace=True)
                #testset = reframed_test.values
                #testset_X, testset_y = testset[:, :-3], testset[:,-3:]
                testset_X, testset_y = test_X_prior, test_y
                testdataReshaped = test_X
                #testset_X.reshape((testset_X.shape[0], 1, testset_X.shape[1]))
    

            
    
    
            ## For MLP use below line only
            
            for z in range(0, model_trials):
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
            
                yhat = model.predict(testset_X)
            
                #print(yhat)
                dataset_results_mlp = pd.DataFrame({'predicted_Latency'+" "+str(z): yhat[:, 0], 'predicted_Cost'+" "+str(z): yhat[:, 1],
                                   'predicted_Reliability'+" "+str(z): yhat[:, 2]})
                dataset_results_mlp['predicted_Reliability'+" "+str(z)].loc[dataset_results_mlp['predicted_Reliability'+" "+str(z)] >0.5] = 1
                dataset_results_mlp['predicted_Reliability'+" "+str(z)].loc[dataset_results_mlp['predicted_Reliability'+" "+str(z)] <0.5] = 0
            
            
                frames = [test_dataset, dataset_results_mlp]
                result_mlp = pd.concat(frames,axis =1)
    
                ## Finding the root mean squared error of the model
            
                rmse = sqrt(mean_squared_error(yhat, testset_y))
                print('Test RMSE for MLP'+" "+str(z) , rmse)
            
                mse = mean_squared_error(yhat, testset_y)
                print('Test MSE for MLP'+" "+str(z),  mse)
            
                mae = mean_absolute_error(yhat, testset_y)
                print('Test MAE for MLP'+" "+str(z),  mae)
                
                mlp_models_results["RMSE"+" "+str(z)].iloc[iterations] = rmse
                mlp_models_results["MSE"+" "+str(z)].iloc[iterations] = mse
                mlp_models_results["MAE"+" "+str(z)].iloc[iterations] = mae
                
                #result_mlp.to_pickle("results/"+str(curr_server)+"/raw_results_mlp"+" "+str(z)+".pkl")
                result_mlp.to_csv("results/"+str(curr_server)+"/raw_results_mlp"+"_model_"+str(z)+"_iteration_"+str(iterations)+".csv")
            
            #################################################################################
            # design LSTM network with variable architectures, use adam optimizer and mse loss function
            '''
            To start:
            Architecture 1: LSTM with 1000 nodes in the hidden layer
            Architecture 2: LSTM with 3 layers containing 100 nodes each
            Architecture 3: LSTM with 3 layers of 10 nodes each
            '''
            for idx in range(0, 4):
                if idx == 0:       
                    model = Sequential()
                    model.add(LSTM(1000, input_shape=(train_X.shape[1], train_X.shape[2])))
                    model.add(Dense(3))
                elif idx == 1:
                    model = Sequential()
                    model.add(LSTM(100, return_sequences=True, input_shape=(train_X.shape[1], train_X.shape[2])))
                    model.add(LSTM(100, return_sequences=True))
                    model.add(LSTM(100))
                    model.add(Dense(3))
                elif idx == 2:
                    model = Sequential()
                    model.add(LSTM(10, return_sequences=True, input_shape=(train_X.shape[1], train_X.shape[2])))
                    model.add(LSTM(10, return_sequences=True))
                    model.add(LSTM(10))
                    model.add(Dense(3))
                elif idx == 3:
                    model = Sequential()
                    model.add(LSTM(100, return_sequences=True, input_shape=(train_X.shape[1], train_X.shape[2])))
                    model.add(LSTM(100))
                    model.add(Dense(3))
            
                
                base_model = model
                for z in range(0, model_trials):
                    
                    #print("LSTM model summary",model.summary())
                    model = base_model
                    model.compile(loss='mse', optimizer='adam')
                    # fit network
                    history = model.fit(train_X, train_y, epochs=20, batch_size=72, validation_data=(test_X, test_y), verbose=1, shuffle=False)
                    # plot history
                    pyplot.plot(history.history['loss'], label='train')
                    pyplot.plot(history.history['val_loss'], label='test')
                    pyplot.legend()
                    pyplot.show()
                    
                    yhat = model.predict(test_X)
            
                    #print(yhat)
                    dataset_results_lstm = pd.DataFrame({'predicted_Latency'+" "+str(z): yhat[:, 0], 'predicted_Cost'+" "+str(z): yhat[:, 1],
                                           'predicted_Reliability'+" "+str(z): yhat[:, 2]})
                    dataset_results_lstm['predicted_Reliability'+" "+str(z)].loc[dataset_results_lstm['predicted_Reliability'+" "+str(z)] >0.5] = 1
                    dataset_results_lstm['predicted_Reliability'+" "+str(z)].loc[dataset_results_lstm['predicted_Reliability'+" "+str(z)] <0.5] = 0
                    
                    frames = [test_dataset, dataset_results_lstm]
                    result_lstm = pd.concat(frames,axis =1)
                
                    ## Finding the root mean squared error of the model
                
                    rmse = sqrt(mean_squared_error(yhat, testset_y))
                    print('Test RMSE for LSTM ',str(idx),":" , rmse)
                
                    mse = mean_squared_error(yhat, testset_y)
                    print('Test MSE for LSTM ', str(idx),":",  mse)
                
                    mae = mean_absolute_error(yhat, testset_y)
                    print('Test MAE for LSTM ', str(idx),":",  mae)
                    
                    lstm_models_results["RMSE"+" "+str(z)].iloc[iterations] = rmse
                    lstm_models_results["MSE"+" "+str(z)].iloc[iterations] = mse
                    lstm_models_results["MAE"+" "+str(z)].iloc[iterations] = mae
                    name = "results/"+str(curr_server)+"/error_measures/lstm_results_model_"+str(idx)+"_model_"+str(z)+"_iteration"+str(iterations)+".pkl"
                    # lstm_models_results.to_pickle(name)
                    # result_lstm.to_pickle("results/"+str(curr_server)+"/raw_results_lstm_"+str(idx)+" "+str(z)+".pkl")
                    
                    lstm_models_results.to_csv(name)
                    result_lstm.to_csv("results/"+str(curr_server)+"/raw_results_lstm_"+str(idx)+"_model_"+str(z)+"_iteration_"+str(iterations)+".csv")
    
            
            
            ###############################################################
            regressor = SVR(kernel='rbf')
            # flatten input
            #tesetdataReshaped = test_X
            n_input = testdataReshaped.shape[1] * testdataReshaped.shape[2]
            X2 = testdataReshaped.reshape((testdataReshaped.shape[0], n_input))
            regr = MultiOutputRegressor(regressor)
            
            regr.fit(X,train_y)
            out= regr.predict(X2)
            svr_rbf = out
            rmse = sqrt(mean_squared_error(out,testset_y))
            print('Test RMSE for SVR RBF: ' , rmse)
            
            mse = mean_squared_error(out,testset_y)
            print('Test MSE for SVR RBF: ' , mse)
            
            mae = mean_absolute_error(out,testset_y)
            print('Test MSE for SVR RBF: ' , mae)
            
            
            svr_rbf_models_results["RMSE"].iloc[iterations] = rmse
            svr_rbf_models_results["MSE"].iloc[iterations] = mse
            svr_rbf_models_results["MAE"].iloc[iterations] = mae
            
            #svr_rbf.savetxt("results/"+str(curr_server)+"/raw_results_svr_rbf.csv")
            np.save("results/"+str(curr_server)+"/raw_results_svr_rbf_iteration_"+str(iterations),svr_rbf)
            ##########################################################
            regressor = SVR(kernel='linear')
            # flatten input
            tesetdataReshaped = test_X
            n_input = testdataReshaped.shape[1] * testdataReshaped.shape[2]
            X2 = testdataReshaped.reshape((testdataReshaped.shape[0], n_input))
            regr = MultiOutputRegressor(regressor)
            regr.fit(X,train_y)
            out= regr.predict(X2)
            
            svr_linear = out
            rmse = sqrt(mean_squared_error(out,testset_y))
            print('Test RMSE for SVR Linear: ' , rmse)
            
            mse = mean_squared_error(out,testset_y)
            print('Test MSE for SVR Linear: ' , mse)
            
            mae = mean_absolute_error(out,testset_y)
            print('Test MSE for SVR Linear: ' , mae)
            
            
            svr_linear_models_results["RMSE"].iloc[iterations] = rmse
            svr_linear_models_results["MSE"].iloc[iterations] = mse
            svr_linear_models_results["MAE"].iloc[iterations] = mae
            
            #svr_linear.savetxt("results/"+str(curr_server)+"/raw_results_svr_linear.pkl")
            np.save("results/"+str(curr_server)+"/raw_results_svr_linear_iterations"+str(iterations),svr_linear)
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
            knn_out = out
            rmse = sqrt(mean_squared_error(out,testset_y))
            print('Test RMSE for kNN: ' , rmse)
            
            mse = mean_squared_error(out,testset_y)
            print('Test MSE for kNN: ' , mse)
            
            mae = mean_absolute_error(out,testset_y)
            print('Test MSE for kNN: ' , mae)
            
            
            kNN_models_results["RMSE"].iloc[iterations] = rmse
            kNN_models_results["MSE"].iloc[iterations] = mse
            kNN_models_results["MAE"].iloc[iterations] = mae
            #knn_out.save("results/"+str(curr_server)+"/raw_results_kNN.pkl")
            np.save("results/"+str(curr_server)+"/raw_results_kNN_iterations_"+str(iterations),knn_out)

            svr_rbf_models_results.to_csv("results/"+str(curr_server)+"/error_measures/"+"svr_rbf_results"+"_iterations_"+str(iterations)+".csv")
            svr_linear_models_results.to_csv("results/"+str(curr_server)+"/error_measures/"+"svr_linear_results"+"_iterations_"+str(iterations)+".csv")
            kNN_models_results.to_csv("results/"+str(curr_server)+"/error_measures/kNN_results"+"_iterations_"+str(iterations)+".csv")
    
            mlp_models_results.to_csv("results/"+str(curr_server)+"/error_measures"+"_iterations_"+str(iterations)+"mlp_results"+" "+str(z)+".csv")
            
        train_master_dataframe.to_pickle("results/"+str(curr_server)+"/train_master_dataframe.pkl")
        test_master_dataframe.to_pickle("results/"+str(curr_server)+"/test_master_dataframe.pkl")
        
        # svr_rbf_models_results.to_pickle("results/"+str(curr_server)+"/svr_rbf_results.pkl")
        # svr_linear_models_results.to_pickle("results/"+str(curr_server)+"/svr_linear_results.pkl")
        # kNN_models_results.to_pickle("results/"+str(curr_server)+"/kNN_results.pkl")
    
        # mlp_models_results.to_pickle("results/"+str(curr_server)+"/mlp_results"+" "+str(z)+".pkl")
        #name = "results/"+str(curr_server)+"/"+"_iterations"+str(iterations)+"svr_rbf_results.csv"
        #

    