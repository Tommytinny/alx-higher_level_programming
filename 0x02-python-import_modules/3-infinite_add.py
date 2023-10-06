#!/usr/bin/python3
if __name__ == "__main__":
    import sys.argv
    
    added_num = 0
    for i in range(1, len(sys.argv)):
        added_num += int(sys.argv[i])
    print("{}".format(added_num))
