#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        j = number * -1
        lastdigit = j % 10
    else:
        lastdigit = number % 10
    print(lastdigit, end='')
    return (lastdigit)
