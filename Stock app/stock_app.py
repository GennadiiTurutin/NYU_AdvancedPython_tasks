
# coding: utf-8

import urllib.request
import datetime as dt
import matplotlib.pyplot as plt

def get_data(ticker, interval='5min', datatype='csv'):   
    """ Retrieves data from the website according to parameters ticker and interval"""
    
    ALPHAVANTAGE_URL = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
                                 '&symbol={}&interval={}&apikey=13URDG5IDU1NOXZN'
                                     '&datatype={}'.format(ticker, interval, datatype))
       
    request_handle = urllib.request.urlopen(ALPHAVANTAGE_URL)
    raw_data = request_handle.read()
    raw_data = raw_data.decode('utf-8')
    raw_data = raw_data.splitlines()
     

    data = raw_data[1].rstrip()
    data = data.split(',')
    date = data[0][:10]
    update = data[0]
    last_close = data[4]
    last_volume = data[5]
      
    close_history = [] 
    
    for line in raw_data:
        line = line.rstrip()
        line = line.split(',')
        if line[0][:10] == date:
            close_history.append(line[4])
                
    return date, update, last_close, last_volume, close_history


def write_chart_to_file(stock):
    """Generates an image with information on stock price for the last business day"""
    
    plt.plot(stock.history)
    plt.title(stock.ticker)
    plt.savefig(stock.ticker + '_chart.png')

def get_html(stock):
    fh = open(STOCK_PRICE_TEMPLATE)
    template= fh.read()
    page = template.format(obj = stock)
    return(page)  

class Stock: 

    def __init__(self, ticker, interval='5min'):
        date, update, last_close, last_volume, close_history = get_data(ticker, interval)
        self.date = date
        self.last_updated = update
        self.current_price = last_close
        self.volume = last_volume
        self.history = list(reversed(close_history)) 
        self.ticker = ticker
            
            
stock = Stock('AAPL') 
write_chart_to_file(stock)

