# submit50 cs50/problems/2022/python/lines
import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] == ".py":
            try:
                with open(sys.argv[1], "r") as file:
                    count = 0
                    rows = file.readlines()
                    for row in rows:
                        if row.isspace():
                            continue
                        elif row.lstrip().startswith("#"):
                            continue
                        else:
                            count += 1
                    print(f"{count}")
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a python file")


main()
