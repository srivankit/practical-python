# pcost.py
#
# Exercise 1.27
'''
Computes total cost of the portfolio price* no. of shares

'''
import sys
def portfolio_cost(filename):
    import csv
    Total_Cost=0.0
    
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start =1):
            record = dict(zip(headers, row))
            try:
                share_price = float(record['price'])
                shares_no = int(record['shares'])
                Total_Cost = Total_Cost + (share_price  * shares_no)
            except ValueError:
                print(f'Row {rowno}: Bad row:{row}' ) 
           
    return Total_Cost        
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

filename = 'Data/portfoliodate.csv'
cost = portfolio_cost(filename)
print(f'Total cost {cost}')

