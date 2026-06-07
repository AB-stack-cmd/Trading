import yfinance as yf
import pandas as pd
from datetime import date
from sklearn.model_selection import train_test_split
import numpy as np

def dataset_save(company_name:str , start:str , end = date.today()):
        """
        saves dataset of the company

        dataset_save("AAPL" , start="2010-01-01") , 
        end : default as current 

        """

        if start == None or len(start)!= 10 or  company_name == None or len(company_name) < 0 :
                raise ValueError("please enter valid arguments")
            
        if isinstance(company_name,str) and isinstance(start,str):
            df = yf.download(
                company_name,
                start=start,
                end = end 
            )

            df.to_excel(f"dataset_{company_name}_{start}.xlsx")
            print("Data saved... ")

def read_df(df_name):
       return



data = pd.read_excel("dataset_AAPL_2010-01-01.xlsx")


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
# print(data["SMA50"].isna().sum())

def load_data(excel_file):
      """
      reads excel file converst the price columns name to date """
      df = pd.read_excel(excel_file)
      df=data.drop([0,1])
      df['Price'] = pd.to_datetime(df['Price'])
      df = df.set_index("Price")
      df.index.name = "Date"
      
      return df

print(load_data("dataset_AAPL_2010-01-01.xlsx"))
