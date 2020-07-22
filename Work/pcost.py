#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

'''
Computes total cost of the portfolio price* no. of shares

'''
import sys
def portfolio_cost(filename):
    import csv
    import report
    Total_Cost=0.0
    record = report.read_portfolio(filename)
    for row in record:
        Total_Cost = Total_Cost + (int(row['shares'])*float(row['price']))
    return Total_Cost        
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

def main(argv):
    if len(argv) !=2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    filename = argv[1]
    cost = portfolio_cost(filename)
    print(f'Total cost {cost}')
if __name__ == '__main__':
    import sys
    main(sys.argv)

