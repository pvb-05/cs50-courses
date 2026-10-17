# submit50 cs50/problems/2022/python/pizza
import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        if sys.argv[1][-4:] == '.csv':
            try:
                with open(sys.argv[1], 'r') as file:
                    table = []
                    rows = csv.reader(file)
                    for row in rows:
                        table.append(row)
                    print(tabulate(table,tablefmt='grid', headers = "firstrow"))
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a CSV file')

main()
