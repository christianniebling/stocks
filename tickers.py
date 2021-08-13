import csv
import random

class Tickers():
    def __init__(self):
        f1 = open("nasdaq_screener.csv", newline='')

        csvreader = csv.reader(f1, delimiter=',') 

        mylist = []
        counter = 0
        for row in csvreader:
            if counter == 0: # skip over the informative 1st row
                counter += 1
                continue
            mylist.append(row[0])
            counter += 1
            if counter > 100: #only run 100 times
                break
        self.ticks = mylist

    def getRandomTick(self):
        return random.choice(self.ticks)

