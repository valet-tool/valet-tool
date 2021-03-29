The folders 1, 2 and 3 designate the server number. 
Each folder contains within it the following files - 

 kNN_results.pkl            raw_results_kNN.csv.npy    'raw_results_mlp 1.pkl'  'raw_results_mlp 7.pkl'           svr_rbf_results.pkl
 lstm_results_model_0.pkl  'raw_results_lstm_0 9.pkl'  'raw_results_mlp 2.pkl'  'raw_results_mlp 8.pkl'           test_master_dataframe.pkl
 lstm_results_model_1.pkl  'raw_results_lstm_1 9.pkl'  'raw_results_mlp 3.pkl'  'raw_results_mlp 9.pkl'           train_master_dataframe.pkl
 lstm_results_model_2.pkl  'raw_results_lstm_2 9.pkl'  'raw_results_mlp 4.pkl'   raw_results_svr_linear.npy
 lstm_results_model_3.pkl  'raw_results_lstm_3 9.pkl'  'raw_results_mlp 5.pkl'   raw_results_svr_rbf.npy
'mlp_results 9.pkl'        'raw_results_mlp 0.pkl'     'raw_results_mlp 6.pkl'   svr_linear_results.pkl


All files with raw_results in it are the predictions for the test set. Files of the format *_results.pkl contain the error metric measures. 

MLP and LSTM were run 10 times. Every run of MLP is saved to file raw_results_mlp *.pkl
Three LSTM models were tested and each was run 10 times - all ten runs for a single model are recorded in a single file. To use, simply drop the other columns.


