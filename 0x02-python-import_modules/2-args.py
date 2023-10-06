#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = int(len(argv)) - 1
    argn = 0
    if arg == 0:
        print("0 arguments:")
    else:
        print("{} arguments:".format(arg))
        for i in range(1, len(argv)):
            argn += 1
            print("{}: {}".format(argn, argv[i]))
