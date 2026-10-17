# submit50 cs50/problems/2022/python/game

import random

while True:
    try:
        n = int(input('Level: ').strip())
        if n < 0:
            continue
        else:
            ran = random.randint(1,n)
            break
    except ValueError:
        continue

while True:
    try:
        guess = int(input('Guess: ').strip())
        if guess < ran:
            print('Too small!')
            continue
        elif guess > ran:
            print('Too large!')
            continue
        elif guess == ran:
            print('Just right!')
            break
    except ValueError:
        continue


