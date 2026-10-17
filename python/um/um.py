# submit50 cs50/problems/2022/python/um
import sys, re

def main():
    print(count(input("Text: ")))


def count(s):
    number = 0
    pattern = r"\bum\b"
    match = re.findall(pattern, s.strip().lower())
    if match is None:
        return 0
    else:
        for item in match:
            number += 1
        return number

if __name__ == "__main__":
    main()
