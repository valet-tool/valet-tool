#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:50:03 2021

@author: nd7896
"""

import numpy as np
import pandas as pd


if __name__ == "__main__":

    ping_data = pd.read_csv("../niranjana/tactic-data-3-master/ping.csv")
    tva_data = pd.read_csv("../niranjana/tactic-data-3-master/tva_output.csv")
    
    old_ping_data_train = pd.read_csv("/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_1_tactic_1_train.csv")
    
    old_ping_data_test = pd.read_csv("/home/nd7896/data/TVA_E/valet-tool/parse_tactics/normalized_tva_server_1_tactic_1_test.csv")
    
    print("Shape of ping data:", ping_data.shape)
    print("Shape of vanilla tva data:", tva_data.shape)
    
    print("Shape of old train data:", old_ping_data_train.shape)
    print("Shape of old test data:", old_ping_data_test.shape)
    print("Shape of old data (total):", old_ping_data_train.shape[0] + old_ping_data_test.shape[0])
    
    indices = np.isin(tva_data["Timestamp"].iloc[:].values, ping_data["Timestamp"].iloc[:].values)
    
    



