#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, int(add(a, b))))
    print("{} - {} = {}".format(a, b, int(sub(a, b))))
    print("{} * {} = {}".format(a, b, int(mul(a, b))))
    print("{} / {} = {}".format(a, b, int(div(a, b))))
