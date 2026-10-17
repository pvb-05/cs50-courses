# submit50 cs50/problems/2022/python/watch
import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    pattern = r'<iframe.*src="https?://(www\.)?youtube\.com/embed/(\w+)".*?>'
    match = re.search(pattern, s)
    if match:
        id = match.group(2)
        return f'https://youtu.be/{id}'
    else:
        return None




if __name__ == "__main__":
    main()
