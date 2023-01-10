#!/usr/bin/python3
def fizzbuzz():
    for fb in range(1, 101):
        if fb % 15 == 0:
            print("FizzBuzz", end=' ')
            continue
        elif fb % 3 == 0:
            print("Fizz", end=' ')
            continue
        elif fb % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{:d}".format(fb),end=' ')


if __name__ == '__main__':
        fizzbuzz()
