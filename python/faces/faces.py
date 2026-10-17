# submit50 cs50/problems/2022/python/faces
def slime(str):
    return str.replace(':)', '🙂')

def cry(str):
    return str.replace(':(', '🙁')

def main():
    str = input('')
    if str.find(':)'):
        str = slime(str)
    if str.find(':('):
        str = cry(str)
    print(str)
main()
