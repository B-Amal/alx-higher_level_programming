#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_mul = []
    len_l = len(my_list)
    for i in range(len_l):
        if my_list[i] % 2 == 0:
            list_mul.append(True)
        else:
            list_mul.append(False)
    return (list_mul)
