#!/usr/bin/python3
i = 0
while i <= 89:
    if i % 10 == 0:
        i += 1 + i // 10
    print("{:02d}".format(i), end='\n' if i == 89 else ", ")
    i += 1
