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
    shares_no = 0
    share_price = 0.0
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                share_price = float(row[2])
                shares_no = int(row[1])
                Total_Cost = Total_Cost + (share_price  * shares_no)
            except ValueError:
                print("couldn't parse", row )    
    return Total_Cost        
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')

