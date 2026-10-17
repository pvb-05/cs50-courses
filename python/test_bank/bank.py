def main():
    str = input('Greeting: ').strip().lower()
    money = value(str)
    print(f'${money}')

def value(greeting):
    if greeting[0] == 'h':
        if greeting[0:5] == 'hello':
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()



