#!/usr/bin/python3
for number in range(9):
    for j in range(number + 1, 10):
        if number * 10 + j < 89:
            print("{:d}{:d}".format(num, j), end=", ")
print("{:d}".format(89))
