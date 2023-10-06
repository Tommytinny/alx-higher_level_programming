#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    added_num = 0
    for i in range(1, len(argv)):
        added_num += int(argv[i])
        print("{}".format(added_num))
