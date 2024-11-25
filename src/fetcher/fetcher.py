import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_data(): 

    df_exr = pd.read_csv('data/exr.csv')

    df_gpn = pd.read_csv('data/gpn.csv')

    df_jpm = pd.read_csv('data/jpm.csv')

    df_mktx = pd.read_csv('data/mktx.csv')

    dataframe_list = []

    dataframe_list.append(df_exr)
    dataframe_list.append(df_gpn)
    dataframe_list.append(df_jpm)
    dataframe_list.append(df_mktx)

    return dataframe_list
