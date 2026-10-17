# submit50 cs50/problems/2022/python/working
import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)'
    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError("Invalid format")
    else:
        hour_left, minute_left, ap_left = int(match.group(1)), match.group(2), match.group(3)
        hour_right, minute_right, ap_right = int(match.group(4)), match.group(5), match.group(6)
        if minute_left is None:
            minute_left = 0
        if minute_right is None:
            minute_right = 0
        if not (1 <= hour_left <= 12):
            raise ValueError("Invalid time")
        if not (1 <= hour_right <= 12):
            raise ValueError("Invalid time")
        if not (0 <= int(minute_left) <= 59):
            raise ValueError("Invalid time")
        if not (0 <= int(minute_right) <= 59):
            raise ValueError("Invalid time")
        if ap_left == 'PM':
            if hour_left != 12:
                hour_left += 12
        if ap_right == 'PM':
            if hour_right != 12:
                hour_right += 12
        if ap_left == 'AM' and hour_left == 12:
            hour_left = 0
        if ap_right == 'AM' and hour_right == 12:
            hour_right =0
        return f'{hour_left:02}:{minute_left:02} to {hour_right:02}:{minute_right:02}'

if __name__ == "__main__":
    main()
