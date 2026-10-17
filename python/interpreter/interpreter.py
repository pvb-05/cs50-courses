# submit50 cs50/problems/2022/python/interpreter
str = input('Expression: ').strip().split(' ')
x = int(str[0])
y = str[1]
z = int(str[2])

if y == '+':
    print(float(x+z))
elif y == '-':
    print(float(x-z))
elif y == '*':
    print(float(x*z))
elif y == '/':
    print(float(x/z))
