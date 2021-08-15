from hashlib import new
from tickers import Tickers
from stock_record import StockRecord
import yfinance
import math

class Person():
    def __init__(self, numberOfStocks, tick):
        self.funds = 0
        self.numStocks = numberOfStocks
        self.tickList = tick.getXRandomTicks(numberOfStocks)
        data = yfinance.download(tickers = self.tickList, period = '5d', interval = '1d') # get data of random chosen stocks
        self.records = []
        
        # check for NaN stocks (filter method with list comprehension)
        # print("number of tickers before filter: {}".format(len(self.tickList)))
        # self.tickList = [x for x in self.tickList if not (math.isnan(data['Open'][x][0]) or math.isnan(data['Close'][x][0]))] # filter out NaN stocks (stocks that return null values)
        # print("number of tickers after filter: {}".format(len(self.tickList)))

        #build new tick list. use only valid data form old tick list
        print("number of tickers before filter: {}".format(len(self.tickList)))
        newTicklist = []
        for tck in self.tickList:
            if math.isnan(data['Open'][tck][0]) or math.isnan(data['Close'][tck][0]) or math.isnan(data['Open'][tck][-1]) or math.isnan(data['Close'][tck][-1]): # if the stock value returns NaN then we delete it
                continue # skip this iteration and dont add the stock
            else:
                newTicklist.append(tck)
        self.tickList.clear()
        self.tickList = newTicklist
        del newTicklist
        print("number of tickers before filter: {}".format(len(self.tickList)))

        # invest in stonks
        for stock in self.tickList:
            # if math.isnan(data['Open'][stock][0]): # if the stock value returns NaN then we skip it
            #     continue
            init = data['Open'][stock][0]
            fin = data['Close'][stock][-1]
            if math.isnan(init) or math.isnan(fin):
                print("this is the nan alarm")
            delta = (fin-init)/init*100 # precent change
            buyin = self.numStocks * init
            cashout = self.numStocks * fin - buyin
            self.records.append(StockRecord(stock,init,fin,buyin,cashout,delta))

        #print(data)


    def getFunds(self):
        return self.funds
    def getTickerSelection(self):
        return self.tickList

    def getNetBalance(self):
        self.funds = 0 # clear previous history
        for rec in self.records:
            self.funds = self.funds + rec.cashout # tally up earnings
        return self.funds