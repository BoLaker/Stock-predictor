import yfinance as yf
import pandas as pd

def get_stock_data(ticker,start,end):
    data = yf.download(ticker,start,end)
    return data

def save_to_disk(df,filename):
    df.to_csv(filename, index=True)
    
def load_from_disk(filename):
    df= pd.read_csv(filename, index_col=0)
    df.index = pd.to_datetime(df.index, format="%Y-%m-%d", errors="coerce")
    return df
    



