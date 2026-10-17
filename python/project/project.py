import argparse
import time
import sys
from playsound import playsound

def get_args():
    parser = argparse.ArgumentParser(description="Pomodoro")
    parser.add_argument("-w", "--work", type=float, help="working time", default=25)
    parser.add_argument("-s", "--short", type=float, help="breaking time short", default=5)
    parser.add_argument("-l", "--long", type=float, help="breaking time long", default=20)
    arg = parser.parse_args()
    work = arg.work
    short = arg.short
    long = arg.long
    try:
        valid_time(work)
        valid_time(short)
        valid_time(long)
    except ValueError:
        sys.exit("Time can't negative!")
    return work, short, long

def valid_time(minute):
    if minute <= 0:
        raise ValueError
    return True

def count_down(label, minute):
    total_second = int(60*minute)
    while (total_second>0):
        display = format_time(total_second)
        print(f'{label}{display}', end='\r')
        time.sleep(1)
        total_second -= 1
    print(f'{label}{00}:{00}'+' '*40, end='\r')

def format_time(second):
    minutes, seconds = divmod(second,60)
    return f'{minutes:02}:{seconds:02}'

def notify_user(message):
    if category_message(message) == False:
        print(f'🔔🔔{message}🔔🔔')
        playsound('warning.mp3')
    else:
        print(f'🎉✨{message}🎉✨')
        playsound('lofi.mp3')

def category_message(message):
    if message == 'POMODORO CLOCK STOPPED.':
        return False
    else:
        return True
    
def main():
    print("="*75+"POMODORO CLOCK"+"="*74)
    work, break_short, break_long = get_args()
    cycle = 0
    try:
        while True:
            cycle += 1 
            count_down("Working Time: ", work)
            notify_user("WORK HOURS OVER! IT'S BREAK OUT TIME.")
            if cycle % 4 == 0:
                count_down("Long Breaking Time: ",break_long)
                notify_user('LONG BREAK OVER! TIME TO GET BACK TO WORK.')
            else:
                count_down("Short Breaking Time: ", break_short)
                notify_user('SHORT BREAK OVER! TIME TO GET BACK TO WORK.')
    except KeyboardInterrupt:
        print(' '*40)
        notify_user('POMODORO CLOCK STOPPED.')

if __name__ == "__main__":
    main()