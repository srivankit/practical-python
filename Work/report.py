#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

def read_portfolio(filename):
    '''
    Read stock prices into a list

    '''
    from fileparse import parse_csv
    portfolio = parse_csv(filename)
    # import csv
    # Total_Cost=0.0
    # portfolio = []
    # stock = {}
    # with open(filename,'rt') as f:
    #     rows = csv.reader(f)
    #     next(rows) #skipping header
        
    #     for row in rows:
    #         try:
    #            stock ={
    #                'name':row[0],
    #                'shares': int(row[1]),
    #                'price': float(row[2])}
                     
    #         except ValueError:
    #             print('error in row')
            
    #         portfolio.append(stock) 

    return portfolio


def read_prices(filename):
    '''
    Reading prices of the shares using share name

    '''
    from fileparse import parse_csv
    prices = parse_csv(filename, has_headers =False)
    # prices ={}
    # import csv
    # with open(filename,'rt') as f:
    #     rows = csv.reader(f)
        
    #     for row in rows:
    #         try:
    #             prices[row[0]] = float(row[1])
    #         except IndexError:
    #             pass

           
    return prices

def make_report(stocks, price):
    '''
    This function is used to prepare report by taking stocks and prices as input
    
    '''
    rows = []
    prices = dict(price)
    
    for row in stocks:
        stock_name=row['name']
        stock_price=float(row['price'])
        current_price = float(prices[stock_name])
        shares_number = int(row['shares'])
        change = current_price - stock_price
        
        summary = f'{stock_name:>10s}{shares_number:>10d}{f"${current_price:>.2f}":>10}{change:>10.2f}'
        rows.append(summary)
    return rows



#Generate Report
def print_report(report):
    '''
    Prints report in a formatted way
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    header_string = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
    print(header_string)
    print(('-' * 10 + ' ') * len(headers))

    for row in report:
        print(row)

def portfolio_report(portfolio_filename, prices_filename):
    # Read data files and create the report data 
    portfolio = read_portfolio(portfolio_filename)
    # print(portfolio)
    prices    = read_prices(prices_filename)
    
    # Generate the report data
    report = make_report(portfolio, prices)

    #print report by calling print_report function
    print_report(report)

#portfolio_report(portfolio_filename = 'Data/portfolio.csv', prices_filename = 'Data/prices.csv')
# import sys
def main(argv):
    if len(argv) !=3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile,pricefile)

if __name__ == '__main__':
    import sys
    main(sys.argv)
    # print('it is main program')

# if __name__ == 'report':
#     print('Not a main program')
