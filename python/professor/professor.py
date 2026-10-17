# submit50 cs50/problems/2022/python/professor

import random

def main():
    level = get_level()

    maths = 0
    scores = 0

    while maths < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        tries = 0
        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer != answer:
                    print('EEE')
                    tries +=1
                    continue
                else:
                    scores += 1
                    break
            except ValueError:
                tries += 1
                print('EEE')
                continue
        if tries == 3:
            print(f"{x} + {y} = {answer}")
        maths += 1
    print(f"Score: {scores}")


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level not in (1,2,3):
                continue
            else:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
