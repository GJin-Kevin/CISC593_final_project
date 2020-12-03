from RoboAdvisor_Data import Robo_Data
from RoboAdvisor_Strategy_BackTesting import Robo_Strategy_BackTesting
from RoboAdvisor_Monitor import Robo_Monitor

import unittest
import pandas as pd 


class test_Robo_Monitor(unittest.TestCase):
    
    def test_Monitor_SMA(self):
        
        robo = Robo_Monitor()
        result = robo.Monitor_SMA()

        self.assertIsNone(result)

    def test_Monitor_RSI(self):

        robo = Robo_Monitor()
        result = robo.Monitor_RSI()
        
        self.assertIsNone(result)

    def test_Monitor_BOLLBands(self):

        robo = Robo_Monitor()
        result = robo.Monitor_BOLLBands()
        
        self.assertIsNone(result)
    
if __name__ == '__main__':
    unittest.main()