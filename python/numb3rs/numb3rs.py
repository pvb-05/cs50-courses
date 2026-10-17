# submit50 cs50/problems/2022/python/numb3rs
import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]?\d))$"
    ips = ip.split(".")

    if len(ips) != 4:
        return False

    for item in ips:
        match = re.search(pattern, item)
        if match is None:
            return False
    return True


if __name__ == "__main__":
    main()
