import pandas as pd
import numpy as np
from data_set import get_stock_features
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics
import yfinance as yf

df = yf.download(
        "AAPL",
        start="2010-01-01",
        end="2026-01-01",
        auto_adjust=True
    )

df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

# df.drop(df.index[2])
# df = get_stock_features()
# print(df.head())

df = get_stock_features("AAPL",start="2010-01-01",end="2026-01-01")
print(df.head())
# print(df.head())
FEATURES = [
    "Close",
    "Volume",
    "Returns",
    "SMA20",
    "SMA50",
    "SMA200",
    "Volatility"
]

''' x features for traning and y for the output '''
X = df[FEATURES]
print("shape")
print(X.shape)
Y = df["Target"]

x_train ,x_test ,y_train ,y_test =train_test_split(X,Y,test_size=0.2,random_state=42)

scaler = MinMaxScaler()

x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)



# class Predict()