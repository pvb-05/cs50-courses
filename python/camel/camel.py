# submit50 cs50/problems/2022/python/camel
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

str = input('camelCase: ').strip()

for item in str:
    if item in list:
        str = str.replace(item, '_'+item.lower())

print(f"snake_case: {str}")
