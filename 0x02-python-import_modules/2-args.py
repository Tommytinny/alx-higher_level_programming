#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv)
    argn = 0
    if arg == 0:
        print("0 arguments:")
    else:
        if arg == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(arg - 1))
        for i in range(1, len(argv)):
            argn += 1
            print("{}: {}".format(argn, argv[i]))
