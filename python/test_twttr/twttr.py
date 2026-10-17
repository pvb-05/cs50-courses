list = ['U', 'E', 'O', 'A', 'I']

def main():
    word = input('Input: ').strip()
    shorten(word)
    print(f'Output: {word}')


def shorten(word):
    for item in word:
        if item.upper() in list:
            word = word.replace(item, '')

if __name__ == "main":
    main()
