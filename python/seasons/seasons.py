# submit50 cs50/problems/2022/python/seasons
import sys
from datetime import date
import inflect

def main():
    try:
        print(convert(input('Date of birth: ')))
    except ValueError:
        sys.exit('Invalid date')

def convert(s):
    birth = date.fromisoformat(s)
    dates = date.today()
    day = dates - birth
    minute = day.days * 24 * 60
    p = inflect.engine()
    str = p.number_to_words(round(minute), andword='')
    return f'{str.capitalize()} minutes'

if __name__ == '__main__':
    main()
