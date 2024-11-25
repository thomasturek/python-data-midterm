from src.fetcher import get_data
from src.analyzer import create_dataframe
import numpy as np
import pandas as pd

def main():

    dataframe_list = get_data()

    EXR = dataframe_list[0]
    GPN = dataframe_list[1]
    JPM = dataframe_list[2]
    MKTX = dataframe_list[3]

    # TASK 1: Is there a company that has no difference between the Open and Close columns?

    same_open_and_close = []

    for i in range(3):

        if(dataframe_list[i]["Open"].equals(dataframe_list[i]["Close"])):

            same_open_and_close.append(dataframe_list[i])

    if not same_open_and_close:
        print("No stock had the same open and close columns.")
    else: 
        print(same_open_and_close)

    # TASK 2: What is the highest and lowest price for each company (close)?

    max_index = [EXR["Close"].max(), GPN["Close"].max(), JPM["Close"].max(), MKTX["Close"].max()]

    min_index = [EXR["Close"].min(), GPN["Close"].min(), JPM["Close"].min(), MKTX["Close"].min()]

    print("Highest closes for EXR: ", max_index[0])
    print("Highest closes for GPN: ", max_index[1])
    print("Highest closes for JPM: ", max_index[2])
    print("Highest closes for MKTX: ", max_index[3])

    print("Lowest closes for EXR: ", min_index[0])
    print("Lowest closes for GPN: ", min_index[1])
    print("Lowest closes for JPM: ", min_index[2])
    print("Lowest closes for MKTX: ", min_index[3])

    # Task 3

    np.random.seed(0)

    dataframes = [EXR, GPN, JPM, MKTX]
    names = ['EXR', 'GPN', 'JPM', 'MKTX']

    stats = []

    for df, name in zip(dataframes, names):
        
        stat = pd.DataFrame(100 + np.random.randn(100).cumsum(), columns=['price'])

        stat['pct_change'] = stat.price.pct_change()
        
        stat['log_ret'] = np.log(stat.price) - np.log(stat.price.shift(1))
        
        stats.append(EXR['log_ret'])

    print("Stats for EXR: ", stats[0].describe())
    print("Stats for GPN: ", stats[1].describe())
    print("Stats for JPM: ", stats[2].describe())
    print("Stats for MKTX: ", stats[3].describe())

    # Task 5

    print(EXR["Volume"].mean())
    print(GPN["Volume"].mean())
    print(JPM["Volume"].mean())
    print(MKTX["Volume"].mean())

if __name__ == "__main__":
    main()