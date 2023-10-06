#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("10 + 5 = {}".format(int(add(a, b))))
    print("10 - 5 = {}".format(int(sub(a, b))))
    print("10 * 5 = {}".format(int(mul(a, b))))
    print("10 / 5 = {}".format(int(div(a, b))))
