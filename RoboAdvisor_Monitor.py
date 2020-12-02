from RoboAdvisor_Data import Robo_Data
from RoboAdvisor_Strategy_BackTesting import Robo_Strategy_BackTesting
from RoboAdvisor_Alert import Robo_Alert


class Robo_Monitor:

    def __init__(self, email_add = None, email_pwd = None):

        self.email_add = email_add
        self.alert = Robo_Alert(email_add, email_pwd)
        self.data = Robo_Data(API = "yahoo")
        self.backtesting = None

    
    def Monitor_SMA(self, sec_id = 'AAPL', sma_short = 20, sma_long = 50, start_date = "2018-10-30"):
    
        # Get real time data from Interactive Broker

        df = self.data.yahoo_historical_data(sec_id = sec_id, start_date = start_date)

        # Check the signal
        # -- sma --
        self.backtesting = Robo_Strategy_BackTesting(df)
        df = self.backtesting.SMA_single_parameter(sma_short = sma_short , sma_long = sma_long)

        print('signal: {}'.format(df.loc[df.shape[0] - 1, 'signal']))
        
        if df.loc[df.shape[0] - 1, 'signal'] == "buy":
            self.alert.send_buy_notification(self.email_add, sec_id, "SMA")
        elif df.loc[df.shape[0] - 1, 'signal'] == "sell":
            self.alert.send_sell_notification(self.email_add, sec_id, "SMA")
        else:
            self.alert.send_hold_notification(self.email_add, sec_id, "SMA")

        
        return None

    def Monitor_RSI(self, sec_id = 'AAPL', period = 14, start_date = "2018-10-30"):
    
        # Get real time data from Interactive Broker

        df = self.data.yahoo_historical_data(sec_id = sec_id, start_date = start_date)

        # Check the signal
        # -- sma --
        self.backtesting = Robo_Strategy_BackTesting(df)
        df = self.backtesting.RSI_single_parameter(period = period)

        print('signal: {}'.format(df.loc[df.shape[0] - 1, 'signal']))
        
        if df.loc[df.shape[0] - 1, 'signal'] == "buy":
            self.alert.send_buy_notification(self.email_add, sec_id, "RSI")
        elif df.loc[df.shape[0] - 1, 'signal'] == "sell":
            self.alert.send_sell_notification(self.email_add, sec_id, "RSI")
        else:
            self.alert.send_hold_notification(self.email_add, sec_id, "RSI")           
        return None


    def Monitor_BOLLBands(self, sec_id = 'AAPL', sma_period = 30, std_period = 20, start_date = "2018-10-30"):
    
        # Get real time data from Interactive Broker

        df = self.data.yahoo_historical_data(sec_id = sec_id, start_date = start_date)

        # Check the signal
        # -- sma --
        self.backtesting = Robo_Strategy_BackTesting(df)
        df = self.backtesting.Bollinger_single_parameter(sma_period = sma_period, std_period = std_period)

        print('signal: {}'.format(df.loc[df.shape[0] - 1, 'signal']))
        
        if df.loc[df.shape[0] - 1, 'signal'] == "buy":
            self.alert.send_buy_notification(self.email_add, sec_id, "BOLLBands")
        elif df.loc[df.shape[0] - 1, 'signal'] == "sell":
            self.alert.send_sell_notification(self.email_add, sec_id, "BOLLBands")
        else:
            self.alert.send_hold_notification(self.email_add, sec_id, "BOLLBands")   
        
        return None          