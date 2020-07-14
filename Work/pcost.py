# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    Total_Cost=0
    shares_no = 0
    share_price = 0
    with open(filename,'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            share_price = row[2][:-1]
            shares_no = row[1]
            Total_Cost = Total_Cost+(int(shares_no)*float(share_price))
    return Total_Cost        


cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')

