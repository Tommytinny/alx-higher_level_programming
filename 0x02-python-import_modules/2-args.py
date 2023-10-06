#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg == 0:
        print("0 arguments:")
    else:
        if arg == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(arg - 1))
        for i in range(1, arg):
            print("{}: {}".format(i, sys.argv[i]))
