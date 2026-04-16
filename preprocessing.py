import numpy as np

"""
creates a matrix (x) of previous stock prices and a target vector (y) of prices the next day
"""

def create_matrix_target(df, window_size):
   
    series = df["Close"].values.astype(float) #uses closed price
    
    x = []
    y = []
    
    for i in range(len(series)-window_size):
        window = series[i:i+window_size]
        target = series[i+window_size]
        
        x.append(window)
        y.append(target)
    
    return np.array(x), np.array(y)
       

"""
standardize the data by using z-score (z=(x-mean)/std)
"""       
def standardize_data(x_train, x_test):
    mean = np.mean(x_train, axis=0)
    std = np.std(x_train,axis=0)
    
    std[std==0] = 1.0
    
    x_train_scaled = (x_train-mean)/std
    x_test_scaled = (x_test-mean)/std
    
    return x_train_scaled, x_test_scaled, mean, std