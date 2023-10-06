#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv)
    if arg == 0:
        print("0 arguments:")
    else:
        if arg == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(arg - 1))
        for i in range(1, arg):
            print("{}: {}".format(i, argv[i]))
