class StockRecord():
    def __init__(self, ticker, init, fin, buyin, cashout, precent_change):
        self.ticker = ticker
        self.init = init
        self.fin = fin
        self.buyin = buyin
        self.cashout = cashout
        self.precent_change = precent_change
        
    def printRecord(self):
        print("Ticker: {}".format(self.ticker))
        print("Init: {}".format(self.init))
        print("Fin: {}".format(self.fin))
        print("Buy in: {}".format(self.buyin))
        print("Cash out: {}".format(self.cashout))
        print("Precent change: {}".format(self.precent_change))