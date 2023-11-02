#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names_set = dir(hidden_4)
    for i in names_set:
        if i[:2] != "__":
            print(i)
