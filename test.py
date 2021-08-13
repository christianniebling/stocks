from tickers import Tickers
from person import Person

t1 = Tickers()
p1 = Person(1000,10,t1)

print(p1.getTickerSelection())

# print("Number of tickers accounted for {}".format(t1.getNumTickers()))
# print("I have access to instance variables {}".format(t1.ticks[2]))
# for i in range(10):
#     print(t1.getRandomTick())

