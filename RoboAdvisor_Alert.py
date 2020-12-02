import smtplib
from email.message import EmailMessage

class Robo_Alert():

    def __init__(self, email_add, email_password, mail_server: str = 'gmail'):
        """[summary] Initialize an instance of Notification.

        Args:
            email_add ([type]): [Email address]
            email_password ([type]): [Email password]
            mail_server (str, optional): [Email server]. Defaults to 'gmail'.
        """        
        self.mail_server = mail_server
        self.email_add = email_add
        self.email_pw = email_password

    def send_buy_notification(self, send_to:str, sec_id, strategy):
        """[summary] Send an email notification

        Args:
            send_to (str): [Email address to send to]
        """        
        
        if self.mail_server == 'gmail':

            msg = EmailMessage()
            msg['Subject'] = '[RoboAdvisor]  BUY Alert'
            msg['From'] = self.email_add
            msg['To'] = send_to
            msg.set_content('BUY Signal: Stoct {} . Buy signal has been triggered for strategy: {}.'.format(sec_id, strategy))

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_add, self.email_pw)
                smtp.send_message(msg)

    def send_sell_notification(self, send_to:str, sec_id, strategy):
        """[summary] Send an email notification

        Args:
            send_to (str): [Email address to send to]
        """        
        
        if self.mail_server == 'gmail':

            msg = EmailMessage()
            msg['Subject'] = '[RoboAdvisor]  SELL Alert'
            msg['From'] = self.email_add
            msg['To'] = send_to
            msg.set_content('SELL Signal: Stoct {} . Sell signal has been triggered for strategy: {}.'.format(sec_id, strategy))

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_add, self.email_pw)
                smtp.send_message(msg)

    def send_hold_notification(self, send_to:str, sec_id, strategy):
        """[summary] Send an email notification

        Args:
            send_to (str): [Email address to send to]
        """        
        
        if self.mail_server == 'gmail':

            msg = EmailMessage()
            msg['Subject'] = '[RoboAdvisor]  HOLD Alert'
            msg['From'] = self.email_add
            msg['To'] = send_to
            msg.set_content('HOLD Signal: Stoct {} . Signal has not been triggered for strategy: {}.'.format(sec_id, strategy))

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_add, self.email_pw)
                smtp.send_message(msg)