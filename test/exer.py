import re
import sys

def get_address(port):
    f=open('1.txt')
    data = ''
    for line in f:
        if line != '\n':
            data += line
        else:
            break


if __name__ == "__main__":
    port = sys.argv[1]
    print(get_address(port))
