# Example
# '1234' should return 1234 as an integer, can't use builtins int()

import sys

def main(num):
    new_num = 0
    base = ord('0')

    for i,n in enumerate(reversed(num)):
        new_num += (ord(n) - base) * (10**i)

    print new_num

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "You need to provide the string to conver"
    else:
        main(sys.argv[1])
