# report.py
#
# Exercise 2.4
'''
Read stock proces into a list

'''

def read_portfolio(filename):
    import csv
    Total_Cost=0.0
    portfolio = []
    stock = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(rows) #skipping header
        
        for row in rows:
            try:
               stock ={
                   'name':row[0],
                   'shares': int(row[1]),
                   'price': float(row[2])}
                     
            except ValueError:
                print('error in row')
            
            portfolio.append(stock) 

    return portfolio


def read_prices(filename):
    prices ={}
    import csv
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

           
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')
# print(prices)
# print(portfolio)
cost = 0
sell = 0
for row in portfolio:
    cost +=row['shares']*row['price']
    sell +=row['shares']*prices[row['name']]
  
if sell-cost >0:
    print(f'Gain on the portfoli is {round((sell-cost),2)}')
elif sell-cost<0:
    print(f'Loss on the portfoli is {round((cost-sell),2)}')
else:
    print('No Profit or Loss on the portfolio')
