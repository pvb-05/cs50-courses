
def main():
    while True:
        try:
            fraction_input = input("Fraction: ")
            fraction = convert(fraction_input)
            str = gauge(fraction)
            print(str)
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x,y = fraction.split('/')
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return round((x/y)*100)

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()




