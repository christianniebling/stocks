# My functions
from tickers import Tickers

# Raw Package
import numpy
import pandas 

# Data Source
import yfinance

# Data viz
import plotly.graph_objs as go
import matplotlib.pyplot

#data = yfinance.download(tickers = 'UBER', period = '5d', interval = '5m')
t1 = Tickers()
#tickName = 'UBER'
tickName = t1.getRandomTick()
stock = yfinance.Ticker(tickName)
data = stock.history(period='1y', interval='1d')

investment = 50 # unit is number of stocks
init = data['Open'][0]
fin = data['Close'][-1]
delta = (fin-init)/init*100 #precent change

buyin = investment * init #buy in price
cashout = fin * investment - buyin #cash out price

print("Date range {} to {}".format(data.index[0], data.index[-1]))
print("You buy {} stocks of {}".format(investment, stock.info['shortName']))
print("This costs you {} USD".format(buyin))
print("The stock's precent change is {}".format(delta))
print("Your gain is {}".format(cashout))

xaxis = []
yaxis = []
counter = 0
for x in data['Close']:
    yaxis.append(x)
    xaxis.append(counter)
    counter += 1
matplotlib.pyplot.plot(xaxis, yaxis)
matplotlib.pyplot.show()
#data['Close'].plot()