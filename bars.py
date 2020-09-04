import csv
import config
import requests
import json
from datetime import datetime


qqqtickers = open('data/qqq_tickers.csv').readlines()
# quick way of iterating thru each line and taking just the ticker
# it was treating each line as a long string, so .split converts line to a list, breaking @ the ,
# turn the string into a list and take second element , .strip is to
# remove xtra space
qqqsymbols = [line.split(',')[2].strip() for line in qqqtickers][1:]
qqqsymbols = ",".join(qqqsymbols)
# for gui
# symbols = input('Please enter the stonks you want to look up separated
# by ,:')


DAILY_BARS = '{}/day?symbols={}&limit=60'.format(config.BARS_URL, qqqsymbols)
# send request to this address, +auth info
r = requests.get(DAILY_BARS, headers=config.Header)
# saves bars in dictionary with bar data as value and sybol as key
data = r.json()

for symbol in data:
    # new file created w each symbol name in data/ohlc folder
    filename = 'data/ohlc/{}.txt'.format(symbol)
    f = open(filename, 'w+')
    f.write('Date, Open, High, Low, Close, Volume, OI\n')
# data is a dictionary so you have to say which keys data u want
    for bar in data[symbol]:
        t = datetime.fromtimestamp(bar['t'])
        day = t.strftime('%Y-%m-%d')
        # each bar is a line
        line = '{}, {}, {}, {}, {}, {}, {}\n'.format(
            day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
        f.write(line)
