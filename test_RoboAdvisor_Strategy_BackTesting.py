from RoboAdvisor_Data import Robo_Data
from RoboAdvisor_Strategy_BackTesting import Robo_Strategy_BackTesting
from RoboAdvisor_Monitor import Robo_Monitor

import unittest
import pandas as pd 


class test_Robo_Strategy_BackTesting(unittest.TestCase):
    
    def test_SMA_single_parameter(self):

        clien_yahoo = Robo_Data(API = "yahoo")
        df = clien_yahoo.yahoo_historical_data(start_date="2019-01-01")

        backtesting = Robo_Strategy_BackTesting(df)
        result = backtesting.SMA_single_parameter()

        self.assertIsInstance(result, pd.DataFrame)


    def test_SMA_bulk_parameters(self):

        clien_yahoo = Robo_Data(API = "yahoo")
        df = clien_yahoo.yahoo_historical_data(start_date="2019-01-01")

        backtesting = Robo_Strategy_BackTesting(df)
        result = backtesting.SMA_bulk_parameters()

        self.assertIsInstance(result, pd.DataFrame)
        

    def test_RSI_single_parameter(self):

        clien_yahoo = Robo_Data(API = "yahoo")
        df = clien_yahoo.yahoo_historical_data(start_date="2019-01-01")

        backtesting = Robo_Strategy_BackTesting(df)
        result = backtesting.RSI_single_parameter()

        self.assertIsInstance(result, pd.DataFrame)

    def test_Bollinger_single_parameter(self):

        clien_yahoo = Robo_Data(API = "yahoo")
        df = clien_yahoo.yahoo_historical_data(start_date="2019-01-01")

        backtesting = Robo_Strategy_BackTesting(df)
        result = backtesting.Bollinger_single_parameter()

        self.assertIsInstance(result, pd.DataFrame)
        
        

if __name__ == '__main__':
    unittest.main()