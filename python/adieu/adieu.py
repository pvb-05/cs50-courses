# submit50 cs50/problems/2022/python/adieu
import inflect

list = []

p = inflect.engine()

while True:
    try:
        str = input('Name: ').strip()
        list.append(str)
    except EOFError:
        break

print(f'Adieu, adieu, to {p.join(list)}')



