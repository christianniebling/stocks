# My functions
from tickers import Tickers
from person import Person

# Raw Package
import numpy
import pandas 

# Data Source
import yfinance

# Data viz
import plotly.graph_objs as go
import matplotlib.pyplot


t1 = Tickers() # we only need 1 ticker object to generate the whole list of NYSE tickers
p1 = Person(100,t1)
p1.getNetBalance()
print(p1.funds)


