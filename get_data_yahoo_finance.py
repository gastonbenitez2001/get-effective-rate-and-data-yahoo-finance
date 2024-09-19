#Imports
import yfinance as yf
import pandas as pd

#Goal: get close price actions
def get_data_yf(list_tickets):
    
    #Get only Close Price
    data = yf.download(list_tickets)['Close']

    #Use when you want only one action
    if isinstance(data,pd.Series):
        
        
        #Transform Serie in Dataframe.
        data = data.to_frame(name=list_tickets[0])

    #Add diary variation, and diary variation cumulative, for each action.
    columns = data.columns
    
    for column in columns:

        data["var_"+column] = data[column].pct_change()
        data["varc_"+column] = data["var_"+column].cumsum()


    #return data
    return data
