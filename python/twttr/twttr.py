# submit50 cs50/problems/2022/python/twttr
list = ['U', 'E', 'O', 'A', 'I']

str = input('Input: ').strip()

for item in str:
    if item.upper() in list:
        str = str.replace(item, '')

print(f'Output: {str}')

