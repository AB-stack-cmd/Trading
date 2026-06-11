import pandas as pd
import numpy as np
from data_set import get_stock_features
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

df = yf.download(
        "AAPL",
        start="2010-01-01",
        end="2026-01-01",
        auto_adjust=True
    )

df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

df = df.drop([0,1])
print(df.head())
DF=df.drop("Date",axis=0).groupby("Close").mean()
print("'''''''''''''''''''''''''''''''''")

# print(df.head())
FEATURES = [
    "Close",
    "Volume",
    "Returns",
    "SMA20",
    "SMA50",
    "SMA200",
    "RSI14",
    "MACD",
    "Volatility"
]

''' x features for traning and y for the output '''
X = df["Close"]
# print(X.shape)
Y = df["Target"]

x_train ,x_test ,y_train ,y_test =train_test_split(X,Y,test_size=0.2,random_state=42)

scaler = MinMaxScaler()

x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)



# class Predict()