# submit50 cs50/problems/2022/python/fuel
frac = 0
while True:
    try:
        x,y = input('Fraction: ').split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        else:
            frac = round((x/y)*100)
            break
    except (ValueError, ZeroDivisionError):
        pass

if frac <= 1:
    print('E')
elif frac >= 99:
    print('F')
else:
    print(f'{frac}%')

