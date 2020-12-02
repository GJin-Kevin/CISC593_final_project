import simfin as sf
import pandas as pd 
import yfinance as yf
import pandas_datareader.data as web
from simfin.names import *

class Robo_Data:

    def __init__(self, API: str = "yahoo", token: str = None) -> None:
        """Initialize an instance of Robo_Data.

        Args:
            API (str, optional): [Input API name]. Defaults to "simfin".
                            Two options:
                                - simfin API: simfin
                                - yahoo finance API: yahoo
            token (str, optional): [Input token. When using free service, no need to add token]. Defaults to None.
        """         

        if API == "yahoo":
            self.API = API
            self.token = token
        elif API == "simfin":

            if token is None:
                self.token = None

            else:
                self.token = token
            
            #// required settings before using sf API
            sf.set_api_key(api_key=self.token)
            sf.set_data_dir('~/simfin_data/')
        else:
            self.token = token


    def yahoo_historical_data(self, sec_id = 'AMZN', start_date = None, end_date = None) -> pd.DataFrame:
        """ Make API call to yahoo to retrieve historical pricing data. This is free.

        Args:
            sec_id (str, optional): [Security Ticker]. Defaults to 'AMZN'.
            start_date ([type], optional): [Start date of historical pricing data]. Defaults to None.
            end_date ([type], optional): [End date of historical pricing data]. Defaults to None.

        Returns:
            pd.DataFrame
        """        

        df = yf.download(tickers = sec_id, start = start_date, end = end_date)
        df = df.reset_index()
        df = df.rename(columns={"Date": "date", 'Open':'open', 'Close':'close', 'High':'high', 'Low':'low', 'Volume':'volume'})
        df = df[['date', 'open', 'close', 'high', 'low', 'volume']]
        df['date'] = pd.to_datetime(df['date'])

        return df

    def simfin_historical_data(self, sec_id = 'AAPL', period: str = 'Daily', market: str = 'us', start_date = None, end_date = None) -> pd.DataFrame:
        """ Download historica data from simfin as a csv file. 
            Token is needed for the most recent data, which is not free. Can sign up membership on https://simfin.com/

        Args:
            sec_id (str, optional): [stock ticker]. Defaults to 'AAPL'.
            period (str, optional): [the period of stock price]. Defaults to 'Daily'.
            market (str, optional): [stock market, us, de, etc]. Defaults to 'us'.
            start_date ([type], optional): ['xxxx-xx-xx' start date of pricing data]. Defaults to None.
            end_date ([type], optional): ['xxxx-xx-xx' end date of pricing data]. Defaults to None.

        Returns:
            pd.DataFrame
        """        

        df = sf.load_shareprices(variant= period, market=market)
       
        df = df.loc[sec_id]
        df = df.reset_index()
        df = df.rename(columns={"Date": "date", 'Open':'open', 'Close':'close', 'High':'high', 'Low':'low', 'Volume':'volume'})
        
        df = df[['date', 'open', 'close', 'high', 'low', 'volume']]
        df['date'] = pd.to_datetime(df['date'])


        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        if start_date is None and end_date is None:
            return df
        elif start_date is not None and end_date is None:
            df = df[(df['date'] >= start_date)]
        elif start_date is None and end_date is not None:
            df = df[(df['date'] <= end_date)]
        else:
            df = df[(df['date'] >= start_date) & (df['date'] <= end_date )]

        df = df.reset_index()
        return df

    def simfin_income_statement(self, sec_id: str = 'AAPL', period : str = 'quarterly', market :str = 'us') -> pd.DataFrame:
        """Download income statement data from simfin as a csv file. 

        Args:
            sec_id (str, optional): [stock tiker]. Defaults to 'AAPL'.
            period (str, optional): [annual, quarterly]. Defaults to 'annual'.
            market (str, optional): [us, de, etc]. Defaults to 'us'.

        Returns:
            pd.DataFrame: 
        """        

        df_income = sf.load_income(variant=period, market=market,
              index=[TICKER, REPORT_DATE, FISCAL_PERIOD],
              parse_dates=[REPORT_DATE, PUBLISH_DATE, RESTATED_DATE])
        df_income = df_income.loc[sec_id]

        return df_income


    def simfin_balance_sheet(self, sec_id: str = 'AAPL', period : str = 'quarterly', market :str = 'us') -> pd.DataFrame:
        """Download balance sheet data from simfin as a csv file. 

        Args:
            sec_id (str, optional): [stock ticker]. Defaults to 'AAPL'.
            period (str, optional): [annual, quarterly]. Defaults to 'quarterly'.
            market (str, optional): [us, de, etc]. Defaults to 'us'.

        Returns:
            pd.DataFrame: 
        """        

        df_balance = sf.load_balance(variant = period, market = market)

        df_balance = df_balance.loc[sec_id]

        return df_balance

    def simfin_cashflow_statment(self, sec_id: str = 'AAPL', period : str = 'quarterly', market :str = 'us') -> pd.DataFrame:
        """Download cashflow statement data from simfin as a csv file. 

        Args:
            sec_id (str, optional): [stock ticker]. Defaults to 'AAPL'.
            period (str, optional): [annual, quarterly]. Defaults to 'quarterly'.
            market (str, optional): [us, de, etc]. Defaults to 'us'.

        Returns:
            pd.DataFrame: 
        """        

        df_cashflow = sf.load_cashflow(variant = period, market = market)

        df_cashflow = df_cashflow.loc[sec_id]

        return df_cashflow
    
    def simfin_Derived_Ratios(self, sec_id: str = 'AAPL', variant: str = 'annual', market :str = 'us') -> pd.DataFrame:
        """Download financial ratio data, like PE, PS, etc from simfin as a csv file. 

        Args:
            sec_id (str, optional): [stock ticker]. Defaults to 'AAPL'.
            variant (str, optional): [annual, quarterly]. Defaults to 'quarterly'.
            market (str, optional): [us, de, etc]. Defaults to 'us'.

        Returns:
            pd.DataFrame: 
        """        

        df_ratios = sf.load_derived(variant = variant, market = market)

        df_ratios = df_ratios.loc[sec_id]

        return df_ratios
        

        

