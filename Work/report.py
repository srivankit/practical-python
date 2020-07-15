# report.py
#
# Exercise 2.4
'''
Computes total cost of the portfolio price* no. of shares

'''
import sys
def read_portfolio(filename):
    import csv
    Total_Cost=0.0
    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows) #skipping header
        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print('error in row')
    return portfolio
filename = 'Data/portfolio.csv'
print(read_portfolio(filename))

