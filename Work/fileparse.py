# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and has_headers ==False:
            raise RuntimeError("select argument requires column headers")
                  
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)

        if has_headers ==True:

            # Read the file headers
            headers = next(rows)
            # If a column selector was given, find indices of the specified columns.
            
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
        else:
            indices = []
        records = []

        for rownum, row in enumerate(rows,1):
            if not row:    # Skip rows with no data
                continue
            
            # If specific column indices are selected, pick them out
            if indices:
                row = [ row[index] for index in indices ]  
            
            # Apply type conversion to the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rownum}: Couldn't parse {row}")
                        print(f'Row {rownum} {e}')

        # Make a dictionary/tuple of records
            if has_headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)  
            records.append(record)
    return records

portfolio = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True)
print(portfolio)