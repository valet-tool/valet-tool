The folders 1, 2 and 3 designate the server number. 


All files with raw_results in it are the predictions for the test set. Files of the format *_results.pkl contain the error metric measures. 

MLP and LSTM were run 10 times. The model run is demoted in the file name as *_model_(trial number). Every run of MLP is saved to file raw_results_mlp*.csv and LSTM in raw_results_lstm.
There are 5 iterations in master_file.py. Every raw_results file has _iteration_(iteration number) in its name. The iterations are as follows - 

Iteration 0: Plain ping data
Iteration 1: All servers ping data
Iteration 2: 5 sampling rate
Iteration 3: 10 sampling rate
Iteration 4: 20 sampling rate




