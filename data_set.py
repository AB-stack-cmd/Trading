import yfinance as yf
import pandas as pd
from datetime import date
from sklearn.model_selection import train_test_split


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