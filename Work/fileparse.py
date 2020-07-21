# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    try:
        if select and has_headers ==False:
            raise RuntimeError("select argument requires column headers")
        
        with open(filename) as f:
            rows = csv.reader(f, delimiter = delimiter)

            if has_headers ==True:

                # Read the file headers
                headers = next(rows)
                # If a column selector was given, find indices of the specified columns.
                # Also narrow the set of headers used for resulting dictionaries
                if select:
                    indices = [headers.index(colname) for colname in select]
                    headers = select
                else:
                    indices = []
            else:
                indices = []
            records = []

            for row in rows:
                if not row:    # Skip rows with no data
                    continue
            # Filter the row if specific columns were selected
                if types:
                    row = [func(val) for func, val in zip(types, row) ]  
                
                if indices:
                    row = [ row[index] for index in indices ]    
    
                # Make a tuple of records
                #record = tuple(row)
                record = dict(zip(headers,row))
                records.append(record)
        return records

    except RuntimeError as e:
        print(e)

# portfolio = parse_csv('Data/portfolio.csv', select=['name','shares'])
#portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
# shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
# prices = parse_csv('Data/prices.csv', types=[str,float],has_headers=False)
# portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
portfolio = parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)
#print(portfolio)