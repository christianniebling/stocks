from tickers import Tickers

class Person():
    def __init__(self, funds, numberOfStocks, tick):
        self.funds = funds
        self.numStocks = numberOfStocks
        self.tickList = tick.getXRandomTicks(numberOfStocks)

    def getFunds(self):
        return self.funds
    def getTickerSelection(self):
        return self.tickList