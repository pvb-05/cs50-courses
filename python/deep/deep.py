# submit50 cs50/problems/2022/python/deep
str = input ('What is the answer to the Great Question of Life, the Universe and Everything? ')

if str.strip()=='42' or str.lower()=='forty-two' or str.lower()=='forty two':
    print('Yes')
else:
    print('No')
