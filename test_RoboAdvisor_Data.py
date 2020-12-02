from RoboAdvisor_Data import Robo_Data
from RoboAdvisor_Strategy_BackTesting import Robo_Strategy_BackTesting
from RoboAdvisor_Monitor import Robo_Monitor

import unittest
import pandas as pd 


class test_Robo_Data(unittest.TestCase):

    
    def test_yahoo_historical_data(self):

        clien_yahoo = Robo_Data(API = "yahoo")
        result = clien_yahoo.yahoo_historical_data()
        self.assertIsInstance(result, pd.DataFrame)
        

    def test_simfin_historical_data(self):

        client_simfin = Robo_Data(API = "simfin")
        result = client_simfin.simfin_historical_data()
        self.assertIsInstance(result, pd.DataFrame)

    def test_simfin_income_statement(self):
        
        client_simfin = Robo_Data(API = "simfin")
        result = client_simfin.simfin_income_statement()
        self.assertIsInstance(result, pd.DataFrame)


    def test_simfin_balance_sheet(self):

        client_simfin = Robo_Data(API = "simfin")
        result = client_simfin.simfin_balance_sheet()
        self.assertIsInstance(result, pd.DataFrame)


    def test_simfin_cashflow_statment(self):

        client_simfin = Robo_Data(API = "simfin")
        result = client_simfin.simfin_cashflow_statment()
        self.assertIsInstance(result, pd.DataFrame)


    def test_simfin_Derived_Ratios(self):

        client_simfin = Robo_Data(API = "simfin")
        result = client_simfin.simfin_Derived_Ratios()
        self.assertIsInstance(result, pd.DataFrame)

    
if __name__ == '__main__':
    unittest.main()