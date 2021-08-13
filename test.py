import csv
import tickers

t1 = tickers.Tickers()


for i in range(10):
    print(t1.getRandomTick())

# f1 = open("nasdaq_screener.csv", newline='')

# csvreader = csv.reader(f1, delimiter=',')

# print(next(csvreader))

# mylist = []
# counter = 0
# for row in csvreader:
#     if counter == 0: # skip over the informative 1st row
#         counter += 1
#         continue

#     print(row)
#     counter += 1
#     if counter > 10:
#         break