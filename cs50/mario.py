while True:
    try:
        x = int(input("Height: "))
    except:
        print("Value Error")
    else:
        if x > 0 and x < 9:
            break
        else:
            continue
def main():
    print_hash(x)

def print_hash(n):
    for i in range(n):
        for _ in range(n - 1):
            print(" ", sep = "", end = "")
        print("#"*(i+1),sep = "")
        n = n -1

main()
