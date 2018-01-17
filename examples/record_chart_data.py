import poloniex as polo
import pandas as pd
import numpy as pd
from pprint import pprint

class symbol_history_scraper:
    def __init__(self,exch_name = 'poloneix', db_name = 'poloneix_history.db'):
        self.exchange = exch_name
        self.registered_symbol_list = []
        self.db_name = db_name
        self.exch_API_obj = polo.Poloniex()
        # self.exch_API_obj = polo.Poloniex(proxies={'http': 'socks5://127.0.0.1:1080','https': 'socks5://127.0.0.1:1080'})



    def get_available_markets(self):
        try:
            markets = self.exch_API_obj.returnCurrencies()
        except:
            print "{} markets query Failed".format(self.exchange)
            return False, None
        return True, markets


    def update_historical_candles(self):
        pass


if __name__ =="__main__":
    polo_scraper = symbol_history_scraper()
    flag, markets = polo_scraper.get_available_markets()
    pprint(markets)
