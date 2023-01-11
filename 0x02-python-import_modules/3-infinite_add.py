#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    result  = 0
    for arg in argv:
        if arg != argv[0]:
            result += int(arg)
    print(result)
