import yfinance as yf
import pandas as pd
from datetime import date
from sklearn.model_selection import train_test_split
import numpy as np

def dataset_save(stock:str , start:str , end = date.today()):
        """
        saves dataset of the company

        example:
            dataset_save("AAPL" , start="2010-01-01") , 
        end : default as current 

        """

        if start == None or len(start)!= 10 or  stock == None or len(stock) < 0 :
                raise ValueError("please enter valid arguments")
            
        if isinstance(stock,str) and isinstance(start,str):
            df = yf.download(
                stock,
                start=start,
                end = end 
            )

            df.to_excel(f"dataset_{stock}_{start}.xlsx")
            print("Data saved... ")

def read_df(df_name):
       return



data = pd.read_excel("dataset_AAPL_2010-01-01.xlsx")
values = data.columns


# print(data.describe())
# print(data.shape)
# print(data.head())
df = data.drop([0,1])
print(df)


def sma_50(data):
    """
    mean of first sma50
    calculating mean of first 50 - 1 
    shows NaN on the first 49 and mean in 50th 
    """
    data['SMA50'] = data['Close'].rolling(50).mean()
    return data["SMA50"]

# data['SMA50'] = data['Close'].rolling(50).mean()
# print(data.head())
# print(data["SMA50"])
# data["SMA50"] = data["Close"].rolling(50).mean()
# print(data["SMA50"])

def load_data(excel_file):
      """
       reads excel file converst the price columns name to date 
        used for only download excel file 
        file contained were Date is in 3rd column First Row
    """
      df = pd.read_excel(excel_file)
      df=df.drop([0,1])
      df['Price'] = pd.to_datetime(df['Price'])
      df = df.set_index("Price")
      df.index.name = "Date"
      
      return df

def get_stock_features(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Download stock data and calculate features.

    Returns:
        DataFrame ready for ML training
    """

    df = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True
    )

    # df =  df.drop([0,1])
    # Moving Averages
    df["SMA20"] = df["Close"].rolling(20).mean()
    df["SMA50"] = df["Close"].rolling(50).mean()
    df["SMA200"] = df["Close"].rolling(200).mean()

    # Exponential Moving Averages
    df["EMA20"] = df["Close"].ewm(span=20).mean()
    df["EMA50"] = df["Close"].ewm(span=50).mean()

    # Daily Returns
    df["Returns"] = df["Close"].pct_change()

    # Volatility
    df["Volatility"] = (df["Returns"].rolling(20).std())

    # Volume Change
    "pct_change used to calculate the first and second value "
    df["Volume_Change"] = ( df["Volume"].pct_change())

    # Momentum shift from current to next 9 
    df["Momentum"] = (df["Close"]- df["Close"].shift(10))

    # Target
    """colums that stores the  greater values of the close from previous"""
    df["Target"] = ( df["Close"].shift(-1) > df["Close"])/df["Close"]

    df.dropna(inplace=True)
    
    """ print(load_data("dataset_AAPL_2010-01-01.xlsx"))"""
    return df




      

