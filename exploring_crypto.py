#imports
import pandas as pd
import json
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# opening json file and converting it to readable DataFrame
data = json.load(open('BTC_data.json'))

#reading in current data from coinmarketcap API
current = pd.DataFrame(data['data'])

# printing first few lines and looking at summary stats
print(current.head())
print(current.info())

'''---------------------------------------------------------------------------------------------'''
# new DF with name + price
current_prices = current[['name', 'price']]

# setting price as index
current_prices = current_prices.set_index(['price'], drop = True)

# sorting values by price descending
current_prices = current_prices.sort_values(['price'], ascending=False)

# loc'ing first 10 coins
current_prices = current_prices.iloc[:10]

print(current_prices)

'''---------------------------------------------------------------------------------------------'''

# new DF with market cap + id + name
mkt_cap_raw = current[['name', 'id', 'market_cap']]

# loc'ing to top 10 and subbing in ID as index
top10 = mkt_cap_raw.iloc[:10]
cap10 = top10.set_index(['id'], drop = True)

# assigning new column as percent share of total
cap10 = cap10.assign(pct_share=lambda x: ((cap10.market_cap) / cap10.market_cap.sum()) * 100)

# setting the style
plt.style.use('seaborn-bright')

# graphing results in barplot
ax = cap10.plot.bar(x='name', y='pct_share', title='8/30/2019: % market cap', legend=None)

# adjusting xticks and rotating text
plt.xticks(size=9, rotation=45)

# adjusting margin on x axis
plt.subplots_adjust(bottom=0.15, left=0.10)

# removing x label
ax.set_xlabel('')

# setting y label
ax.set_ylabel('% share')

plt.show()

'''----------------------------------------------------------------------------------------------'''

# new DF with name + 24h percent change + 7d percent change
volatility = current[['name', 'percent_change_24h', 'percent_change_7d']]

# setting index to name column
volatility = volatility.set_index(['name'], drop = True).dropna()

# soring DF in descending order
volatility = volatility.sort_values(['percent_change_24h'], ascending=False)

# subsetting DF with just 24 hr data
volatility_24h = volatility['percent_change_24h']

# setting the style
plt.style.use('seaborn-bright')

# setting the graph dimensions
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(13, 7))

# setting the main title and shared y label
fig.suptitle('8/30/2019: Biggest Winner/Loser over 24 Hours', fontsize=30)
axes[0].set_ylabel('% change')

# plotting volatility_24h top 10 winners
ax = volatility_24h[:10].plot.bar(ax=axes[0])
ax.xaxis.set_tick_params(labelsize=7, rotation=45)
ax.set_xlabel('')

# plotting volatility_24h top 10 losers
ax = volatility_24h[-10:].plot.bar(ax=axes[1], color='darkred')

# adjusting label size and text rotation
ax.xaxis.set_tick_params(labelsize=7, rotation=45)

# removing x label
ax.set_xlabel('')

# adjusting bottom margin
plt.subplots_adjust(bottom=0.13)

plt.show()

'''----------------------------------------------------------------------------------------------'''

# subsetting volatility DF with 7d data
volatility_7d = volatility['percent_change_7d']


# sorting 7d data by descending values
volatility_7d = volatility_7d.sort_values(ascending=True)

# setting the style
plt.style.use('seaborn-bright')

# setting the graph dimensions
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(13, 7))

# setting the main title and shared y label
fig.suptitle('8/30/2019: Biggest Winner/Loser over 7 days', fontsize=30)
axes[0].set_ylabel('% change')

# plotting volatility_7d top 10 winners
ax = volatility_7d[:10].plot.bar(ax=axes[0], color='darkred')
ax.xaxis.set_tick_params(labelsize=7, rotation=45)
ax.set_xlabel('')

# plotting volatility_7d top 10 losers
ax = volatility_7d[-10:].plot.bar(ax=axes[1])

# adjusting label size and text rotation
ax.xaxis.set_tick_params(labelsize=7, rotation=45)

# removing x label
ax.set_xlabel('')

# adjusting bottom margin
plt.subplots_adjust(bottom=0.14)

plt.show()
