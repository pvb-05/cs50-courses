# submit50 cs50/problems/2022/python/scourgify
import sys, csv

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        try:
            list = []
            with open(sys.argv[1], 'r') as file:
                rows = csv.DictReader(file)
                for row in rows:
                    last_name, first_name = row['name'].split(', ')
                    home = row['house']
                    list.append({"first" : first_name, "last" : last_name, "house" : home})
            with open(sys.argv[2], 'w') as file:
                rowss = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
                rowss.writeheader()
                rowss.writerows(list)
        except FileNotFoundError:
            sys.exit('Could not read invalid_file.csv')

main()
