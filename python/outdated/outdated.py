# submit50 cs50/problems/2022/python/outdated
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        str = input('Date: ').strip()
        if '/' in str:
            month,day,year = map(int, str.split('/'))
        elif ',' in str:
            month,day, year = str.replace(',','').split(' ')
            day = int(day)
            year = int (year)
            month = months.index(month)+1
        else:
            continue
        if (1<=month<=12) and (1<=day<=31):
            break
        else:
            raise ValueError
    except(IndexError,ValueError):
        continue

print(f"{year}-{month:02}-{day:02}")
