import btalib
import pandas as pd

# Read a csv file into a pandas dataframe
df = pd.read_csv('data/ohlc/AMD.txt', parse_dates=True, index_col='Date')
# sma obj created
sma = btalib.sma(df)
rsi = btalib.rsi(df)
macd = btalib.macd(df)

df['sma'] = sma.df
df['rsi'] = rsi.df
df['macd'] = macd.df['macd']
df['signal'] = macd.df['signal']
df['histogram'] = macd.df['histogram']
# print(df)
oversold_days = df[df['rsi'] > 70]


print(df)
