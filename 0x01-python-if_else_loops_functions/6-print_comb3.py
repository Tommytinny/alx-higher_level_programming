#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i and i != j and i < 8:
            print("{}{}, ".format(i, j), end="")
        elif j > i and i != j and i > 7:
            print("{}{}".format(i, j))
