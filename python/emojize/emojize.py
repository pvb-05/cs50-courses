# submit50 cs50/problems/2022/python/emojize
import emoji

str = input('Input: ')

print(f'Output: {emoji.emojize(str, language='alias')}')


