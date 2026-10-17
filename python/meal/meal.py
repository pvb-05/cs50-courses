# submit50 cs50/problems/2022/python/meal
def main():
    str = input('What time is it? ')
    time = convert(str)
    if time >= 7.00 and time <= 8.00:
        print('breakfast time')
    elif time >= 12.00 and time <= 13.00:
        print('lunch time')
    elif time >= 18.00 and time <= 19.00:
        print('dinner time')


def convert(time):
    hour, minute = time.split(':')
    hour = float(hour)
    minute = float(minute)/60
    time = hour + minute
    return time

if __name__ == "__main__":
    main()
