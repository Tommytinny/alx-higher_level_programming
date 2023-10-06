#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    sign = "__"
    start = True

    for i in names:
        string = i
        for j in range(len(sign)):
            if string[j] != sign[j]:
                start = False
                break
        if not start:
            print(i)
