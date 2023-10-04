#!/usr/bin/python3
count = 1
for i in range(122, 96, -1):
    if count % 2 == 0:
        alpha = i - 32
    else:
        alpha = i
    count += 1
    print("{}".format(chr(alpha)), end="")
