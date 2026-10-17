# submit50 cs50/problems/2022/python/coke
amount = 50

while amount>0:
    print(f'Amount Due: {amount}')
    str = int(input('Insert coin: ').strip())
    if str == 5:
        amount -= 5
    elif str == 10:
        amount -= 10
    elif str == 25:
        amount -= 25
    else:
        continue

amount = abs(amount)
print(f'Change Owed: {amount}')



