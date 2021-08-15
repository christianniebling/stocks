from tickers import Tickers
from person import Person
import yfinance
import random

t1 = Tickers()
#p1 = Person(10,t1)

l1 = ["ANGO", "AAPL", "UBER", "NVDA"]
data = yfinance.download(tickers = l1, period = '5d', interval = '5m')
print(data["Close"][l1[1]])

print(random.choice(l1))

#print(p1.getTickerSelection())


