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
    
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    else:
        df.columns = [str(c).replace("(", "").replace("'", "").split(",")[0] for c in df.columns]
    
    df = df.apply(pd.to_numeric, errors="coerce")
    
    return df.dropna()
    



