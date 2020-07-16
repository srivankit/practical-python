# report.py
#
# Exercise 2.4

def read_portfolio(filename):
    '''
    Read stock prices into a list

    '''
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
    '''
    Reading prices of the shares using share name

    '''
    
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


# print(prices)
# print(portfolio)
# cost = 0
# sell = 0
# for row in portfolio:
#     cost +=row['shares']*row['price']
#     sell +=row['shares']*prices[row['name']]
  
# if sell-cost >0:
#     print(f'Gain on the portfoli is {round((sell-cost),2)}')
# elif sell-cost<0:
#     print(f'Loss on the portfoli is {round((cost-sell),2)}')
# else:
#     print('No Profit or Loss on the portfolio')
def make_report(stocks, price):
    '''
    This function is used to prepare report by taking stocks and prices as input
    
    '''
    rows = []
    for row in stocks:
        stock_name=row['name']
        stock_price=row['price']
        shares_number = row['shares']
        change = price[stock_name]-stock_price
        dollar = '$'
        summary = f'{stock_name:>10s}{shares_number:>10d}{dollar:>7s}{stock_price:<5.2f}{change:>10.2f}'
        rows.append(summary)
    return rows

# Read data files and create the report data 
portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

# Generate the report data
report = make_report(portfolio, prices)

#Generate Report
headers = ('Name', 'Shares', 'Price', 'Change')
header_string = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
print(header_string)
print(('-' * 10 + ' ') * len(headers))

for row in report:
    print(row)

# cost = [(s['name'],s['shares']) for s in portfolio if (s['shares']*s['price'])>10000]

# print(cost)
# names = { s['name'] for s in portfolio }

# stocks = { s: prices[s] for s in names}
# print(stocks)