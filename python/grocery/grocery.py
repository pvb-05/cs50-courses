# submit50 cs50/problems/2022/python/grocery
dict = {}

while True:
    try:
        item = input().strip().upper()
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1
    except EOFError:
        break


for key,item in sorted(dict.items()):
    print(item, key)
