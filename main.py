#Imports
from get_data_fed import dowload_data_fed
from get_data_yahoo_finance import get_data_yf


if __name__=='__main__':

    #get data from FED
    df_fed_funds = dowload_data_fed()

    #List tickets - add tickets you want get Close Price
    list_tickets=['AAPL']

    #example multiple tickets
    #list_tickets=['AAPL','TSLA','AMZN','GOOG']

    df_prices = get_data_yf(list_tickets=list_tickets)

    print(df_fed_funds)
    print(df_prices)