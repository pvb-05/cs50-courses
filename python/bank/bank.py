# submit50 cs50/problems/2022/python/bank
str = input('Greeting: ').strip().lower()

if str[0] == 'h':
    if str[0:5] == 'hello':
        print('$0')
    else:
        print('$20')
else:
    print('$100')


