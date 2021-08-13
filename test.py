import csv
from tickers import Tickers

t1 = Tickers()

print("Number of tickers accounted for {}".format(t1.getNumTickers()))

for i in range(10):
    print(t1.getRandomTick())

