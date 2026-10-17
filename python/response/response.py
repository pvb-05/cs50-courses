# submit50 cs50/problems/2022/python/response
import validators

def main():
    str = input("What's your mail address? ")
    if validators.email(str):
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()
