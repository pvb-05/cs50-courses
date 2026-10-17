# submit50 cs50/problems/2022/python/plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # “All vanity plates must start with at least two letters.”
    for i in s[0:2]:
        if i not in alphabet:
            return False

    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not(2<=len(s)<=6):
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end. The first number used cannot be a ‘0’.”
    pos = -1
    for j in s[2:]:
        if j in number:
            pos = s.find(j)
            break

    if pos != - 1:
        if s[pos] == '0':
            return False
        for k in s[pos:]:
            if k not in number:
                return False
            
    return True

main()
